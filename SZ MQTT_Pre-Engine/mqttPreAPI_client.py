import paho.mqtt.client as mqtt #import the mqtt library
from datetime import datetime
import struct

#read incoming messages
def on_message(client, userdata, message):
    if message.topic.endswith("MGR") and message.payload[0] == 2 and message.payload[1] == 1: #detect MGR starting with bytes 02 01
        print ("Controller Name:", message.payload[4:68].decode()) 
        print("API version:", message.payload[68:84].decode())
        print("Controller Software version:", message.payload[84:100].decode())
    if message.topic.endswith("MGR") and message.payload[0] == 2 and message.payload[1] == 7: #detect MGR starting with bytes 02 07
        numVenues = int.from_bytes(message.payload[4:6], byteorder='big')
        print ("Number of venues:", numVenues)
        for i in range (0, numVenues):
            print("Venue name:", message.payload[6+(16*i):22+(16*i)].decode()) # the venues show every 16 bytes
    if message.topic.endswith("PAR") and message.payload[0] == 4 and message.payload[1] == 3: #detect PAR starting with bytes 04 03
        print ("Timestamp:", datetime.fromtimestamp(int.from_bytes(message.payload[4:8], byteorder='big')))
        print ("Sequence number:", int.from_bytes(message.payload[8:12], byteorder='big'))
        print ("AP mac address:", prettify(message.payload[12:18].hex()))
        bandbyte = message.payload[18]
        if bandbyte == 1:
            band = "2.4GHz"
        else:
            band = "5GHz"
        print ("Band:", band)
        print ("Air Time utilization:", message.payload[19], "%")
        numClients = int.from_bytes(message.payload[20:22], byteorder='big')
        print ("Number of clients:", numClients)
        for j in range (0, numClients):
            print("Client mac address:", prettify(message.payload[22+(11*j):28+(11*j)].hex())) # the client mac shows every 11 bytes
            print("Phy info:", message.payload[28+(11*j)]) # this field is not currently used
            print("RSSI-1:", message.payload[29+(11*j)]-256, "dBm")
            print("RSSI-2:", message.payload[30+(11*j)]-256, "dBm")
            print("RSSI-3:", message.payload[31+(11*j)]-256, "dBm")
            print("SNR:", message.payload[32+(11*j)]-256, "dBm")

#add ":"s to mac address
def prettify(mac_string):
    return ':'.join(mac_string[i:i+2] for i in range(0,12,2))

#use "localhost" if this client and the mosquitto broker are running in the same computer
#otherwise use the URL or IP address of the computer where the mosquitto broker is running
#this client assumes the mosquitto broker is listening at port 1883 without security enabled
broker_address="localhost" 
client = mqtt.Client("preAPIclient") #create new instance
client.on_message=on_message #attach message function to client
print("connecting to broker")
client.connect(broker_address)
client.subscribe("#") #subscribe to all topics

payload = struct.pack('bb', 1,1) #get controller information
client.publish("3.0/LOC/lbstest/LS/MGQ",payload, 2)

payload = struct.pack('bb', 1,7) #get venues
client.publish("3.0/LOC/lbstest/LS/MGQ",payload, 2)

payload = struct.pack('bbbbbbbbbbb',3,1,0,7,10,0,10,1,0,0,0) #sent PAQ request for 2.4 GHz radio
client.publish("3.0/LOC/lbstest/LS/PAQ",payload, 2)

payload = struct.pack('bbbbbbbbbbb',3,1,0,7,10,0,10,2,0,0,0) #sent PAQ request for 5 GHz radio
client.publish("3.0/LOC/lbstest/LS/PAQ",payload, 2)

client.loop_forever() #starts a thread on the mqtt client which reads the message buffers forever
