from claseviajero import viajerofrecuente
import csv
import re
class manejador:
    __lista=[]
    def manej(self,i):
        print(self.__lista[i].cantitotmillas())
    def manej2(self,i,millas):
        self.__lista[i].acummillas(millas)
    def manej3(self,i,millasc):
        self.__lista[i].canje(millasc)

    def testing(self):
        archi=open('viajeros.csv')
        reader = csv.reader(archi, delimiter=',')
        for fila in reader:
            num=int(fila[0])
            dni=re.match('^[0-9]+$',fila[1])
            nom=str(fila[2])
            ap=str(fila[3])
            milla=int(fila[4])
            if type(num)==int and type(dni)==re.Match and type(nom)==str and type(ap)== str and type(milla)==int:
                viajerox=viajerofrecuente(num,dni,nom,ap,milla)
                self.__lista.append(viajerox)
        return (self.__lista)
        