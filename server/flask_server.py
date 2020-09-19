# PARA INICIAR EL SERVER:
# .\flask_env\Scripts\Activate.ps1
# $env:FLASK_APP = "server/flask_server.py"
# $env:FLASK_ENV = "development"
# $env:EnableLogging = "True"
# python -m flask run
from flask import Flask
from flask import request
from flask import jsonify
import logging
from server.popos.commander import Commander
from server.popos import fake_measurements as FakeMeasurements
import os
import datetime
from config import *
import time
from pdb import set_trace as st

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
try:
    app.logger.disabled = not os.environ["EnableLogging"]
except:
    app.logger.disabled = True

if deviceIndependant:
    SerialConnection = FakeMeasurements.FakeMeasurements(app.logger)
else:
    SerialConnection = Commander()
    Commander.logger = app.logger
    
@app.route('/')
def status():
    return jsonify(api_status())

@app.route('/list_devices', methods=['GET'])
def list_devices():
    data = SerialConnection.list_devices()
    return jsonify(data)

@app.route('/open_connection', methods=['POST'])
def open_connection():
    if SerialConnection.connection_available: return connection_already_exists()
    device = request.json["device"]
    status = SerialConnection.connect_device(device)
    if status == 200: 
        message_response = "Device connected"
    else:
        message_response = "Could not find an device - is it plugged in?"
    return jsonify(message = message_response), status

@app.route('/close_connection', methods=['DELETE'])
def close_connection():
    if not SerialConnection.connection_available: return no_connection()
    if Commander.mode != None: Commander.stop()
    device = request.json["device"]
    response = SerialConnection.disconnect_device(device)
    if "error" in response: # TODO this if is falopa
        status = 400
    else:
        status = 202
    return jsonify(response), status

@app.route('/read_temperature', methods=['GET'])
def get_temperature():
    if not SerialConnection.connection_available: return no_connection()
    temperature = SerialConnection.read_temperature()
    response = { "temperature": str(temperature) }
    if request.args.get('consumer') == "UI": response["status"] = api_status()
    return jsonify(response), 200

@app.route('/cold', methods=['POST'])
def cold():
    if not SerialConnection.connection_available: return no_connection()
    if temperature_out_of_range(request): return invalid_temperature()
    SerialConnection.cold(request.json["objective_temperature"])
    return '', 202

@app.route('/hot', methods=['POST'])
def hot():
    if not SerialConnection.connection_available: return no_connection()
    if temperature_out_of_range(request): return invalid_temperature()
    SerialConnection.hot(request.json["objective_temperature"])
    return '', 202

@app.route('/stop_device', methods=['POST'])
def stop_device():
    if not SerialConnection.connection_available: return no_connection()
    SerialConnection.stop()
    return '', 202

@app.route('/error', methods=['POST'])
def error():
    if not SerialConnection.connection_available: return no_connection()
    SerialConnection.error_set(request.json["error"])
    return '', 202

@app.route('/error_clear', methods=['POST'])
def error_clear():
    if not SerialConnection.connection_available: return no_connection()
    SerialConnection.error_clear()
    return '', 202

def temperature_out_of_range(request):
    if 10 <= float(request.json["objective_temperature"]) <= 50:
        return False
    return True

def invalid_temperature():
    return jsonify({"error": "Invalid temperature. It must be between 10 and 50"}), 400

def api_status():
    return {
        "device": SerialConnection.connection.port if SerialConnection.connection_available else None,
        "operation_mode": SerialConnection.mode,
        "target_temperature": SerialConnection.target_temperature,
        "last_measurement": SerialConnection.last_measurement,
        "time_since_last_measurement": time.monotonic() - SerialConnection.last_measurement_timestamp if not SerialConnection.last_measurement_timestamp == None else None,
        "status_codes": SerialConnection.device_status_codes,
        "status_descriptions": SerialConnection.device_status_descriptions
    }

def no_connection():
    return jsonify({"error": "You must stablish a connection with the device first."}), 400

def connection_already_exists():
    return jsonify({"error": "You are trying to stablish a conection, but one already exists"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
