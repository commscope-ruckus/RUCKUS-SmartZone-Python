import paho.mqtt.client as mqtt #import the mqtt library
import sci_message_pb2 #import all SZ .proto classes compiled by the protoc tool

#read incoming messages
def on_message(client, userdata, message):
    scim = sci_message_pb2.SciMessage().FromString(message.payload)
#    print(scim)
    print(scim.apClient)
    print(scim.apClient.ap)    
    print(scim.apClient.clients[0].clientMac)
#    print(scim.apReport)
#    print(scim.apWiredClient)
#    print(scim.apStatus)
#    print(scim.switchDetailMessage)
#    print(scim.switchConfigurationMessage)
#    print(scim.apRogue)


#log function
def on_log(client, userdata, level, buf):
    print("log: ",buf)

broker_address="localhost"

client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to message callback
#client.on_log=on_log

print("connecting to mosquitto broker")
client.connect(broker_address) #connect to mosquitto broker

print("Subscribing to sci-topic")
client.subscribe("sci-topic")

client.loop_forever() #starts a thread on the mqtt client which reads the message buffers

