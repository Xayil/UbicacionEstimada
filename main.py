# Base de datos de huellas digitales (solo un ejemplo)
fingerprint_database = {
    "Laboratorio de Aplicaciones": {"Wi-Fi_SSID_1": 0, "Wi-Fi_SSID_2": 0},
    "Cafetería": {"Wi-Fi_SSID_1": 0, "Wi-Fi_SSID_2": 40},
    "Edificio A": {"Wi-Fi_SSID_1": 60, "Wi-Fi_SSID_2": 40},
    "Starbucks": {"Wi-Fi_SSID_1": 62, "Wi-Fi_SSID_2": 40},
}

# Función para estimar la ubicación basada en señales Wi-Fi
def estimar_ubicacion(fingerprint, database):
    mejor_coincidencia = None
    mejor_diferencia = float('inf')

    for ubicacion, huella_digital in database.items():
        diferencia_total = 0

        for ssid, intensidad_rss in huella_digital.items():
            if ssid in fingerprint:
                diferencia = abs(fingerprint[ssid] - intensidad_rss)
                diferencia_total += diferencia

        if diferencia_total < mejor_diferencia:
            mejor_diferencia = diferencia_total
            mejor_coincidencia = ubicacion

    return mejor_coincidencia

# Simulación de una medición de señales Wi-Fi
fingerprint_actual = {"Wi-Fi_SSID_1": 11, "Wi-Fi_SSID_2": 40}

# Estimar la ubicación basada en la huella digital
ubicacion_estimada = estimar_ubicacion(fingerprint_actual, fingerprint_database)
print("Ubicación estimada:", ubicacion_estimada)
