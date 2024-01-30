import random

def seleccion_por_ruleta(poblacion, calificaciones):

    if len(poblacion) != len(calificaciones):
        raise ValueError("La longitud de la población y las calificaciones debe ser la misma.")

    calificaciones_invertidas = [1 / calificacion for calificacion in calificaciones]

    #print(calificaciones_invertidas)

    suma_calificaciones_invertidas = sum(calificaciones_invertidas)
    
    #print(suma_calificaciones_invertidas)

    probabilidades = [calificacion_inv / suma_calificaciones_invertidas for calificacion_inv in calificaciones_invertidas]

    #print(probabilidades)

    punto_seleccion = random.uniform(0, 1)

    acumulado_probabilidades = 0

    seleccionado = None

    for i, probabilidad in enumerate(probabilidades):
        acumulado_probabilidades += probabilidad
        if punto_seleccion <= acumulado_probabilidades:
            seleccionado = poblacion[i]
            break

    return seleccionado


def padre1(padre1,totalrecetas,Recetas):

    if padre1 == totalrecetas[0]:
        padre1 = Recetas[0]
    if padre1 == totalrecetas[1]:
        padre1 = Recetas[1]        
    if padre1 == totalrecetas[2]:
        padre1 = Recetas[2]
    if padre1 == totalrecetas[3]:
        padre1 = Recetas[3]

    return padre1

def padre2(padre2,totalrecetas,Recetas):

    if padre2 == totalrecetas[0]:
        padre2 = Recetas[0]
    if padre2 == totalrecetas[1]:
        padre2 = Recetas[1]        
    if padre2 == totalrecetas[2]:
        padre2 = Recetas[2]
    if padre2 == totalrecetas[3]:
        padre2 = Recetas[3]

    return padre2

def cantidad1(padre1,totalrecetas,Cantidades):

    if padre1 == totalrecetas[0]:
        cantidad1 = Cantidades[0]
    if padre1 == totalrecetas[1]:
        cantidad1 = Cantidades[1]       
    if padre1 == totalrecetas[2]:
        cantidad1 = Cantidades[2]
    if padre1 == totalrecetas[3]:
        cantidad1 = Cantidades[3]

    return cantidad1

def cantidad2(padre2,totalrecetas,Cantidades):

    if padre2 == totalrecetas[0]:
        cantidad2 = Cantidades[0]
    if padre2 == totalrecetas[1]:
        cantidad2 = Cantidades[1]       
    if padre2 == totalrecetas[2]:
        cantidad2 = Cantidades[2]
    if padre2 == totalrecetas[3]:
        cantidad2 = Cantidades[3]

    return cantidad2