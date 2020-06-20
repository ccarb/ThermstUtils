# PARA INICIAR EL SERVER:
# .\flask_env\Scripts\Activate.ps1
# $env:FLASK_APP = "flask_server.py"
# $env:FLASK_ENV = "development"
# python -m flask run
from flask import Flask
from flask import request
from flask import jsonify
from server.popos import connection as Connection
from server.popos import fake_measurements as FakeMeasurements
import os
app = Flask(__name__)
SerialConnection = Connection.Connection()
FakeMeasurements = FakeMeasurements.FakeMeasurements()

    
@app.route('/')
def status():
    return 'La aplicación esta funcionando'

@app.route('/connect', methods=['GET', 'POST', 'DELETE'])

@app.route('/list_devices', methods=['GET'])
def list_devices():
    data = SerialConnection.list_devices()
    print(data)
    return jsonify(data)

@app.route('/open_connection', methods=['POST'])
def open_connection():
    device = request.json["device"]
    status = SerialConnection.connect_device(9600, device)
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

@app.route('/temperature', methods=['GET'])
def get_temperature():
    response = SerialConnection.request_temperature_measure()
    return jsonify(response), 200

@app.route('/temperature_test', methods=['POST'])
def set_temperature_test():
    FakeMeasurements.set_objective(request.json["temperature"])
    return '', 202

@app.route('/temperature_test', methods=['GET'])
def get_temperature_test():
    return { "temperature": str(FakeMeasurements.read_temperature()) }, 200


@app.route('/ping', methods=['GET'])
def ping():
    response = SerialConnection.ping()
    return jsonify(response), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)