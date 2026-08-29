# wifi.py : Gère la connexion au réseau


import machine, network, time
import config

# Test WIFI

def do_connect():
    wlan = network.WLAN(network.STA_IF) # Transforme ESP32 en client de la box internet (pour pouvoir se connecter)

    wlan.active(False)  # Éteint le Wi-Fi pour réinitialiser le pilote
    time.sleep(0.5)
    wlan.active(True)   # Rallume proprement
    
    wlan.config(pm=network.WLAN.PM_NONE) # Force le module WIFI a être réveillé
    
    print('connecting to network...')
    wlan.connect(config.SSID1, config.MDP1)

    # AJOUT TIMEOUT WIFI
    timeout = 15 

    while not wlan.isconnected() and timeout >0:
        print(f"Attente Wi-Fi... {timeout}s restantes")
        time.sleep(1)
        timeout-=1
    
    if wlan.isconnected():
        print('network config:', wlan.ifconfig())
        return True
    else:
        print(" Erreur: Imposible de se connexter au wifi (Timeout)")
        return False

