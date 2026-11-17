from observacion import Observacion
from consultar_clima import leer_json, calcular_datos

# AEROPARQUE AERO | 1 h | 8.6 °C | 66 % | 11 km/h (leve)
# AEROPARQUE AERO | 2 h | 8.0 °C | 69 % | 13 km/h (leve)


lista = [Observacion("AEROPARQUE AERO", 0, 8, 70, 13), Observacion("AEROPARQUE AERO", 1, 8.6, 66, 11)]
diccionario = calcular_datos(lista)

for dato, item in diccionario.items():
    print(f"{dato}: {item}")