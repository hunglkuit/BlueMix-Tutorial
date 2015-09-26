# DEMO USING IBM IOT SERVICE

### 1. Introduction:

This application include 2 sides:
- Client Side is a python application which have responsibility sending MQTT message to IBM broker.
- Server Side is a Node-Red application contains 1 MQTT subscriber and cloudant database.

Client code is stored in client directory. 

### 2. Operation:

Client will register device with IBM IOT service and use client application to send message to broker. MQTT subcriber will subcribe this broker and save all messages to cloudant database