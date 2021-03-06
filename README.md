![Bluemix](https://raw.githubusercontent.com/hunglkuit/BlueMix-Tutorial/master/python-client-connect2iot-service/IBM-Bluemix.jpg)
=======
[IBM® Bluemix™](https://www.ng.bluemix.net) is the IBM open cloud platform that provides mobile and web developers access to IBM software for integration, security, transaction, and other key functions, as well as software from business partners.

This repository is used to share my experiences while working on Bluemix platform. Most of my applications were writen in NodeJS and Python.

* [Python Application used to connect to IBM IoT service.] (#ibmiot-client)

<a name='ibmiot-client'></a>
## Python Applocation connect to IBM IoT service.

This application is implemented on IBMIOT library. We can download and install this library by using command `pip install ibmiotf`. 
The constructor builds the IBMIoT client instance received an options dict containing the following definitions:
* org - Your organization ID.
* type - The type of your device.
* id - The ID of your device.
* auth-method - Method of authentication (the only value currently supported is “token”).
* auth-token - API key token (required if auth-method is “token”).

After success creation, we connect to IBM IoT by using 'connect()' method and publish data via 'publishEvent()'. 
Example Code: 
```
deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
deviceCli = ibmiotf.device.Client(deviceOptions)
myData = { 'hello' : 'world', 'x' : x}
deviceCli.publishEvent(event="greeting", msgFormat="json", data=myData)
```

