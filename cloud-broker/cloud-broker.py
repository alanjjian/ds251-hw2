import paho.mqtt.client as mqtt
import sys
import base64
import boto3
import numpy as np
import matplotlib.pyplot as plt

LOCAL_MQTT_HOST="localhost"
LOCAL_MQTT_INBOUND = 1884
LOCAL_MQTT_OUTBOUND = 1885
LOCAL_MQTT_TOPIC= "test_topic"
prefix = 'face-images'

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    print("message received: ",str(base64.b64decode(msg.payload)))
    # if we wanted to re-publish this message, something like this should work
    decoded_img = base64.b64.decode(msg.payload)
    img_arr = np.array(decoded_img)
    img = plt.imshow(decoded_img, interpolation='nearest')
    plt.savefig("img.png")
    filename = str(int(np.random.random() * 10000000000)) + ".png"
    boto3.Session().resource('s3').Bucket(bucket).Object(
            os.path.join(prefix, filename).upload_file("img.png"))   

    remote_mqttclient.publish(LOCAL_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except Exception as e:
    print(e)

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local

remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_local


try:
    local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_INBOUND, 60)
    print("connected!")
except:
    print("local client yikes!")
try:
    remote_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_OUTBOUND, 60)
except:
    print("remote client yikes!")

local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
