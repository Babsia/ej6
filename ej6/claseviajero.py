import re
class viajerofrecuente:
    __numv = 0
    __dni = ""
    __nom = ""
    __ape = ""
    __millasa = 0

    def __init__(self, num, dni, nom, ape, milla):
        self.__numv = num
        self.__dni = dni
        self.__ape = ape
        self.__millasa = milla
        self.__nom = nom

    def cantitotmillas(self):
        return(self.__millasa)

    def acummillas(self, millasv):
        self.__millasa += millasv
    def canje(self,acumm):
      if (acumm<=self.cantitotmillas()):
          self.__millasa-=acumm
          print(self.cantitotmillas())
      else:
          print("no posee esa cantidad de millas")
