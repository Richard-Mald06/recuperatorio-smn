import json
from observacion import Observacion

def leer_json(ruta_json):
    lista_validos = []
    errores = 0
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        contenido = json.load(archivo)

    for registro in contenido:
        try:
            registro_valido = Observacion(
            estacion = registro["estacion"],
            hora = registro["hora"],
            temperatura = registro["temperatura"],
            humedad = registro["humedad"],
            velocidad_viento = registro["velocidad_viento"]
            )
        except ValueError:
            errores += 1
            continue
        lista_validos.append(registro_valido)
    print(f"se excluyeron {errores} registros que no son validos")
    return lista_validos

def filtrar_por_estacion(estacion_solicitada, lista_validos):
    estacion_solicitada = estacion_solicitada.upper().strip()
    lista_solicitados = []
    for dato in lista_validos:
        if dato.verificar_estacion(estacion_solicitada):
            lista_solicitados.append(dato)
    return lista_solicitados

def calcular_datos(lista_solicitados):
    diccionario = {}
    cantidad = len(lista_solicitados)
    sumador = 0
    minimo = lista_solicitados[0]
    maximo = lista_solicitados[0]
    for dato in lista_solicitados:
        if dato.temperatura<minimo.temperatura:
            minimo = dato
        if dato.temperatura>maximo.temperatura:
            maximo = dato
        sumador += dato.temperatura
    promedio = sumador/cantidad
    diccionario["cantidad"] = cantidad
    diccionario["maxima"] = maximo
    diccionario["minima"] = minimo
    diccionario["promedio"] = promedio
    return diccionario
