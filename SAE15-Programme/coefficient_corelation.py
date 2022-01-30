###########################################
##########LIBRAIRIE DE CALCULE#############
###########################################
######## Copyright ONAY & MERENNA #########
###### Last update : 30/01/22 16h10  ######
###########################################
###########################################



import lib_calcul
from math import sqrt

#On défini les liste x et y vide
x=[]
y=[]


#Ceci permet de faire la transition entre un fichier .dat et une liste
f1=open("FR_MTP_COME.dat","r")
number_list=f1.readlines()
for b in range(12):
    number = number_list[b]
    x.append(int(number))
f1.close()


#Ceci permet de faire la transition entre un fichier .dat et une liste
f2=open("FR_MTP_COME_VELO-result.dat","r")
number_list=f2.readlines()
for b in range(12):
    number = number_list[b]
    y.append(int(number))
f2.close()

#Le résultat de chaque moyenne son stocker dans 2 variables différentes
moyenne_x=lib_calcul.moyenne(x)
moyenne_y=lib_calcul.moyenne(y)

#Calcul la covariance(x,y) selon les listes x,y et les moyennes : moyenne_x ; moyenne_y
covariance_x_y=lib_calcul.cov(x,y,moyenne_x,moyenne_y)

#Calcul la variance de x selon la liste x et sa moyenne
variance_x=lib_calcul.var(x,moyenne_x)
#Calcul la variance de y selon la liste y et sa moyenne
variance_y=lib_calcul.var(y,moyenne_y)

#Calcul à l'aide des résultat précédents le coefficient de correlation et l'arrondi a 2 chiffre après la virgule
coeff_core= covariance_x_y/sqrt(variance_x*variance_y)
print(round(coeff_core,2))

#Stock le résultat du coefficient de correlation dans un fichier.dat
f3=open("coefficient_corelation.dat","w")
f3.write(str(coeff_core))
f3.close()