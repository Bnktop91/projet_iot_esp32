# Banc d'Essai IoT — Supervision de Température & Humidité

Système d'acquisition et de supervision IoT End-to-End.

## Stack Technique

- **Terrain (Microcontrôleur) :** ESP32 sous MicroPython (v1.28.0)
- **Capteur :** DHT11 (Température & Humidité sur GPIO 4)
- **Protocole & Métriques :** Wi-Fi, MQTT (payloads JSON sur le topic `capteur/test`)
- **Serveur & Gateway :** Linux Ubuntu, Docker, Mosquitto Broker, Node-RED (Flows + Dashboard)
- **DevOps & Outillage :** VS Code, `mpremote`, Git

## Architecture du Flux de Données

```text
[ ESP32 + DHT11 ] 
       │ (Wi-Fi / JSON)
       ▼
[ Broker Mosquitto (Docker) ] 
       │ (MQTT Subscriber)
       ▼
[ Node-RED (Docker) ] 
       │
       ▼
[ Dashboard IHM (Jauges/Graphiques) ]
```

## Structure du Code Embarqué (ESP32)

L'ESP32 embarque un code modulaire séparé en 5 fichiers :

- `config.py` : Identifiants réseau et adresses du Broker.
- `wifi.py` : Connexion et gestion de l'interface Wi-Fi.
- `mqtt.py` : Client MQTT (`umqtt.simple`) et gestion des tentatives de reconnexion.
- `boot.py` : Script de démarrage automatique qui initialise le Wi-Fi.
- `main.py` : Boucle principale d'acquisition du DHT11 et d'envoi des payloads JSON toutes les 600s.

## Déploiement et Démarrage

### 1. Ingestion du code sur l'ESP32
```bash
mpremote cp config.py :
mpremote cp wifi.py :
mpremote cp mqtt.py :
mpremote cp main.py :
mpremote cp boot.py :
```


### 2. Démarrage des services Docker

```bash
docker-compose up
```

### 3. Monitoring en direct

- **Console ESP32 :** `mpremote repl`
- **Souscription MQTT :** `mosquitto_sub -h <IP_BROKER> -t "capteur/test"`
- **Dashboard Node-RED :** `http://localhost:1880/dashboard`