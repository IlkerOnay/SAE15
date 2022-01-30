###########################################
##########LIBRAIRIE DE CALCULE#############
###########################################
######## Copyright ONAY & MERENNA #########
###### Last update : 30/01/22 16h10  ######
###########################################
###########################################

#Ce programme sert juste a crée des fonctions de calcul

import math



#La fonction nommer "moyenne ", permet de calculer la moyenne
#L est une liste des nombres dont il faut calculer la moyenne



def moyenne(L):
    somme = 0
    for i in range(len(L)):
        somme += L[i]
    somme = somme / len(L)
    return somme





#Calcule l'écart-type, L est une liste de chiffre et m leur moyenne

def sigma(L,m):
    valeur = 0
    for i in range(len(L)):
        valeur = valeur + (L[i]-m)**2
    result=math.sqrt(valeur/len(L))
    result=round(result,2)
    return result



#calcul la covariance de x,y pour le coefficient de corrélation / x,y une liste et moyenne_x moyenne_y leur moyenne respectifs

def cov(x,y,moyenne_x,moyenne_y):
    valeur1 = 0
    valeur2 = 0
    valeur_final = 0
    for i in range(len(x)):
        valeur1 = x[i]-moyenne_x
        valeur2 = y[i]-moyenne_y
        valeur3 = valeur1*valeur2
        valeur4 = valeur3*1/len(x)
        valeur_final = valeur_final +valeur4
    valeur_final= round(valeur_final,2)
    return valeur_final



#calcul de la variance (on reprend sigma de lib_calcul est on enleve la racine carré sigma qui est là pour calculer l'écart-type donc on obtient la variance )

def var(L,m):
    valeur = 0
    for i in range(len(L)):
        valeur = valeur + (L[i]-m)**2
        result = valeur /len(L)
    result=round(result,2)
    return result


