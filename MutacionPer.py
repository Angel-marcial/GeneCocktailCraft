import random

def mutacionInsercion(permutacion, probabilidad_mutacion):

    if random.uniform(0, 1) < probabilidad_mutacion:

        posicion_origen = random.randint(0, len(permutacion) - 1)
        posicion_destino = random.randint(0, len(permutacion) - 1)


        while posicion_destino == posicion_origen:
            posicion_destino = random.randint(0, len(permutacion) - 1)

        elemento = permutacion.pop(posicion_origen)

        permutacion.insert(posicion_destino, elemento)

    return permutacion

