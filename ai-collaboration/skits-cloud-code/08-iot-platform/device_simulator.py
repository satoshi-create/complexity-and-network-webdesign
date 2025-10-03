import json, time, random
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('iot-endpoint.amazonaws.com', 8883, 60)

while True:
    payload = {"temp": random.uniform(20,30)}
    client.publish('iot/topic', json.dumps(payload))
    print('Sent:', payload)
    time.sleep(5)
