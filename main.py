import sys
from consultar_clima import leer_json, filtrar_por_estacion, calcular_datos
from observacion import Observacion
#python main.py observaciones.json "AEROPARQUE AERO" 

def main():
    ruta = sys.argv[1]
    estacion = sys.argv[2]

    # Función de carga de observaciones.
    observaciones = leer_json(ruta)
    print(f"Observaciones válidas: {len(observaciones)}")
    print()

    # Función de filtrado por estación.
    lista_solicitados = filtrar_por_estacion(estacion, observaciones)

    # Función de resumen de temperaturas.
    resumen = calcular_datos(lista_solicitados)
    minima = resumen["minima"]
    maxima = resumen["maxima"]

    print(estacion)
    print(f"Observaciones: {resumen['cantidad']}")
    # REEMPLAZAME: temperatura y hora de la observación mínima y de la máxima.
    print(f"Temperatura mínima: {minima.temperatura} °C a las {minima.hora} h")
    print(f"Temperatura máxima: {maxima.temperatura} °C a las {maxima.hora} h")
    print(f"Temperatura promedio: {resumen['promedio']} °C")
    print()
    for observacion in lista_solicitados:
        # REEMPLAZAME: descripción de la observación.
        print(observacion.mensaje())


main()