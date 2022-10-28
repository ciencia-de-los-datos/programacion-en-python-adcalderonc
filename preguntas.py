"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from lib2to3.pgen2 import driver
with open(r"data.csv", "r") as file:
   data = file.readlines()


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open(r"data.csv", "r") as file:
        data = file.readlines()
    data[0:2]
    data_events = [line.replace("\n", "") for line in data]
    data_events = [line.split('\t') for line in data_events]
    data_events= [line[1:2] for line in data_events]
    data_events= [int(line[0]) for line in data_events]
    return (sum(data_events))


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data_dos = [line.replace("\n", "") for line in data]
    data_dos = [line.split('\t') for line in data_dos]
    data_dos= [line[0] for line in data_dos]
    from collections import Counter
    from operator import itemgetter

    letras= Counter((data_dos))
    d1 = letras
    l2 =[]

    for i in d1:
        tpl = (i, d1[i])
        l2.append(tpl)

    l2.sort(key=itemgetter(0), reverse=False)
    return l2

# si me da?

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    from operator import itemgetter
    data_tres = [line.replace("\n", "") for line in data]
    data_tres = [line.split('\t') for line in data_tres]
    data_tres= [line[0:2] for line in data_tres]
    diccionario={}
    sumadorA=0
    sumadorB=0
    sumadorC=0
    sumadorD=0
    sumadorE=0
    for row in data_tres:
        if row[0]=='A':
            sumadorA+=int(row[1])
            diccionario[row[0]]= sumadorA
        elif row[0]=='B':
            sumadorB+=int(row[1])
            diccionario[row[0]]= sumadorB
        elif row[0]=='C':
            sumadorC+=int(row[1])
            diccionario[row[0]]= sumadorC
        elif row[0]=='D':
            sumadorD+=int(row[1])
            diccionario[row[0]]= sumadorD
        elif row[0]=='E':
            sumadorE+=int(row[1])
            diccionario[row[0]]= sumadorE
    d2 = diccionario
    l3 =[]

    for i in d2:
            tpl = (i, d2[i])
            l3.append(tpl)

    l3.sort(key=itemgetter(0), reverse=False)
    return l3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from collections import Counter
    from operator import itemgetter


    data_cuatro =[line.replace("\n", "") for line in data]
    data_cuatro = [line.split('\t') for line in data_cuatro]
    data_cuatro= [line[2] for line in data_cuatro]
    #print(data_cuatro)


    prueba= []

    for row in data_cuatro:
        prueba.append(row[5:7])

    d1 = Counter((prueba))
    l2 =[]

    for i in d1:
        tpl = (i, d1[i])
        l2.append(tpl)

    l2.sort(key=itemgetter(0), reverse=False)

    return l2


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open(r"data.csv", "r") as file:
        data = file.readlines()
    data_cinco = [line.replace("\n", "") for line in data]
    data_cinco = [line.split('\t') for line in data_cinco]
    data_cinco= [line[0:2] for line in data_cinco]

    listaordenada=[]
    listatuplas=[]

    def organizador(lista):
        etiqueta= lista[0] 
        valor= lista[1]
        ind_etiqueta=None
        if len(listaordenada) ==0: 
            listaordenada.append([etiqueta,[valor]])
        else:
            for index, row in enumerate(listaordenada):
                if etiqueta in row:
                    ind_etiqueta=index
                    break
            if ind_etiqueta is None:
                listaordenada.append([etiqueta,[valor]])
            else:
                listaordenada[ind_etiqueta][1].append(valor)


    def tuplas(lista):
        listatuplas.append((lista[0], int(max(lista[1])), int(min(lista[1]))))

    for row in data_cinco:
        organizador(row)
    for row in listaordenada:
        tuplas(row)
    a=sorted(listatuplas)

    return a


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open(r"data.csv", "r") as file:
        data = file.readlines()

    data_seis = [line.replace("\n", "") for line in data]
    data_seis = [line.split('\t') for line in data_seis]
    data_seis= [line[4:5] for line in data_seis]


    lista_dic=[]
    listaordenada=[]
    listatuplas=[]

    def organizador(lista):
        etiqueta= lista[0] 
        valor= int(lista[1])
        ind_etiqueta=None
        if len(listaordenada) ==0: 
            listaordenada.append([etiqueta,[valor]])
        else:
            for index, row in enumerate(listaordenada):
                if etiqueta in row:
                    ind_etiqueta=index
                    break
            if ind_etiqueta is None:
                listaordenada.append([etiqueta,[valor]])
            else:
                listaordenada[ind_etiqueta][1].append(valor)


    def tuplas(lista):
        listatuplas.append((lista[0], min(lista[1]), max(lista[1])))

    for i in data_seis:
        for j in i[0].split(','):
            token= j.split(':')
            lista_dic.append(token)

    for row in lista_dic:
        organizador(row)

    for row in listaordenada:
        tuplas(row)

    b=sorted(listatuplas)

    return b


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data_siete = [line.replace("\n", "") for line in data]
    data_siete = [line.split('\t') for line in data_siete]
    data_siete= [line[0:2] for line in data_siete]


    listaordenada=[]

    def organizador(lista):
        etiqueta= int(lista[1]) 
        valor= lista[0]
        ind_etiqueta=None
        if len(listaordenada) ==0: 
            listaordenada.append((etiqueta,[valor]))
        else:
            for index, row in enumerate(listaordenada):
                if etiqueta in row:
                    ind_etiqueta=index
                    break
            if ind_etiqueta is None:
                listaordenada.append((etiqueta,[valor]))
            else:
                listaordenada[ind_etiqueta][1].append(valor)

    for row in data_siete:
        organizador(row)

    f=sorted(listaordenada)

    return f


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data_ocho = [line.replace("\n", "") for line in data]
    data_ocho = [line.split('\t') for line in data_ocho]
    data_ocho= [line[0:2] for line in data_ocho]


    listaordenada=[]

    def organizador(lista):
        etiqueta= int(lista[1]) 
        valor= lista[0]
        ind_etiqueta=None
        if len(listaordenada) ==0: 
            listaordenada.append((etiqueta,[valor]))
        else:
            for index, row in enumerate(listaordenada):
                if etiqueta in row:
                    ind_etiqueta=index
                    break
            if ind_etiqueta is None:
                listaordenada.append((etiqueta,[valor]))
            else:
                if valor not in listaordenada[ind_etiqueta][1] :
                    listaordenada[ind_etiqueta][1].append(valor)
                    listaordenada[ind_etiqueta][1].sort()

    for row in data_ocho:
        organizador(row)

  
    return sorted(listaordenada)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data_nueve = [line.replace("\n", "") for line in data]
    data_nueve = [line.split('\t') for line in data_nueve]
    data_nueve= [line[4:5] for line in data_nueve]


    lista_dic=[]
    listaordenada=[]
    listatuplas=[]

    def organizador(lista):
        etiqueta= lista[0] 
        valor= lista[1]
        ind_etiqueta=None
        if len(listaordenada) ==0: 
            listaordenada.append([etiqueta,[valor]])
        else:
            for index, row in enumerate(listaordenada):
                if etiqueta in row:
                    ind_etiqueta=index
                    break
            if ind_etiqueta is None:
                listaordenada.append([etiqueta,[valor]])
            else:
                listaordenada[ind_etiqueta][1].append(valor)


    def tuplas(lista):
        listatuplas.append((lista[0], len(lista[1])))

    for i in data_nueve:
        for j in i[0].split(','):
            token= j.split(':')
            lista_dic.append(token)

    for row in lista_dic:
        organizador(row)

    for row in sorted(listaordenada):
        tuplas(row)

        
    return dict(listatuplas)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data_diez = [line.replace("\n", "") for line in data]
    data_diez = [line.split('\t') for line in data_diez]
    data_diez= [line[0:5] for line in data_diez]


    listaordenada=[]

    def organizador(lista):
        etiqueta= lista[0] 
        valor1= len(lista[3].split(','))
        valor2= len(lista[4].split(','))
        listaordenada.append((etiqueta, valor1, valor2))


    for row in data_diez:
        organizador(row)


    return listaordenada


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data_once = [line.replace("\n", "") for line in data]
    data_once = [line.split('\t') for line in data_once]
    data_once= [line[1:4] for line in data_once]


    lista_dic=[]
    listaordenada=[]
    listatuplas=[]

    def organizador(lista):
        etiqueta= lista[0] 
        valor= int(lista[1])
        ind_etiqueta=None
        if len(listaordenada) ==0: 
            listaordenada.append([etiqueta,[valor]])
        else:
            for index, row in enumerate(listaordenada):
                if etiqueta in row:
                    ind_etiqueta=index
                    break
            if ind_etiqueta is None:
                listaordenada.append([etiqueta,[valor]])
            else:
                listaordenada[ind_etiqueta][1].append(valor)


    def tuplas(lista):
        listatuplas.append((lista[0], sum(lista[1])))

    for i in data_once:
        for j in i[2].split(','):
            lista_dic.append([j,i[0]])

    for row in lista_dic:
        organizador(row)

    for row in sorted(listaordenada):
        tuplas(row)
    
    return dict(listatuplas)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data_doce = [line.replace("\n", "") for line in data]
    data_doce = [line.split('\t') for line in data_doce]
    data_doce= [line[0:5] for line in data_doce]

    lista_dic=[]
    listaordenada=[]
    listatuplas=[]

    def organizador(lista):
        etiqueta= lista[0] 
        valor= int(lista[1])
        ind_etiqueta=None
        if len(listaordenada) ==0: 
            listaordenada.append([etiqueta,[valor]])
        else:
            for index, row in enumerate(listaordenada):
                if etiqueta in row:
                    ind_etiqueta=index
                    break
            if ind_etiqueta is None:
                listaordenada.append([etiqueta,[valor]])
            else:
                listaordenada[ind_etiqueta][1].append(valor)


    def tuplas(lista):
        listatuplas.append((lista[0], sum(lista[1])))

    for i in data_doce:
        for j in i[4].split(','):
            token= j.split(':')
            lista_dic.append([i[0],int(token[1])])

    for row in lista_dic:
        organizador(row)

    for row in sorted(listaordenada):
        tuplas(row)

    return dict(listatuplas)
