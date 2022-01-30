# <ins>SAE 15 : Traiter des données /ONAY ILKER/MERENNA NATHAN /</ins>


Pour pouvoir traiter des données il faut tout d'abord les acquérirs, dans notre cas le site pour la récolte de données sera le site suivants : <br>
https://data.montpellier3m.fr/ <br>
C'est la data center de montpellier en libre accès pour ce qui le souhaite.
***
<br>

## <ins> Le "scraping" :</ins>
<br>
Le web scraping est une technique d'extraction du contenu de sites Web, via un script ou un programme, dans le but de le transformer pour permettre son utilisation dans un autre contexte. <br> <br>

***
<br>

## <ins>La librairie :</ins>
<br>
Dans notre cas nous allons utiliser différentes librairies tel que :<br>
-lxml : pour parser est récupérer ce qui nous intéresses dans le fichier selon leur entête<br>
-requests : récupérer les données depuis le site est le stocker dans une variable/texte pour pouvoir le traiter avec lxml<br>
-time : dans la librairie time nous allons utiliser "sleep" qui permet "d'endormir" le programme un temps voulu en seconde pour pouvoir crée une boucle pour pouvoir échantilloners tout les "X" temps (X=3600 dans notre cas pour 1h <br><br>

***
<br>

## <ins>Le programme : </ins>

C'est la partie la plus intéréssantes de notre travails. <br>
Notre programmations a été effectué sur seulement 2 parkings, mais il est modulable pour plusieurs. Nous avons choisis le vélomag Comédie et le parking voiture Comédie stratégiquements, car le programme ne s'effectue pas au hasard sur des parkings et vélomag qui n'ont rien a avoir entre eux mais sur deux choses très proche.<br>
Nous avons crée plusieurs programme la première étant "park.py", il consiste simplement a récupérer la data du parking de la place de la comédie, de récupérer les informations utilise comme le nombre de place restante. Pour ensuite calculer la moyenne de place restante et l'écart type de celui-ci tout en stockant les informations et calcul intéréssantes.
<br>
Le deuxième programme "velomag.py" est une copie du proccesus du premier programme, même si le programme change un peu car les entêtes des fichiers ne sont pas les mêmes mais le reste plus ou moins pareils
<br>
Une des parties intéressantes, le troisième programme et aussi le quatrième, "lib_calcul.py" et "coefficient_corelation.py" , c'est deux programme sont tout deux des programmes de calcul les calculs retrouver sont les suivantes : <br>
<ins>Pour lib_calcul :</ins> <br>
-La moyenne<br>
-L'écart type<br>
-La covariance<br>
-La variance<br>
<br>
<ins>Pour coefficient_corelation :</ins> <br>
-Stockage des contenues d'un fichier dans une liste<br>
-Apelle a la fonction de la moyenne, covariance, variance pour calculer le coefficient de corrélations
<br><br>

***

## <ins>GNUPLOT :</ins> <br>
Pour representer nos données en graphique il nous fallait un logiciel interactifs, donc fait son apparition GNUPLOT.
<br>

Les données que nous avons trouver intéressants de mettre en avant sont les données suivantes : <br>
-Place libre vélo/voiture<br>
-Moyenne de place libre velo/voiture<br>
-Ecart type de place libre velo/voiture<br>

<ins>Les commandes utiliser pour afficher notre gnuplot est la suivantes :</ins>
```
plot "FR_MTP_COME.dat" title "Place parking" with lines, "MOYENNE_FR_MTP_COME.dat" title "place parking moyenne" with point pointsize 2,"FR_MTP_COME_VELO-result.dat" title "Place vélomag" with lines, "MOYENNE_FR_MTP_COME_VELO.dat" title "nombre Vélomag moyen libre" with point pointsize 2,"SIGMA_FR_MTP_COME_PARK.dat" title "écart type parking" with point pointsize 2,"SIGMA_FR_MTP_COME_VELO.dat" title "écart type vélomag" with point pointsize 2
```

<ins>La commande retourne : </ins>
<img src=".\picture\gnu.png">
> <ins>Observations :</ins><br>
Nous avons effectué 12 échantillons dont une par heure de 23h du soir jusqu'à 11H du matin
<br>
On observe qu'en moyenne il y'a 440 place de parking libre (voiture) et 21 place de vélomag libre, c'est à dire 21 vélo non utiliser <br>
On observe aussi que entre chaque heure il y'a un changement de 131 place de parking libre d'après l'écart type et pour le velomag un changement de 1,59 donc environ 2 donc de forte changement on lieu pour le parking voiture mais très peu pour le vélomag (environ 2 fois plus selon le pourcentage car, 131 voiture correspond environ a 15% et 2 velo à 8% selon leur place total respectifs.)<br>
On peut remarquer une forte augmentation des place libre de 0h vers 3h puis des changements moin considérable<br>

Que peut t'on en déduire d'après nos observations, nos constatation et nos calcules mais aussi, comme le prouve notre coefficient de corrélations (qui n'est pas sur le graphique mes stockers dans un fichier nommée "coefficient_corelation.dat"). On peut en déduire une faible corrélations positive (coef=0,49 environ, toujours compris entre -1 et 1).<br><br>

Mais ce n'est qu'une hypothèse, on a très peu de data sur le quel appuyez nos calculs donc cela reste incertains.


ONAY ILKER
MERENNA NATHAN
