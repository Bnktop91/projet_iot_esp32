# mqtt.py : Service de messagerie MQTT

import json
from umqtt.simple import MQTTClient
import config

client = None # variable global

def connect(): # CONNEXION
    global client # précise qu'on modifie la variable global
    print("Connexion au broker Mosquitto...")
    client= MQTTClient(config.CLIENT_ID, config.BROKER_IP1, keepalive=60) # Objet client (garde processus en vie 60s)
    client.connect() # Ouvre canal TCP vers conteneur
    print("Connecté !")

def send_data(T, H): # ENVOI MQTT
    global client

    donnees={
        "temperature": T,
        "humidite": H
    }

    # Dictionnaire Python -> Conversion JSON -> Encodage UTF-8 (octets)
    payload= json.dumps(donnees).encode('utf-8')

    client.publish(config.TOPIC, payload)
    print(f"Messsage JSON envoyé sur le '{config.TOPIC}': {payload}")

def disconnect():
    global client

    if client:
        try:
            client.disconnect()
            print("Déconnecté de Mosquitto pour ne pas bloquer la ligne.")
        except Exception as e:
            pass # Ne fait rien

        client= None