import requests

from config import *

serverUrl="http://127.0.0.1:5000/"

def getDevices():
    if deviceIndependant:
        return [{"port":"Dummy Device"}]
    else:
        r=requests.get( serverUrl + "list_devices")
        return r.json()

def openDevice(device : dict):
    if deviceIndependant:
        # there is no device to open
        pass
    else:
        requests.post( serverUrl + "open_connection", json=device)

def closeDevice(device: dict):
    if deviceIndependant:
        # there is no device to close
        pass
    else:
        requests.post( serverUrl + "close_connection", json=device)

def startDevice(settings: dict):
    if deviceIndependant:
        requests.post( serverUrl + "temperature_test", json=settings)
    else:
        # to do: make request sending settings
        pass

def readTemperature():
    if deviceIndependant:
        r=requests.get( serverUrl + "temperature_test")
        r=r.json()
        return str(r["temperature"])
    else:
        # to do: make data request
        return "-1000"

def shutdownServer():
    requests.get(serverUrl + "shutdown")