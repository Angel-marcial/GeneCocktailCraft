import random

def combinacionUniforme(padre1, padre2, probabilidad_cruza):
    # Verificar si se realiza la cruza según la probabilidad
    if random.uniform(0, 1) < probabilidad_cruza:
        # Inicializar el hijo con la misma longitud que los padres
        hijo = [None] * len(padre1)

        # Llenar el hijo alternando elementos de los padres
        for i in range(len(padre1)):
            if random.choice([True, False]):  # Alternar aleatoriamente entre padres
                hijo[i] = padre1[i]
            else:
                hijo[i] = padre2[i]

        return hijo
    else:
        # Si no se realiza la cruza, devolver uno de los padres aleatoriamente
        return random.choice([padre1, padre2])










