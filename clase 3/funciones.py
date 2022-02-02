# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:02:31 2022

@author: HP
"""

def mi_funcion ():
    print("hola mundo")

def returnHolaMundo ():
   return "hola mundo"


# llamar una funcion 
mi_funcion ()
# llamar una funcion que retorna algo
hola_mundo = returnHolaMundo()
print(hola_mundo)

#paramentros de funciones

def mi_funcion_params(nombre, apellido):
    print (nombre, apellido)
  
# llamar a una funcion qe tiene parametros
mi_funcion_params ('jhesvid' ,'cardenas')

def mi_funcion_param (nombre , apellido):
    return f'{nombre} - {apellido}'
nombreApconGion = mi_funcion_param ('jhesvid' , 'cardenas')
print(nombreApconGion)
# como fue implementado el pop
def pop(lista, index=0):
    mi_funcion ()
    print (lista, index)
    
lista = [1,2,3]

pop(lista) # la lista [1,2,4]3
# va aeliminar el ultimo elemento ejemplo el 4
lista.pop()
print(lista)
#elimina el elemnto con el indice 0 res=> elimina el numero 1
lista.pop(0)
print(lista)



