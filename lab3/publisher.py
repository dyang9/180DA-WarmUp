import paho.mqtt.client as mqtt

# initialize a cliend
client = mqtt.Client()

# connect to broker
client.connect("test.mosquitto.org")

# publish a message
client.publish("ece180d/test", payload="HELLO WORLD!", qos=1)
client.disconnect()