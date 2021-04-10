#1 Algoritmos de Ordenação

import random
import time
import timeit

#1
'''def calc_time():
    for i in range(1, 5):
        time.sleep(1)

inicio = timeit.default_timer()
calc_time()
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))

def selection_sort(list_func):
    n = len(list_func)

    for a in range(0, n):
        index_min = a
        for j in range(a + 1, n):
            if list_func[j] < list_func[index_min]:
                index_min = j
        list_func[a], list_func[index_min] = list_func[index_min], list_func[a]

    return list_func

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        insert_value = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > insert_value:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = insert_value
    return lista

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista'''

#3
import pandas as pd
import csv
def read_csv(): #código para leitura de arquivo csv
    courses = []
    with open('C:/Users/USER10/Desktop/Samuel/Faculdade/3º Semestre/Linguagem de Programação/linguageDeProgramacaoOficial1-master/cursos-prouni2.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            courses.append(row[0])
    return courses

def del_name(courses_name):
    listaP = []
    num = 0
    for lis in courses_name:
        lis = lis.rstrip()
        for letter in listaP:
            if letter == lis:
                num = 1
        if num == 0:
            listaP.append(lis)
            num = 0
        else:
            num = 0
    return listaP


if __name__ == '__main__':

    '''#lista = [8,22,5,-12,0,3,7]
    lista = random.sample(range(50_000), 50_000)
    #print(f'Unordered: {lista}')

    ordered_list3 = insertion_sort(lista)
    print(f'Insertion sort:   {ordered_list3}')
    calc_time()
    #insertion_sort = 4.000462 com print
    #insertion_sort = 4.054306 sem print

    ordered_list = selection_sort(lista)
    print(f'Selection Sort:   {ordered_list}')
    calc_time()
    #selection_sort = 4.018994 com print
    #selection_sort = 3.996126 sem print

    ordered_list2 = bubble_sort(lista)
    print(f'Bubble sort: {ordered_list2}')
    calc_time()
    #bubble_sort = 4.014290 com print
    #bubble_sort = 4.004033 sem print'''

#2
'''Buscar Linear ou sequêncial: 
E comparado valor a valor até que se encontre o valor desejado, neste caso
pode-se dizer que ele trabalha também com a sorte, pois se o valor estiver no final da lista, ele irá
percorrer todo a lista até retornar o valor.
Busca Binária:
A busca binária divide o valor ao meio, nesta divisão ele verifica se o valor que é solicitado
é menor ou maior do que os valores feitos nesta divisão e esta divisão vai sendo feita até que seja encontrado o valor.
Este algoritmo é o mais vantajoso e traz o resultado em menos tempo.'''

#3
courses_name = read_csv()
#print(sorted(courses_name))
#print(type(courses_name))
del_name(courses_name)
print(sorted(del_name(courses_name, '\n')))
len(courses_name)

