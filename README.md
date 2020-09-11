# ThermstUtils
User interface for thermal stimulator configuration and maintenance

## Setup

```
python3 -m venv env/
source env/bin/activate
pip3 install -r requirements.txt

```

## Running the app

Activate the env:
```
source env/bin/activate
```
Run the main:
```
python3 main.py
```

- Optional env variables:

Powershell:
``` powershell
$env:EnableLogging = "True"
$env:deviceIndependant = True
```
Windows Console:
```
set EnableLogging="True"
set deviceIndependant=True
```
Linux Console:
```
$EnableLogging="True"
$deviceIndependant=True
```
## Permisions to connect to arduino

sudo chmod 666 /dev/ttyUSB0
