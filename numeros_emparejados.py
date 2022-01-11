'''
- El numero que más veces ha salido es el 3.
- El numero que mas veces ha salido como complementario del 3, es el 10 con 51 veces.
- El numero que más veces ha salido junto con el 3 y el 10 es el 49 con 10 veces.
- 03 / 10 / 49
'''
import json
from libreria_primitiva import *

lista_numeros = []
with open('./json/primitiva_numbers.json') as file:
    data = json.load(file)
    for elemento in data:
        if "3" in elemento["Numbers"]:
            lista_numeros.append(elemento["Numbers"])
diccionario_numeros = {}

for numeros in lista_numeros:
    for numero in numeros:
        if numero != "3":
            if numero in diccionario_numeros.keys():
                diccionario_numeros[numero] += 1
            else:
                diccionario_numeros[numero] = 0
#print(ordenar_diccionario(diccionario_numeros))

diccionario_aux = {}
for numeros in lista_numeros:
    if set(['3', '10']).issubset(set(numeros)):
        for numero in numeros:
            if numero in diccionario_aux.keys():
                diccionario_aux[numero] += 1
            else:
                diccionario_aux[numero] = 0
print(ordenar_diccionario(diccionario_aux))