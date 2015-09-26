import ibmiotf.device
import ibmiotf.application
import config
import time
import customData


def myAppEventCallback(event):
    print("Received live data from %s (%s) sent at %s: hello=%s x=%s" % (event.deviceId, event.deviceType, event.timestamp.strftime("%H:%M:%S"), data['hello'], data['x']))

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print "Connection failed. RC: {}".format(rc)
    else:
        print "Connected successfully"

def on_publish(client, userdata, mid):
    print "Message {} published.".format(mid)

def on_disconnect(client, userdata, rc):
	print "Disconnected"

# Encode data following custom format.


# Server configure.
options = {
    "org": config.mqttSettings['org'],
    "type": config.mqttSettings['device_type'],
    "id": config.mqttSettings['clientID'],
    "auth-method": config.mqttSettings['auth_method'],
    "auth-token": config.mqttSettings['auth_token']}

app_options = {
    "org": config.mqttSettings['org'],
    "type": config.mqttSettings['device_type'],
    "id": config.mqttSettings['clientID'],
    "authMethod": config.mqttSettings['auth_method'],
    "auth-token": config.mqttSettings['auth_app_token']}



# Setup application to subcribe data send to server

# mqtt_client = ibmiotf.application.Client(app_options)
# mqtt_client.connect()
# mqtt_client.on_connect = on_connect
# mqtt_client.subscribeToDeviceEvents(config.mqttSettings['device_type'],config.mqttSettings['clientID'],"greeting")
# mqtt_client.deviceEventCallback = myAppEventCallback

# setup device send event to server

mqtt_device = ibmiotf.device.Client(options)
mqtt_device.setMessageEncoderModule("custom",customData)
mqtt_device.connect()

for x in range (0,200):
    data = { 'hello' : 'world', 'x' : x}
    print "send data" + str(x) + "th"
    mqtt_device.publishEvent("greeting", "json", data)
    time.sleep(1)



# Disconnect after finish work
print "---- Disconnect after finish work ----"
mqtt_device.disconnect()
#mqtt_client.disconnect()


