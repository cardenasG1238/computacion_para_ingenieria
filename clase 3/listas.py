# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:23:44 2022

@author: HP
"""

#array en blanco

lista = []

#lista con elementos
listelementos = [1,3,4,5]

#acceder a los elementos de una list

listalumnos = ["jhonny","rither","jose"]
alumnoPos_1 =listalumnos [len(listalumnos)-1] # rither
# obtener el tamaño de la lista
tamañolistalumnos = len(listalumnos)
print("el tamaño de la lista alumnos es :", tamañolistalumnos)
#insertar elementos a una lista
lista.append (1)
lista.append (2)
lista.append (5)
#lista [1,2,5]
#lista [1,2,3,5]
#insertar un elemento en un indice de la lista
#insertar (indice(o, tamaño -1), elemeto)
lista.insert (2, 3)
print (lista)
#eliminar elementos de una lista
#lista [1,2,3,5]
lista.pop()
print (lista)
#lista [1,2,3
lista.pop(0)
#lista [2,3]
print (lista)

listadocentes = ["jhonny", "caballero", "haku"]

listadocentes.remove ("caballero")
# ["jhonny", "haku"]

print(listadocentes)


#iterar listas

for docente in listadocentes :
    print(docente)

tamañolistadocentes = len(listadocentes)
for i in range(0, len(listadocentes)):
    
    print(listadocentes[i])
    
    