import requests

from config import *

serverUrl="http://127.0.0.1:5000/"

def getDevices():
    r=requests.get( serverUrl + "list_devices")
    return r.json()

def openDevice(device : dict):
    requests.post( serverUrl + "open_connection", json=device)

def closeDevice(device: dict):
    requests.delete( serverUrl + "close_connection", json=device)

def startDevice(settings: dict): # TODO: name is missleading.
    requests.post( serverUrl + "set_temperature", json=settings)

def cold(settings: dict):
    requests.post( serverUrl + "cold", json=settings)

def hot(settings: dict):
    requests.post( serverUrl + "hot", json=settings)

def stopTemp():
    requests.post( serverUrl + "stop_device")

def readTemperature():
    r=requests.get( serverUrl + "read_temperature?consumer=UI")
    if not r.status_code == 200: return {"error": "ServerError"}
    r=r.json()
    return r

def shutdownServer():
    requests.get(serverUrl + "shutdown")

def apiStatus():
    r = requests.get(serverUrl)
    if not r.status_code == 200: return {"error": "ServerError"}
    return r.json()
