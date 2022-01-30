###########################################
##########LIBRAIRIE DE CALCULE#############
###########################################
######## Copyright ONAY & MERENNA #########
###### Last update : 30/01/22 16h10  ######
###########################################
###########################################


import requests
from lxml import etree
from time import sleep
import lib_calcul

#On determine une liste vide pour calculer la moyenne
free_moyenne=[]






# Vide le "CACHE"
parkings=["FR_MTP_COME"]
for i in range(len(parkings)):
    f1 = open(str(f'{parkings[i]}.dat'), "w")
    f1.close()
    f2 = open(str(f'MOYENNE_{parkings[i]}.dat'), "w")
    f2.close()



#REQUETE LXML RECUPERE LA DATA DU PARKING COMEDIE ET LA STOCK DANS UNE VARIABLE "REQ" PUIS PARSE PARRAPORT AU ENTETE POUR AVOIR
# CE QUE L'ON SOUHAITE DONC / PLACE LIBRE /
#ajoute dans la liste free_moyenne le résultat de free.text pour calculer la moyenne (free.text est le nombre de place libre)
# PUIS STOCK DANS UN FICHIER .DAT POUR POUVOIR LE LIRE AVEC GNUPLOT
# 12 ECHANTILLON (1/h) pour cela le programme et dans une boucle dans une range de 12 et la fin de la boucle une commande sleep de la libraire TIME endorme
#le programme durant 3600seconde c'est à dire 1H


for i in range(12):
    for i in range(len(parkings)):
        f1 = open(str(f'{parkings[i]}.dat'), "a")
        r = requests.get(f'https://data.montpellier3m.fr/sites/default/files/ressources/{parkings[i]}.xml')
        req=r.text
        req = req[40:]
        print(req)
        parser = etree.XMLParser()
        tree = etree.XML(req, parser)
        for free in tree.xpath("/park/Free"):
            print({free.text})
            f1.write(f'{free.text}\n')
            free_moyenne.append(int(free.text))
        f1.close()

    sleep(3600)


#Stocke dans le fichier.dat le résultat de la moyenne du parkings[i] dans notre cas le parking "FR_MTP_COME" est le seul volontairements
f2 = open(str(f'MOYENNE_{parkings[i]}.dat'), "a")
moyenne_park = lib_calcul.moyenne(free_moyenne)
print("La moyenne est de : ", moyenne_park)
f2.write(str(f'{moyenne_park}\n'))
f2.close()

#Calcul l'écart type
park_sigma=lib_calcul.sigma(free_moyenne,moyenne_park)
print("Sigma : ",park_sigma)

#stocke l'écart type dans un ficher.dat
f11=open("SIGMA_FR_MTP_COME_PARK.dat","w")
f11.write(str(park_sigma))
f11.close()