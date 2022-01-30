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

#VIDE LE "CACHE" càd les fichiers d'enregistrements des données

f4 = open("FR_MTP_COME_VELO-result.dat", "w", encoding='utf8')
f4.close()
f7 = open("MOYENNE_FR_MTP_COME_VELO.dat", "w")
f7.close()*

#création d'une liste pour calculer la moyenne
moyenne_velo=[]


# Enregistre une première fois la data du site dans un texte avec une requete (pareil que le parking)
# et parse et récupere le nombre de vélo disponible/libre pour le parking d'id 002 donc velomag comédie
#Calcule aussi la moyenne du nombre de vélo disponible/libre
# 12 ECHANTILLON (1/h) pour cela le programme et dans une boucle dans une range de 12 et la fin de la boucle une commande sleep de la libraire TIME endorme
#le programme durant 3600seconde c'est à dire 1H
for i in range(12):
    req = requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
    f3 = open("FR_MTP_COME_VELO.dat", "w", encoding="utf8")
    f3.write(f"{req.text}\n")
    f3.close()
    f4 = open("FR_MTP_COME_VELO-result.dat", "a", encoding='utf8')
    tree = etree.parse("FR_MTP_COME_VELO.dat")
    for si in tree.xpath("/vcs/sl/si"):
        if si.get("id") == "002":
            print(si.get("fr"))
            f4.write(f'{si.get("fr")}\n')
            f4.close()
            moyenne_velo.append(int(f'{si.get("fr")}'))
    sleep(3600)


#Calcul est stock la moyenne dans un fichier.dat
f7 = open("MOYENNE_FR_MTP_COME_VELO.dat", "a")
calcul_velo = lib_calcul.moyenne(moyenne_velo)
print("La moyenne est de test : ", calcul_velo)
f7.write(str(f'{calcul_velo}\n'))
f7.close()

#Calcul est stock l'écart type dans un fichier.dat
velo_sigma=lib_calcul.sigma(moyenne_velo,calcul_velo)
print("Sigma : ",velo_sigma)
f11=open("SIGMA_FR_MTP_COME_VELO.dat","w")
f11.write(str(velo_sigma))
f11.close()