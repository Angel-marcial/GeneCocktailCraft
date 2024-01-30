import random

def mutacionInversion(permutacion, probabilidad_mutacion):
    # Verificar si se realiza la mutación según la probabilidad
    if random.uniform(0, 1) < probabilidad_mutacion:
        # Seleccionar dos posiciones aleatorias diferentes en la permutación
        inicio = random.randint(0, len(permutacion) - 1)
        fin = random.randint(inicio, len(permutacion))

        # Invertir la subsecuencia seleccionada
        permutacion[inicio:fin] = reversed(permutacion[inicio:fin])

    return permutacion
