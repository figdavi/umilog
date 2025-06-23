# umilog
Local backend server setup for ESP8266 sensor logging. It's built with FastAPI and SQLite.

This project contains both the backend and the .ino file for the ESP8266.

## How it works

![](simple_diagram.png)

## Project structure
```tree
.
│   .gitignore
│   Dockerfile
│   poetry.lock
│   pyproject.toml
│   README.md
│
├── data/       # Sensor data
│
└── src/umilog/
    │   database.py     # SQLite setup and CRUD
    │   main.py         # FastAPI app and routes
    │   umilog.ino      # ESP8266 flashable code
    │   __init__.py


```
- Note: A file named `sensor.sqlite3` will be created automatically on first run to store sensor data inside `data/` folder.


## Run locally

### Requirements

- Docker ([Download Page](https://docs.docker.com/get-docker/))
- Arduino IDE (for uploading the `.ino` file) ([Download Page](https://www.arduino.cc/en/software/))

### FastAPI Container

1. Clone the repository
```bash
git clone https://github.com/figdavi/umilog.git
cd umilog
```

2. Build and run docker compose
```bash
docker compose up --build
```

### Microcontroller (ESP8266)

#### Arduino Library Requirements

All libraries are already part of the core package for the ESP8266 board. 

On the Arduino IDE:

1. Go to `Tools` > `Board` > `Boards Manager`

2. Search for ESP8266 and install the `ESP8266 by ESP8266 Community` package

#### Flashing the Microcontroller

1. Open the `.ino` file (in `src/umilog/umilog.ino`) in the Arduino IDE.
2. Set the correct board and port (e.g., NodeMCU 1.0).
3. Replace the placeholder Wi-Fi credentials and host-ip in the sketch. 
4. Remove the `#include "secrets.h"` line or create a secrets.h file with the credentials.
5. Upload the code to the ESP8266.