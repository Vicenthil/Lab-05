from personaje import Personaje

class Enano(Personaje):
    def __init__(self,nombre="",raza="",arma="",vida="",daño="",bonificacion="",clan=""):
        super().__init__(nombre,raza,arma,vida,daño,bonificacion)
        self.__clan = clan 

    def __str__(self):
        return super().__str__()+ "Clan: {} ".format(self.__clan)
    
    def GetClan(self):
        return self.__clan
    
    def SetClan(self,clan):
        self.__clan = clan

    def Historia(self):
        pass
    def Victoria(self):
        pass
    def Derrota(self):
        pass
    def AumentaVida(self):
        pass