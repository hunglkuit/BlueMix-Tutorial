#Settings for the mqtt client
mqttSettings = dict(
    #Change this to something that identifies your Client
    org         = "4vauhm",
    device_type = "MQTTDevice",
    clientID    = 'aabbccddeeff1122',
    auth_method = 'token',
    auth_token  = "i9K7Fs7+3!qsNz*)*)",
    auth_app_token = "iCHBUe5WSyhRtB!W9?",

    #Don't change this
    server      = 'realtime.ngi.ibm.com',
    port        = 1883,
    publishTopic    = '/org/dutchcourage/poseidon/client/sensor',
)

# Location information for the GrovePi station
# Change these values!
location = dict(
    latitude         = 0,
    longitude        = 0,
)

# Interval in which values should be stored or send
# Don't set this under 30
updateInterval = 60
