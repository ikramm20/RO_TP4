import numpy as np


def vecteur_stochastique(nombre) : 
    
    vecteur = []

    print("Des elements comme '0.1','0.2','0.3' ")

    for i in range(nombre):
        element = float(input("element: "))
        vecteur.append(element)

    vecteur = np.array(vecteur)
    somme = np.sum(vecteur)
    
    if somme == 1 or somme == 0.9999999999999999 : 
        return (True,vecteur)    
    else :
       return (False,vecteur)


def matrice_stochastique():
    
    n = int(input("la dimension matricielle: "))
    liste_validation = []
    matrice = []



    for i in range(n) : 
        val,vecteur = vecteur_stochastique(n)
        liste_validation.append(val)
        matrice.append(vecteur)

    
    matrice = np.array(matrice)

    if False in liste_validation :
        return (False,matrice)
    else : 
        return (True,matrice)


def Calcule_matrice():

    negative = False
    nombre = int(input("type de matrice: "))
    val,matrice = matrice_stochastique ()
    
    if val:
        for rowPosition,row in enumerate(matrice) : 
            for colPosition,col in enumerate(row):
                if col < 0 :
                    print("valeur negative dans [",rowPosition,",",colPosition,"]")
                    nagative  = True


        if  negative == False :
            print("\n matrice : \n")
            print(matrice)
            print("\nmatrice ",nombre," : \n")
            print(np.power(matrice,nombre))

    else : 
        print(matrice," n'est pas stochastique")


def switch_def ():
    
    while True : 

        print("\n\n*********Question de type 1 jusqu'à 3: Q1-> verifier si vecteur stochastique, Q2-> verifier si Matrice stochastique , Q3-> Calculer matrice*********" )

        choix = int(input("Choisir un type de Question: "))

        if choix == 1:
            nombre = int(input("Nombre d'éléments vectoriels : "))
            val,vecteur = vecteur_stochastique(nombre)

            if val:
                print(vecteur," vecteur est stochastique") 
            else :
                print(vecteur," vecteur n'est pas stochastique") 


        elif choix == 2:
            val,matrice = matrice_stochastique()

            if val:
                print(matrice," matrice est stochastique") 
            else :
                print(matrice," matrice n'est pas stochastique") 
        
        elif choix == 3:

            Calcule_matrice()


        elif choix == 4 : 
            break
        else : 
            print("Entree invalide")
            

if __name__ == "__main__" :
    
    switch_def ()