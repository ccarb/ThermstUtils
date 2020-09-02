import os

try:
    if os.environ["deviceIndependant"]=="True":
        deviceIndependant=True
    else:
        deviceIndependant=False
except:
    deviceIndependant=False
