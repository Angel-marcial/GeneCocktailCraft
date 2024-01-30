def calcular_aptitud(ingredientes_totales, cantidades_totales, numIngredientes,calificacionHumana):

    cantidades_seleccionadas = cantidades_totales[:numIngredientes]
    ingredientes_seleccionados = ingredientes_totales[:numIngredientes]

    receta = list(zip(ingredientes_seleccionados, cantidades_seleccionadas))

    ingredientes_utilizados = set(ingrediente for ingrediente, cantidad in receta)
    variabilidad_ingredientes = len(ingredientes_utilizados) / numIngredientes

    desviacion_cantidades = max(cantidades_seleccionadas) - min(cantidades_seleccionadas)
    equilibrio_cantidades = 1 - (desviacion_cantidades / max(cantidades_seleccionadas))

    diversidad_cantidades = len(set(cantidades_seleccionadas)) / numIngredientes

    peso_variabilidad = 0.1
    peso_equilibrio = 0.1
    peso_diversidad = 0.1

    aptitud = (peso_variabilidad * variabilidad_ingredientes +
               peso_equilibrio * equilibrio_cantidades +
               peso_diversidad * diversidad_cantidades)


    peso_calificacion_humana = 0.1

    aptitud_final = (aptitud + peso_calificacion_humana * calificacionHumana) / (1 + peso_calificacion_humana)

    return aptitud_final








