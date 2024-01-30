def ajustar_valores(valores, total_deseado, total_actual):
    if not isinstance(valores, list):
        raise TypeError("El argumento 'valores' debe ser una lista.")

    suma_valores = sum(valores)
    valores_normalizados = [valor / suma_valores for valor in valores]
    valores_ajustados = [round(valor * total_deseado, 2) for valor in valores_normalizados]

    valores_normalizados_actual = [valor / suma_valores for valor in valores]
    valores_ajustados_actual = [round(valor * total_actual, 2) for valor in valores_normalizados_actual]

    return valores_ajustados