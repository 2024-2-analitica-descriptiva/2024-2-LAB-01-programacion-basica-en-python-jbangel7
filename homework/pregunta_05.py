"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict




#print(final_list)


#print(x)
#print()

# 
#numbers_int = [int(z[1])for z in x] 

#list_ref = list(zip(letters,numbers_int))
#resultados = {}


def pregunta_05():

    file = open('files\input\data.csv', "r").readlines() #abro el archivo y lo leo linea por linea
    x = [z.replace('\n', '') for z in file] 
    x = [z.split('\t') for z in file] 
    letters = [z[0] for z in file] 
    numbers_int = [int(z[1])for z in x]  


    combined_list = []
    min_length = len(letters)

    for i in range(min_length):
        combined_list.append((letters[i], numbers_int[i]))

    # Group tuples by the first element (word)
    groups = defaultdict(list)
    for tup in combined_list:
        groups[tup[0]].append(tup)

    # Find max and min for each group
    result_list = []
    for word, group_tuples in groups.items():
        max_tuple = max(group_tuples, key=lambda item: item[1])
        min_tuple = min(group_tuples, key=lambda item: item[1])
        result_list.append((word, max_tuple[1], min_tuple[1]))

    final_list = sorted(result_list, key=lambda x: x[0])
    return final_list

""""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
"""

