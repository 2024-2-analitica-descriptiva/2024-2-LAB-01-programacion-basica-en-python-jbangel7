"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter
"""
file = open('files\input\data.csv', "r").readlines() #abro el archivo y lo leo linea por linea
x = [z.replace('\n', '') for z in file] 
x = [z.split('\t') for z in file] 
date = [z[2] for z in x] 
date_splt = [z.split('-') for z in date]
month = [z[1] for z in date_splt] 

final_log = sorted(list(Counter(month).items()))


print(x)
print()
print(date)
print()
print(date_splt)
print()
print(month)
print()
print(final_log)
"""



def pregunta_04():
    file = open('files\input\data.csv', "r").readlines() #abro el archivo y lo leo linea por linea
    x = [z.replace('\n', '') for z in file] 
    x = [z.split('\t') for z in file] 
    date = [z[2] for z in x] 
    date_splt = [z.split('-') for z in date]
    month = [z[1] for z in date_splt] 

    final_log = sorted(list(Counter(month).items()))
    return final_log


    
"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
