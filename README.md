# IoT MQTT Data Pipeline

<p>A complete end-to-end IoT data pipeline built with Python. This project simulates a real-world IoT environment where a mock sensor device generates data, transmits it via the MQTT protocol using the Paho-MQTT library, and visualizes it on a live dashboard </strong>.</p>

## Architecture Overview

### Publisher (`sensor_gen.py`)
Simulates an IoT edge device. It generates telemetry data (temperature and humidity) and publishes JSON payloads to an MQTT broker.

### Broker
Acts as the central message hub, routing messages between publishers and subscribers based on topics.

### Subscriber (`dashboard.py`)
Ingests live data streams from the broker and renders the data in a real-time visualization dashboard.

### Certificate Generator (`generate_certs.py`)
Generates X509 Certifcate to authenticate a party’s identity in a SSL/TLS connection.

---

## Technical Stack

- **Language:** Python 3.x  
- **Protocol:** MQTT (Message Queuing Telemetry Transport)  
- **Key Library:** `paho-mqtt`  
- **Data Format:** JSON
