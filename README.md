## Recuperatorio-smn
<img width="1000" height="130" alt="WhatsApp Image 2026-11-18 at 02 21 17" src="https://github.com/user-attachments/assets/d3306c27-47ff-4349-be34-63297930384a" />

# Descripcion
Este es un programa de línea de comandos que lee las observaciones de un día de las estaciones del Servicio Meteorológico Nacional. 
Cada observación se representa con un objeto de tipo Observacion y resume las temperaturas de una estación.

# Elementos 
En observacion.py se crea la clase Observacion con los metodos:
- verificar_estacion(): compara la estacion con el nombre que pida el usuario
- intensidad_viento(): devuelve la intensidad del viento segun su velocidad

            | Intensidad | Velocidad |
            |---|---|
            | `calma` | menor a 2 km/h |
            | `leve` | desde 2 y menor a 20 km/h |
            | `moderado` | desde 20 y menor a 40 km/h |
            | `fuerte` | 40 km/h o más |

- mensaje(): regresa un mensaje con el formato solicitado por el profesor

En consultar_clima.py se definen las funciones:
- leer_json(): recibe la ruta del archivo JSON, carga los datos y devuelve una lista de objetos Observacion. si un registro no cumple las validaciones de la clase, se descarta y el programa sigue con el siguiente.
- filtrar_por_estacion(): devuelva sólo las observaciones de una estación
- calcular_datos(): calcula y devuelve un diccionario con la cantidad de observaciones, la observación con la temperatura mínima, la observación con la temperatura máxima y el promedio de temperatura

Main.py: codigo principal proporcionado por el profesor, se completa utilizando las funciones creadas en consultar_clima.py

## Como utilizar el programa


<img width="600" height="323" alt="WhatsApp Image 2026-11-17 at 18 29 32" src="https://github.com/user-attachments/assets/37638f8b-4241-4b73-b1a5-14141aa190f8" />



