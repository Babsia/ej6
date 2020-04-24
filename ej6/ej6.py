from clasefecha import FechaHora
def opcion0():
    print("Adiós")

def opcion1(a,b):
    suma=hora1+hora2
    test.AdelantarHora(suma)
    test.Mostrar()


def opcion2(a,b):
    resta=hora1-hora2
    test.AdelantarHora(resta)
    test.Mostrar()

def opcion3(a,b):
    comp=hora1>hora2
    if comp==True:
        print("el mayor es:{}".format(a))
    else:
        print("el mayor es:{}".format(b))

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument,a,b):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(a,b)

if __name__ == '__main__':
    bandera = False
    a=int(input("ingrese hora"))
    b=int(input("ingrese hora"))
    while a>24 or b>24:
        a=int(input("ingrese hora en formato 24h"))
        b=int(input("ingrese hora en formato 24h"))
    hora1=FechaHora(1,1,2020,a,0,0)
    hora2=FechaHora(1,1,2020,b,0,0)
    test=FechaHora(1,1,2020,0,0,0)

    while not bandera:
        print("")
        print("0 Salir")
        print("1 sumar hora")
        print("2 restar hora2")
        print("3 distinguir mayor 3")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion,a,b)
        bandera = int(opcion)==0