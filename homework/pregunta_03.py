"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
"""
file = open('files\input\data.csv', "r").readlines() #abro el archivo y lo leo linea por linea
x = [z.replace('\n', '') for z in file] 
x = [z.split('\t') for z in file] 
letters = [z[0] for z in file] 
numbers = [z[1] for z in x]   
numbers_int = [int(z[1])for z in x] 

list_ref = list(zip(letters,numbers_int))
resultados = {}

for l, n in list_ref:
        if l in resultados:
            resultados[l] += n
    
        else:
            resultados[l] = n

tupla = sorted(list(resultados.items()))


  

print(x)
print()
print(letters)
print()
print(numbers)
print()
print(numbers_int)
print()
print(list_ref)
print()
print(tupla)
"""


def pregunta_03():
    file = open('files\input\data.csv', "r").readlines() #abro el archivo y lo leo linea por linea
    x = [z.replace('\n', '') for z in file]              # reemplazo el salto de carro por espacio vacio
    x = [z.split('\t') for z in file]                    # genero el split a partir de la tabulación
    letters = [z[0] for z in file]                       # Creo una lista con todas las letras de la primera columna
    numbers = [z[1] for z in x]                          # Creo una lista con todas los strings de la segunda columna
    numbers_int = [int(z[1])for z in x]                  # Convierto los strings de la segunda columna a números

    list_ref = list(zip(letters,numbers_int))            # Creo una lista de tuplas con las letras como Key, y los números como value
    resultados = {}

    for l, n in list_ref:
            if l in resultados:
                resultados[l] += n
        
            else:
                resultados[l] = n

    tuple_fin = sorted(list(resultados.items()))
    return(tuple_fin)
    
    
"""""
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
