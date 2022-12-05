from personaje import Personaje

class Elfo(Personaje):
    def __init__(self,nombre="",raza="",arma="",vida="",daño="",bonificacion="",reino=""):
        super().__init__(nombre,raza,arma,vida,daño,bonificacion)
        self.__reino = reino

    def __str__(self):
        return super().__str__()+"reino: {} ".format(self.__reino)
    
    def GetReino(self):
        return self.__reino
    
    def SetReino(self,reino):
        self.__reino = reino

    def Historia(self):
        pass
    def Victoria(self):
        pass
    def Derrota(self):
        pass
    def QuitaVida(self):
        pass
    