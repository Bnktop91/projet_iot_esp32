# main.py
# CF DOC https://docs.micropython.org/en/latest/esp32/quickref.html#lan

import machine, dht, time, network
import wifi, mqtt

# 1. Connexion Wi-Fi au lancement du script
wifi.do_connect()

# 2. Initialisation du capteur

capteur= dht.DHT11(machine.Pin(4))
wlan=network.WLAN(network.STA_IF)

# 3. Connexion à Mosquitto si WIFI actif

while True:
    # S'assurer que le WIFI est toujours là
    if not wlan.isconnected():
        print("Wi-Fi perdu, tentative de reconnexion...")
        wifi.do_connect()

    if wlan.isconnected():
        try:
            # Mesure
            capteur.measure()
            T = capteur.temperature()
            H = capteur.humidity()

            # Connexion, envoi, déconnexion propre
            mqtt.connect()
            mqtt.send_data(T, H)
            mqtt.disconnect()

        except Exception as e:
            print("Erreur mesure capteur:", e)
    else:
        print("Wi-Fi indisponible.")

    print("Attente de 10 minutes...")
    time.sleep(600)