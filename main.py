import paho.mqtt.client as mqtt
import json

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost",1883)
client.loop_start()


def on_message(client, userdata, msg):
    print(f"Got a message on {msg.topic}")
    print(f"Content: {msg.payload.decode()}")


#JSON message
message = {
    "id": "HYDROLOGICAL-01",
    "pressure": 72,
    "flow_rate": 41.2
}

client.publish("hydroficient/grandmarina/sensors/main-building", json.dumps(message))
print("Message sent!")

