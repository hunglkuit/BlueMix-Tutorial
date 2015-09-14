[IBM® Bluemix™](https://www.ng.bluemix.net) is the IBM open cloud platform that provides mobile and web developers access to IBM software for integration, security, transaction, and other key functions, as well as software from business partners.

This repository is used to share my experiences while working on Bluemix platform. Most of my applications were writen in NodeJS and Python.

* [Python Application used to connect to IBM IoT service] (#ibmiot-client)
<a name='ibmiot-client'>
## Python Applocation connect to IBM IoT service.

This application is implemented on IBMIOT library. We can download and install this library by using command `pip install ibmiotf`. 
The constructor builds the IBMIoT client instance received an options dict containing the following definitions:
** org - Your organization ID.
** type - The type of your device.
** id - The ID of your device.
** auth-method - Method of authentication (the only value currently supported is “token”).
auth-token - API key token (required if auth-method is “token”).

