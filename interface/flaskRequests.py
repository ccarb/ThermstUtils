import requests

serverUrl="http://127.0.0.1:5000/"

def getDevices():
    r=requests.get( serverUrl + "list_devices")
    return r.json()

def openDevice(device : dict):
    requests.post( serverUrl + "open_connection", json=device)

def closeDevice(device: dict):
    requests.post( serverUrl + "close_connection", json=device)

def startDevice(settings: dict):
    requests.post( serverUrl + "temperature_test", json=settings)

def readTemperature():
    r=requests.get( serverUrl + "temperature_test")
    r=r.json()
    return str(r["temperature"])

def shutdownServer():
    requests.get(serverUrl + "shutdown")