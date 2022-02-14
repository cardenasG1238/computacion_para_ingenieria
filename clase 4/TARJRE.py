# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:21:58 2022

@author: HP
"""
class TarjetaDeCredito :
    def _init_(self , banco, codigo, propietario, fechVenc):
        self.banco=banco
        self.codigo=codigo
        self.propietario=propietario
        self.fechVenc=fechVenc
    # metodos de la clase
    
    def activar():
        print("tarjeta con codigo {self.codigo} activada!")
    def bloquear (self):
        print(f"tarjeta con codigo {self.codigo} bloqueada")
    def pagar(self):
        password = input("enter your pin code")
        print (f"el password es!! {password} producto pagado")
        
# crear 3 objetos para los bancos BNB, SOL Y BCP

tarjBnb = TarjetaDeCredito('BNB', 1234, 'jhesvid car', '12/12/24')
tarjSol = TarjetaDeCredito('Banco Sol', 1234, 'jhesvid car',)