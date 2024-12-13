"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from collections import Counter
from collections import defaultdict

def pregunta_06():

    file = open('files/input/data.csv', "r").readlines() #abro el archivo y lo leo linea por linea
    x = [z.replace('\n', '') for z in file] 
    x = [z.split('\t') for z in file] 
    dict = [z[4] for z in x] 
    dict1 = [z.replace('\n', '') for z in dict] 
    dict_splt = [z.split(',') for z in dict1]
    dict_splt1 = [[','.join(z.split(':')) for z in sublist] for sublist in dict_splt]
    dict_splt2 = [[(z.split(',')) for z in sublist] for sublist in dict_splt1]

    l1 = []
    for sublist in dict_splt2:
        for item in sublist:
            l1.append(item)


    words = [z[0]for z in l1]  
    numbers= [int(z[1])for z in l1]  

    new_list = []
    for i in range(len(words)):
            new_list.append((words[i], numbers[i]))


    # Group tuples by the first element (word)
    groups = defaultdict(list)
    for tup in new_list:
            groups[tup[0]].append(tup)

    # Find max and min for each group
    result_list = []
    for word, group_tuples in groups.items():
            max_tuple = max(group_tuples, key=lambda item: item[1])
            min_tuple = min(group_tuples, key=lambda item: item[1])
            result_list.append((word, min_tuple[1], max_tuple[1]))

    final_list = sorted(result_list, key=lambda x: x[0])
    return final_list




# print()
# print(numbers)
# print()
# print(words)
# print()
# print(new_list)
# print()
# print(final_list)
# print()
# print(l1_splt)
# print(final_log)


# def pregunta_06():
#     """
#     La columna 5 codifica un diccionario donde cada cadena de tres letras
#     corresponde a una clave y el valor despues del caracter `:` corresponde al
#     valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
#     pequeño y el valor asociado mas grande computados sobre todo el archivo.

#     Rta/
#     [('aaa', 1, 9),
#      ('bbb', 1, 9),
#      ('ccc', 1, 10),
#      ('ddd', 0, 9),
#      ('eee', 1, 7),
#      ('fff', 0, 9),
#      ('ggg', 3, 10),
#      ('hhh', 0, 9),
#      ('iii', 0, 9),
#      ('jjj', 5, 17)]

#     """
