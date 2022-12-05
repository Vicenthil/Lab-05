from enano import Enano
from elfo import Elfo
from humano import Humano

Lista_enano = []
Lista_elfo = []
Lista_humano = []
#num1= 1

"""
def aumentaVida(hum):
    aumentoHP = input("Ingrese su aumento de vida (Este debe estar entre 50 y 100)")
    vida = vida + aumentoHP
    hum.SetVida(vida)
"""

def IngresaDatos():
    nombre1=input("Ingrese el nombre de su primer personaje: ").capitalize()
    print("Enano/Elfo/Humano")
    raza1 = input("Elija una de las razas disponibles: ").capitalize()
    while raza1 != "Elfo" and raza1 != "Enano" and raza1 != "Humano":
        print("Elija una de las opiones disponibles!!!")
        print("Elfo, Enano o Humano")
        raza1 = input("Elija una de las razas disponibles: ").capitalize()
    nombre2=input("Ingrese el nombre de su segundo personaje: ").capitalize()
    print("Enano/Elfo/Humano")
    raza2 = input("Seleccione otra raza distinta a la primera: ").capitalize()
    while raza2 != "Elfo" and raza2 != "Enano" and raza2 != "Humano":
        print("Elija una de las opiones disponibles!!!")
        print("Elfo, Enano o Humano")
        raza1 = input("Elija una de las razas disponibles: ").capitalize()
    while raza1 == raza2:
        print("Error, Selecione otra raza distinta!!!")
        print("Elfo, Enano o Humano")
        raza2 = input("Elija una de las razas disponibles: ").capitalize()
    print("Lanza/Arco/Cuchillo")
    arma1 = input("Seleccione el tipo de arma de su primer personaje: ").capitalize()
    while arma1 != "Lanza" and arma1 != "Arco" and arma1 != "Cuchillo":
        print("Elija una de las opiones disponibles!!!")
        print("'Lanza' / 'Arco' / 'Cuchilla'")
        arma1 = input("Seleccione el tipo de arma de su primer personaje: ").capitalize()
    print("Lanza/Arco/Cuchillo")
    arma2 = input("Seleccione el tipo de arma de su segundo personaje: ").capitalize()
    while arma2 != "Lanza" and arma2 != "Arco" and arma2 != "Cuchillo":
        print("Elija una de las opiones disponibles!!!")
        print("'Lanza' / 'Arco' / 'Cuchilla'")
        arma2 = input("Seleccione el tipo de arma de su segundo personaje: ").capitalize()
    while arma1 == arma2:
        print("Error, Seleccione un arma distinta!!!")
        print("'Lanza' / 'Arco' / 'Cuchilla'")
        arma2 = input("Seleccione el tipo de arma de su segundo personaje: ").capitalize()
    if raza1 ==  "Enano":
        vida = 100
        daño = 15
        bonificacion1 = ("Aumento de vida")
        clan1 = input("Ingresa el nombre de tu Clan: ").capitalize()
        print("El aumento de vida tiene que estar entre 50 y 100")
        aumentovida1 = int(input("Ingresa el aumento de vida que deseas: "))
        while aumentovida1 <=49 or aumentovida1 >= 101:
            print("El aumento de vida tiene que estar entre 50 y 100")
            aumentovida1 = int(input("Ingresa el aumento de vida que deseas: "))
        en = Enano()
        en.SetNombre(nombre1)
        en.SetRaza(raza1)
        en.SetArma(arma1)
        en.SetVida(vida)
        en.SetDaño(daño)
        en.SetBonificacion(bonificacion1)
        en.SetClan(clan1)
        #en.SetAumentovida(aumentovida1)
        Lista_enano.append(en)
    if raza1 == "Elfo":
        vida = 150
        daño = 30
        bonificacion = ("Quita Vida")
        reino1 = input("Ingresa el nombre de tu Reino: ").capitalize()
        #quitavida = int(input("EL quita vida corresponde al 10% "))
        el = Elfo()
        el.SetNombre(nombre1)
        el.SetRaza(raza1)
        el.SetArma(arma1)
        el.SetVida(vida)
        el.SetDaño(daño)
        el.SetBonificacion(bonificacion)
        #el.SetQuitavida(quitavida)
        el.SetReino(reino1)
        Lista_elfo.append(el)
    if raza1 == "Humano":
        vida = 200 
        daño = 45
        bonificacion = ("Super Bono")
        familia1 = input("Ingresa el nombre de tu familia: ").capitalize()
        hu = Humano()
        hu.SetNombre(nombre1)
        hu.SetRaza(raza1)
        hu.SetArma(arma1)
        hu.SetVida(vida)
        hu.SetDaño(daño)
        hu.SetBonificacion(bonificacion)
        hu.SetFamilia(familia1)
        Lista_humano.append(hu)

    if raza2 ==  "Enano":
        vida = 100
        daño = 15
        bonificacion2 = ("Aumento de vida")
        clan2 = input("Ingresa el nombre de tu Clan: ").capitalize()
        print("El aumento de vida tiene que estar entre 50 y 100")
        aumentovida2 = int(input("Ingresa el aumento de vida que deseas: "))
        while aumentovida2 <=49 or aumentovida2 >= 101:
            print("El aumento de vida tiene que estar entre 50 y 100")
            aumentovida2 = int(input("Ingresa el aumento de vida que deseas: "))
        en = Enano()
        en.SetNombre(nombre2)
        en.SetRaza(raza2)
        en.SetArma(arma2)
        en.SetVida(vida)
        en.SetDaño(daño)
        en.SetBonificacion(bonificacion2)
        en.SetClan(clan2)
        #en.SetAumentovida(aumentovida2)
        Lista_enano.append(en)
    if raza2 == "Elfo":
        vida = 150
        daño = 30
        bonificacion = ("Quita Vida")
        reino2 = input("Ingresa el nombre de tu Reino: ").capitalize()
        #quitavida = int(input("EL quita vida corresponde al 10% "))
        el = Elfo()
        el.SetNombre(nombre2)
        el.SetRaza(raza2)
        el.SetArma(arma2)
        el.SetVida(vida)
        el.SetDaño(daño)
        el.SetBonificacion(bonificacion)
        #el.SetQuitavida(quitavida)
        el.SetReino(reino2)
        Lista_elfo.append(el)
    if raza2 == "Humano":
        vida = 200
        daño = 45
        bonificacion = ("Super Bono")
        familia2 = input("Ingresa el nombre de tu familia: ").capitalize()
        hu = Humano()
        hu.SetNombre(nombre2)
        hu.SetRaza(raza2)
        hu.SetArma(arma2)
        hu.SetVida(vida)
        hu.SetDaño(daño)
        hu.SetBonificacion(bonificacion)
        hu.SetFamilia(familia2)
        Lista_humano.append(hu)
    
def combate(raza1,raza2):
    ronda = 1
    while ronda<=10:
        if raza1 == "Elfo":
                vida = 150
                accion = input("Atacar o retirarse").capitalize()
                if accion == "Atacar":
                    num1 = float(input("introduzca el primer daño que quiere hacer:"))
                    num2 = float(input("introduzca el segundo daño que desea hacer"))
                elif accion == "Retirarse":
                    pass
                    vida = 150
        elif raza1 == "Enano":
            vida = 100
        elif raza1 == "humano":
            vida = 200
        if raza2 == "Elfo":
                vida = 150
                accion = input("Atacar o retirarse").capitalize()
                if accion == "Atacar":
                    num1 = float(input("introduzca el primer daño que quiere hacer:"))
                    num2 = float(input("introduzca el segundo daño que desea hacer"))
                elif accion == "Retirarse":
                    """""
                    try:
                    num1 = float ( input("Introduzca un número 1: "))
                    num2 = float ( input("Introduzca un número 2: "))
                    division = num1 / num2
                    print("La división es:", division)
                except ZeroDivisionError:
                    print("No se puede dividir entre 0")
                except ValueError:
                    print("No introdujo valores correctos")
                finally:
                    print("Calculo finalizado")
                    """
                    pass
                    vida = 150
        elif raza2 == "Enano":
            vida = 100
        elif raza2 == "humano":
            vida = 200
    print("El ganador es ")

def VerDatos(lista):
    for i in range(len(lista)):
        print(str(lista[i]))

def main():
    IngresaDatos()
    VerDatos(Lista_enano)
    VerDatos(Lista_elfo)
    VerDatos(Lista_humano)
    #combate(raza1,raza2)
main()
        
        
