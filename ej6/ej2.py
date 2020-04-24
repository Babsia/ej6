from manejadorviajeros import manejador
from claseviajero import viajerofrecuente
import csv
import re
def opcion0():
    print("Adiós")

def opcion1(i,l):
    print("millas acumuladas1")
    l.manej(i)

def opcion2(i,l):
    print("acumular millas")
    millas=int(input("ingrese la cantidad de millas a acumular"))
    l.manej2(i,millas)

def opcion3(i,l):
    print("Canjear millas")
    mil=int(input("ingrese la cantidad de millas a canjear"))
    l.manej3(i,mil)

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument,i,l):
    func = switcher.get(argument,lambda: print("Opción incorrecta"))
    func(i,l)

if __name__ == '__main__':
    l=manejador()
    l.testing()
    i=int(input("ingrese un numero de viajero"))
    while i<=0 or i>20:
        i=int(input("Usted no ingreso un numero valido, vuelva a intentarlo: "))
    i-=1
    bandera = False
    while not bandera:
        print("")
        print("0 Salir")
        print("1 cantidad de millas 1")
        print("2 acumular millas 2")
        print("3 canjear millas 3")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion,i,l)
        bandera = int(opcion)==0








    

    



