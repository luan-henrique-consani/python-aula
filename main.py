import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados = [3,4,8,8]

# media = np.divide(np.sum(dados), len(dados))

def descobreModa(lista):
    for i in range(len(lista)):
        primeiroDado = lista[i]

        print(primeiroDado)
        if primeiroDado != lista[i]:
            primeiroDado = lista[i]
            return
        elif primeiroDado == lista[i]:
            primeiroDado
            print(primeiroDado)
            print(lista[i])
            break

descobreModa(dados)
