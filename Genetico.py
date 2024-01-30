import random
import matplotlib.pyplot as plt

import Permutacion 
import Ingredientes
import Combinacion
import Ruleta
import Funcion
import MutacionPer
import MutacionCom
import convercion


cortes = 22
militros = 1000
militrosprueba = 50
recetas = 4
cruza = 1

ingredientes = 5
generaciones = 4
hijos = 4  # solo números pares
mutacion = .3
Aptitud = [0] * 4

R1 = ['Q', 'T', 'C', 'B', 'P', 'U', 'V', 'E', 'K', 'D', 'M', 'S', 'H', 'L', 'G', 'O', 'I', 'N', 'F', 'A', 'R', 'J']
C1 = [10, 88, 11, 87, 4, 11, 78, 29, 35, 25, 35, 22, 100, 8, 10, 39, 113, 32, 9, 143, 12, 99]

totalrecetas = ['R1', 'R2', 'R3', 'R4']

calificaciones = [0] * recetas

mejor_fitness = []
promedio_fitness = []
peor_fitness = []

mejor_individuo_generacion = []
peor_individuo_generacion = []



def generarRecetasAleatorias(receta, recetas):
    poblacion = []

    for _ in range(recetas):
        receta_aleatoria = receta.copy()
        random.shuffle(receta_aleatoria)
        poblacion.append(receta_aleatoria)

    return poblacion

def generarCantidadesAleatorias(cantidad, recetas):
    poblacion = []

    for _ in range(recetas):
        cantidad_aleatoria = cantidad.copy()
        random.shuffle(cantidad_aleatoria)
        poblacion.append(cantidad_aleatoria)

    return poblacion

# Genera la población inicial de recetas y cantidades
poblacionRecetas = generarRecetasAleatorias(R1, recetas)
poblacionCantidad = generarCantidadesAleatorias(C1, recetas)

for generacion in range(generaciones):
    print("\nGeneracion: ", generacion)

    for i in range(recetas):
        print(f"Receta {i}:", poblacionRecetas[i])
        print(f"Cantidad {i}:", poblacionCantidad[i])
        cantidadesAgustadas = convercion.ajustar_valores(poblacionCantidad[i],militrosprueba,militros)
        print(f"Cantidad {i}:",cantidadesAgustadas)

        cal1 = random.randint(1, 10)
        cal2 = random.randint(1, 10)
        cal3 = random.randint(1, 10)
        cal4 = random.randint(1, 10)

        calificacion = [cal1,cal2,cal3,cal4]
        #calificacion_str = input(f"Ingrese la calificación de la receta {i + 1}: ")
        #calificacion = float(calificacion_str)
        #calificaciones.append(calificacion)
        
    Aptitud = [0] * recetas

    for j in range(recetas):
        # Calcula la aptitud con las recetas generadas
        Aptitud[j] = Funcion.calcular_aptitud(poblacionRecetas[j], poblacionCantidad[j], ingredientes, calificacion[j])
        print(Aptitud[j])

    mejor_fitness.append(max(Aptitud))
    promedio_fitness.append(sum(Aptitud) / len(Aptitud))
    peor_fitness.append(min(Aptitud))




    if j == recetas - 1:
        # Selecciona los mejores padres   
        padre1 = Ruleta.seleccion_por_ruleta(totalrecetas, Aptitud)
        padre2 = Ruleta.seleccion_por_ruleta(totalrecetas, Aptitud)

        while padre2 == padre1:
            padre2 = Ruleta.seleccion_por_ruleta(totalrecetas, Aptitud)

        cantida1 = Ruleta.cantidad1(padre1, totalrecetas, poblacionCantidad)
        cantida2 = Ruleta.cantidad2(padre2, totalrecetas, poblacionCantidad)

        padre1 = Ruleta.padre1(padre1, totalrecetas, poblacionRecetas)
        padre2 = Ruleta.padre2(padre2, totalrecetas, poblacionRecetas)

        print("\npadre 1: ", padre1, "\nCantidad:", cantida1, "\npadre 2: ", padre2, "\nCantidad:", cantida2)

        # Genera 4 hijos nuevos
        poblacionRecetas = []
        poblacionCantidad = []
        for k in range(2):

            # Genera cortes aleatorios 
            corte1 = Ingredientes.corteAleatorio()
            corte2 = Ingredientes.corteAleatorio()
            # Permutacion 

            if corte1 < corte2:
                hijo1 = Permutacion.emparejamientoParcial(padre2, padre1, corte1, corte2)
                hijo2 = Permutacion.emparejamientoParcial(padre1, padre2, corte1, corte2)
            else:
                aux = corte1
                corte1 = corte2
                corte2 = aux
                hijo2 = Permutacion.emparejamientoParcial(padre1, padre2, corte1, corte2)
                hijo1 = Permutacion.emparejamientoParcial(padre2, padre1, corte1, corte2)

            hijoCantidad1 = Combinacion.combinacionUniforme(cantida1, cantida2, cruza)
            hijoCantidad2 = Combinacion.combinacionUniforme(cantida1, cantida2, cruza)

            print("Cantidad 1", hijoCantidad1, "\nCantidad 2", hijoCantidad2)

            mutado1 = MutacionPer.mutacionInsercion(hijo1, mutacion)
            mutado2 = MutacionPer.mutacionInsercion(hijo2, mutacion)

            print("hijo mutado1: ", mutado1, "\nhijo mutado2: ", mutado2)

            comMutada1 = MutacionCom.mutacionInversion(hijoCantidad1, mutacion)
            comMutada2 = MutacionCom.mutacionInversion(hijoCantidad2, mutacion)

            print("combinacion mutado1: ", comMutada1, "\ncombinacion mutado2: ", comMutada2)

            poblacionRecetas.append(mutado1)
            poblacionRecetas.append(mutado2)
            poblacionCantidad.append(comMutada1)
            poblacionCantidad.append(comMutada2)

        j = 0



print("\nMejor Fitness por Generación:", mejor_fitness)
print("Promedio Fitness por Generación:", promedio_fitness)
print("Peor Fitness por Generación:", peor_fitness)

generaciones = list(range(generaciones))
plt.plot(generaciones, mejor_fitness, label='Mejor Fitness', marker='o')
plt.plot(generaciones, peor_fitness, label='Mejor Fitness', marker='o')


plt.xlabel('Generación')
plt.ylabel('Aptitud')
plt.title('Gráfica de Aptitud por Generación')
plt.legend()
plt.show()