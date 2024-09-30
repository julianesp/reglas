# explicacion de algnas rutas:
# desde A a B: toma 10 minutos el recorrido.
# desde A a C: toma 15 minutos el recorrido.

#definicion de rutsa.
rutas = {
    "A": [("B", 10), ("C", 15)],
    "B": [("D", 12), ("E", 15)],
    "C": [("F", 10)],
    "D": [("E", 2), ("F", 1)],
    "E": [("G", 5)],
    "F": [("G", 2)],
    "G": []  # G es el destino final
}

#mostrar tiempo que tarda en ir de una ruta a otra, por ejemplo, desde A a B
# Función para mostrar los tiempos de viaje
def mostrar_tiempos(rutas):
    for origen, destinos in rutas.items():
        for destino, tiempo in destinos:
            print(f"El tiempo de {origen} a {destino} es {tiempo} minutos.")

# Llamamos a la función para mostrar los tiempos de cada ruta
mostrar_tiempos(rutas)


def encontrar_ruta_mas_rapida(rutas, inicio, destino):
    # aqui se guarda la mejor ruta y el tiempo mínimo hacia cada estacion
    tiempo_minimo = {estacion: float('inf') for estacion in rutas}
    tiempo_minimo[inicio] = 0  # El tiempo al punto de inicio es 0

    # aohra creo un diccionario para guardar cómo llegamos a cada estación (para reconstruir la ruta)
    ruta_previa = {}

    # Lista de estaciones por visitar
    estaciones_por_visitar = [inicio]

    # Empezamos la búsqueda
    while estaciones_por_visitar:
        estacion_actual = estaciones_por_visitar.pop(0)

        # Revisamos todas las rutas desde la estación actual
        for destino_ruta, tiempo_viaje in rutas[estacion_actual]:
            tiempo_total = tiempo_minimo[estacion_actual] + tiempo_viaje

            # Si encontramos una ruta más rápida hacia el destino
            if tiempo_total < tiempo_minimo[destino_ruta]:
                tiempo_minimo[destino_ruta] = tiempo_total
                ruta_previa[destino_ruta] = estacion_actual
                estaciones_por_visitar.append(destino_ruta)

    # Reconstruimos la ruta más rápida desde el inicio hasta el destino
    ruta_optima = []
    estacion = destino
    while estacion in ruta_previa:
        ruta_optima.append(estacion)
        estacion = ruta_previa[estacion]
    ruta_optima.append(inicio)
    ruta_optima.reverse()

    # Devolvemos la mejor ruta y el tiempo total
    return ruta_optima, tiempo_minimo[destino]

# Usamos la función para encontrar la ruta más rápida de A a G
inicio = "A"
destino = "G"
ruta, tiempo_total = encontrar_ruta_mas_rapida(rutas, inicio, destino)

# Mostrar el resultado
print(f"La ruta mas rapida de {inicio} a {destino} es: {' -> '.join(ruta)}")
print(f"El tiempo total es: {tiempo_total} minutos.")
