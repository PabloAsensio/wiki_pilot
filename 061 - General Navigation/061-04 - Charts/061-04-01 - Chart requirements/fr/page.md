Les cartes aéronautiques sont des représentations fondamentales pour la navigation aérienne, agissant comme une "Terre réduite" sur un plan. Leur fonction principale est de montrer la relation entre les distances sur la carte et les distances réelles sur la planète, permettant aux pilotes de planifier et d'exécuter des vols avec précision. Voici les concepts clés pour comprendre leur fonctionnement.

## L'Échelle de la Carte

L'**échelle de la carte** est la relation entre une longueur mesurée sur la carte et la distance correspondante sur la Terre. Elle s'exprime par la formule :

**Échelle = Distance sur la Carte / Distance sur la Terre**

Pour comparer les échelles, on utilise une règle simple basée sur le dénominateur de la fraction représentative :
*   **À plus grand dénominateur, plus petite échelle** : Couvre plus de surface mais avec moins de détails (ex. 1:2 000 000).
*   **À plus petit dénominateur, plus grande échelle** : Couvre moins de surface mais avec plus de détails (ex. 1:500 000).

Par exemple, lors du calcul de l'échelle à une latitude de 45°N où 6 cm sur la carte représentent 1 degré de longitude, on obtient une échelle approximative de **1:1 309 562**. Il est crucial de se rappeler de convertir toutes les mesures dans la même unité (comme les centimètres) avant d'effectuer le calcul.

## Calcul des Distances (Écart)

Pour déterminer la distance réelle entre deux méridiens à une latitude spécifique, on utilise la formule d'**écart (departure)**. Comme les méridiens convergent vers les pôles, la distance entre eux diminue à mesure que la latitude augmente.

**Écart (NM) = Changement de Longitude x 60 x cos(latitude)**

Cette formule permet de calculer la distance en Milles Nautiques (NM) qui sépare deux points de longitude différente situés sur le même parallèle.

## Projections Cartographiques

Il existe différentes façons de projeter la surface sphérique de la Terre sur un plan, chacune avec ses propres caractéristiques.

### Projection Conique Conforme de Lambert
Dans cette projection, l'échelle est exacte seulement sur les **parallèles standards**. Ses caractéristiques principales sont :
*   L'échelle diminue entre les parallèles standards et augmente en dehors d'eux.
*   La **convergence de la carte** est constante et se calcule en multipliant le changement de longitude par le sinus du parallèle d'origine (connu comme la "constante du cône").
*   Une ligne droite sur cette carte approxime un **grand cercle**, ce qui est idéal pour la navigation radio.

### Projection Mercator
C'est une projection cylindrique où l'échelle s'agrandit à mesure que nous nous éloignons de l'Équateur.
*   L'expansion de l'échelle est proportionnelle à la sécante de la latitude.
*   Pour résoudre les problèmes d'échelle en Mercator, on utilise la relation : **Dénominateur A x cos(Lat B) = Dénominateur B x cos(Lat A)**.

## Convergence et Orthomorphisme

Une propriété essentielle des cartes de navigation est l'**orthomorphisme** (ou conformité), qui garantit que les angles mesurés sur la carte sont égaux aux angles sur la Terre. Cela assure que les caps de navigation sont corrects.

*   **Convergence de la Carte** : C'est l'angle d'inclinaison entre les méridiens sur la carte.
*   **Convergence de la Terre** : C'est l'angle réel d'inclinaison des méridiens sur la planète.
*   **Angle de Conversion** : C'est la différence angulaire entre le grand cercle (route la plus courte) et la ligne de route (loxodromique). Il se calcule comme la moitié de la convergence.

## Application Pratique : Vitesse et Temps

L'utilisation correcte de l'échelle permet de calculer la **Ground Speed (GS)** ou vitesse sol. Si nous connaissons la distance sur la carte et le temps qu'il faut pour la parcourir, nous convertissons d'abord la distance de la carte en distance terrestre en utilisant l'échelle, puis nous appliquons la formule :

**GS = Distance Terrestre / Temps de Vol**

Par exemple, si nous mesurons 13,8 cm sur une carte avec une échelle où 1 cm équivaut à 3,1 NM, la distance réelle est de 42,78 NM. Si nous volons ce segment en 15 minutes, notre vitesse sol serait de 171 nœuds.
