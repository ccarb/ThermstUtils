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
    return 'La aplicación esta funcionando'

@app.route('/list_devices', methods=['GET'])
def list_devices():
    data = SerialConnection.list_devices()
    print(data)
    return jsonify(data)

@app.route('/open_connection', methods=['POST'])
def open_connection():
    device = request.json["device"]
    app.logger.info("Device::::::::::::::::::::::::::::" + device)
    status = SerialConnection.connect_device(device)
    if status == 200: 
        message_response = "Device connected"
    else:
        message_response = "Could not find an device - is it plugged in?"
    return jsonify(message = message_response), status

@app.route('/close_connection', methods=['DELETE'])
def close_connection():
    device = request.json["device"]
    response = SerialConnection.disconnect_device(device)
    if "error" in response:
        status = 400
    else:
        status = 202
    return jsonify(response), status

@app.route('/read_temperature', methods=['GET'])
def get_temperature():
    temperature = SerialConnection.read_temperature()
    response = { "temperature": str(temperature) }
    return jsonify(response), 200

@app.route('/set_temperature', methods=['POST'])
def set_temperature():
    response = SerialConnection.set_objective_temperature(request.json["objective_temperature"])
    return '', 202

@app.route('/ping', methods=['GET'])
def ping():
    response = SerialConnection.ping()
    return jsonify(response), 200

def readTemp():
    return str(datetime.datetime.now())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
