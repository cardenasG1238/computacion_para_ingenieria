# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 07:45:49 2022

@author: HP

"""

# implementacion de nuestra clase coche o car

class coche:
    """ esta clase define el estado y comportamiento de un coche """
    # atributos de clase
    ruedas = 4
    # metodo constructor
    def _init_(self,colorAuto, aceleracion):
        #asignacion de atributos y variables
        self.color =colorAuto
        self.aceleracion= aceleracion
        # setter and getters
        # getter color
        @property
        def color(self):
            return self.__color
        # setter
        @color.setter
        def color (self, nuevoColor):
            self.__color= nuevoColor
            
            
    #metodos de clase
    def acelera(self):
        print("acelerando!!!!!!")
    def frenar(self):
        print(f"frenado!!!!!  con las ruedas {self.ruedas}")
        
# creacion de objetos
coche_rojo =coche('rojo', '120km/h')

print(f"atributo de clase ------------------> {coche.ruedas}")

coche.ruedas

coche_lento_azul = coche('azul', '90km/h')
print(f"el color de cohe lento es :{coche_lento_azul.color}")
coche_lento_azul.color= "verde"
print (f"el nuevo color de cohce lento es:{coche_lento_azul.color}")

# llamar a los metodos de la clase
coche_rojo.frenar()
coche_lento_azul.acelera()  

        
    