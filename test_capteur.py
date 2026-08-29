import machine, dht, time

capteur= dht.DHT11(machine.Pin(4)) # capteur sur broche 4 (GPIO 4)

try:
    print("Mesure en cours...")
    time.sleep(2)
    capteur.measure()

    temp= capteur.temperature()
    humid= capteur.humidity()

    print(f"Température: {temp}°C")
    print(f"Humidité: {humid}%")

except Exception as e: 
    print("Erreur de lecture du capteur :", e)