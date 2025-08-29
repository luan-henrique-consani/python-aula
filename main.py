import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados = [8,4,3,8]
media = np.divide(np.sum(dados), len(dados))

def descubraModa(lista):
    numeroRepete = max(set(lista), key=lista.count)
    return numeroRepete


def descubraMediana(lista):
    listaOrganizada = sorted(lista)
    mediana = 0
    if len(lista) % 2 == 0:
       i = len(listaOrganizada)
       primeiroNum = listaOrganizada[(i // 2) - 1]
       segundoNum = listaOrganizada[i // 2]
       mediana = np.divide(primeiroNum + segundoNum, 2)
    elif len(lista) % 2 == 1:
        i = len(listaOrganizada)
        numeroMeio = listaOrganizada[i // 2]
        mediana = numeroMeio
    
    return mediana

def descrubaDispersaoPadrao(lista):
    listaOrganizada = sorted(lista)
    for i in range(len(listaOrganizada)):
        numero = np.pow((listaOrganizada - media) * -1, 2)
    soma = np.sum(numero)
    dp = np.sqrt(soma)
    return dp
        
    
variancia = np.pow(descrubaDispersaoPadrao(dados),2)

# respostas

print("----------------------------------------------------")
print(f"Essa é sua média: {media}")
print("----------------------------------------------------")
print(f"Essa é sua moda: {descubraModa(dados)}")
print("----------------------------------------------------")
print(f"Essa é sua mediana: {descubraMediana(dados)}")
print("----------------------------------------------------")
print(f"Essa é a dispersão padrão: {descrubaDispersaoPadrao(dados):.3f}")
print("----------------------------------------------------")
print(f"Essa é a variância: {variancia}")

