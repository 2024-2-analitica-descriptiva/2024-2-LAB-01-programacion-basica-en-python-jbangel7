"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter
from operator import itemgetter


def pregunta_02():
    file = open('files\input\data.csv', "r").readlines() #abro el archivo y lo leo linea por linea
    x = [z[0] for z in file]                             #genero una lista con las letras de la primera columna
    l = list(Counter(x).items())                         #De la lista anterior, con Counter().items genero la tupa de letras y cantidad de estas en la lista.
    l.sort(key=itemgetter(0))                            #Ordeno la lista por arden alfabetico ascendente del key de la tupla 
    return l

#result = pregunta_02()
#print(result)

"""
Retorne la cantidad de registros por cada letra de la primera columna como
la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

Rta/
[('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

"""
