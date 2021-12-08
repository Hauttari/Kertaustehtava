import json
import requests
import paho.mqtt.client as mqtt
import time
use_mqtt=True

if use_mqtt:
    broker_address="broker.hivemq.com"
    client = mqtt.Client("oMATUNNUS") # luo uusi asiakas 

    client.connect(broker_address) # avaa yhteys brokerille 

#luetaan tiedosto
file = open("mobiledata.txt","r")

for line in file:
    s=json.loads(line)
    if s['channel']=='solution':
        pos=s['position_lcl']

        positiondata={}
        positiondata['time']=s['time']
        positiondata['x']=pos[0]
        positiondata['y']=pos[1]
        positiondata['z']=pos[2]

        #muunnos json
        jsonm=json.dumps(positiondata, indent=True)
        print(jsonm)
        #lähetetään HTTP:lla
        if True:   #omalle palvelinohjelmalle tai thingspeakiin

            response=requests.post('http://localhost:5000/newmeasurement/', data=jsonm)
            print(response)

        if use_mqtt:
            client.publish("my_topicTH", jsonm)
        time.sleep(1)







