# config.py - Configuration du système IoT

# CONFIGURATION WIFI (Ne fonctionne pas si la box detecte trop de connexions/déconnexions)

# WIFI:
SSID1= "MON_REASEAU1"
MDP1= "MON_MDP1"

# Partage de connexion:
# SSID2= "MON_RESEAU2"
# MDP2= "MON_MDP2"

# CONFIGURATION MQTT

BROKER_IP1= "192.168.1.XX" # IP locale de ton PC
BROKER_IP2= "172.20.10.XX" # IP en partage de connexion
CLIENT_ID= "esp32_victor"
TOPIC = "capteur/test"
