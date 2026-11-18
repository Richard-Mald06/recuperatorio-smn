class Observacion:
    def __init__(self, estacion, hora, temperatura, humedad, velocidad_viento):

        if len(estacion) == 0:
            raise ValueError("La estación no puede estar vacía.")

        if not 0<=hora<=23:
            raise ValueError("La hora debe estar entre 0 y 23.")

        if temperatura is None or humedad is None or velocidad_viento is None:
            raise ValueError("La temperatura, la humedad o la velocidad del viento no pueden faltar.") 

        if temperatura < -30:
            raise ValueError("las temperaturas no deben ser menores a -30°")

        if not 0<=humedad<=100:
            raise ValueError("La humedad debe estar entre 0 y 100.")

        if velocidad_viento<0:
            raise ValueError ("La velocidad del viento no puede ser negativa.")

        self.estacion = estacion
        self.hora = hora
        self.temperatura = temperatura
        self.humedad = humedad
        self.velocidad_viento = velocidad_viento

    def verificar_estacion(self, nombre):
        if self.estacion == nombre:
            return True
        else:
            return False

    def intensidad_viento(self):
        if self.velocidad_viento < 2:
            return "calma"
        elif 2<=self.velocidad_viento<20:
            return "leve"
        elif 20<=self.velocidad_viento<40:
            return "moderado"
        else:
            return "fuerte"

    def mensaje(self):
        return f"{self.estacion} | {self.hora} h | {self.temperatura} °C | {self.humedad} % | {self.velocidad_viento} km/h ({self.intensidad_viento()})"

    def horas_heladas(self):
        if self.temperatura <= 0:
            return True
        return False