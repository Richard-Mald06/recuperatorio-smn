import sys
import consultar_clima

#python main.py observaciones.json "AEROPARQUE AERO" 

def main():
    ruta = sys.argv[1]
    estacion = sys.argv[2]

    # Función de carga de observaciones.
    print(f"Observaciones válidas: {len(observaciones)}")
    print()

    # Función de filtrado por estación.
    # Función de resumen de temperaturas.
    minima = resumen["minima"]
    maxima = resumen["maxima"]

    print(estacion)
    print(f"Observaciones: {resumen['cantidad']}")
    # REEMPLAZAME: temperatura y hora de la observación mínima y de la máxima.
    print(f"Temperatura mínima: {REEMPLAZAME} °C a las {REEMPLAZAME} h")
    print(f"Temperatura máxima: {REEMPLAZAME} °C a las {REEMPLAZAME} h")
    print(f"Temperatura promedio: {resumen['promedio']} °C")
    print()
    for observacion in de_la_estacion:
        # REEMPLAZAME: descripción de la observación.
        print(REEMPLAZAME)


main()