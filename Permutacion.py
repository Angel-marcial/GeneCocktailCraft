
def emparejamientoParcial(padre1, padre2, corte1, corte2):
    size = len(padre1)
    hijo = [None] * size

    hijo[corte1:corte2+1] = padre1[corte1:corte2+1]

    print("cortes: ",hijo)

    for i in range(corte1, corte2+1):
        if padre2[i] not in hijo:
            index = padre2.index(padre1[i])
            while hijo[index] is not None:
                index = padre2.index(padre1[index])
            hijo[index] = padre2[i]

    for i in range(size):
        if hijo[i] is None:
            hijo[i] = padre2[i]


    print("hijoPermutado",hijo)
    return hijo





