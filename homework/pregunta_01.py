"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
"""
x = open('files\input\data.csv', "r").readlines()

print(x)
print()



def pregunta_01(files, column):
    x = [z.replace('\n', '') for z in files] 
    x = [z.split('\t') for z in files] 
    valores = [int(z[column]) for z in x] 
    total = sum(valores)
    return total


rev = pregunta_01(x, 1)

print(rev)
"""


"""
Retorne la suma de la segunda columna

Rta/
214

"""

"""
x = [z.replace('\n', '') for z in x] 
print()
print(x)
print()

x = [z.split('\t') for z in x] 
print()
print(x)

x = [int(z[1]) for z in x] 
print()
print(x)

x = sum(x)
print()
print(x)
"""


def pregunta_01():
    file = open('files/input/data.csv', "r").readlines()
    x = [z.replace('\n', '') for z in file] 
    x = [z.split('\t') for z in file] 
    valores = [int(z[1]) for z in x] 
    total = sum(valores)
    return total

#msuma = pregunta_01()
#print(msuma)