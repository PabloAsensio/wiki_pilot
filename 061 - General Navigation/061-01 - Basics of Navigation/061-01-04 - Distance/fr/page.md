En navigation aérienne, la distance n'est pas seulement une mesure linéaire ; c'est une combinaison de géométrie sphérique, de mouvement des masses d'air et de calculs de temps. Voici tous les concepts essentiels pour comprendre comment les trajets sont mesurés autour du monde.

## 1. La Forme de la Terre et l'Unité de Base
Bien que pour de nombreux calculs nous supposions que la Terre est une sphère parfaite, en réalité c'est un **Sphéroïde Oblat** (aplati aux pôles). Cela signifie que le rayon de courbure change légèrement :
*   Un **Mille Nautique (NM)** est historiquement défini comme la longueur de **1 minute d'arc de méridien**.
*   En raison de l'aplatissement, un mille nautique réel est un peu plus long aux **Pôles** (environ 1862 m) et un peu plus court à l'**Équateur** (environ 1844 m).
*   Cependant, pour normaliser, l'OACI définit le Mille Nautique exactement comme **1 852 mètres**.

## 2. Navigation du Nord au Sud (Latitude)
Les **parallèles de latitude** sont des lignes qui courent d'Est en Ouest, mais elles sont utilisées pour mesurer à quel point nous sommes au Nord ou au Sud. La distance entre eux est constante.
*   **Règle d'Or :** **1 minute de latitude = 1 NM**. Par conséquent, **1 degré de latitude = 60 NM**.
*   **Calcul :** Pour trouver la distance entre deux points sur le même méridien :
    *   S'ils sont dans le **même hémisphère**, **soustraire** les latitudes.
    *   S'ils sont dans des **hémisphères différents**, **additionner** les latitudes.
    *   Multiplier la différence en degrés par 60 pour obtenir les milles.

## 3. Navigation d'Est en Ouest (Écart)
C'est ici qu'intervient la **convergence des méridiens**. Les lignes de longitude se rejoignent aux pôles. Par conséquent, la distance physique de 1 degré de longitude varie selon l'endroit où vous êtes. La distance réelle parcourue le long d'un parallèle est appelée **Écart (Departure)**.
*   **Formule :** **Écart (NM) = Changement de Longitude (en minutes) × Cosinus de la Latitude**.
*   À une latitude plus élevée (plus près du pôle), la distance pour un même changement de degrés est moindre.
*   Sur les cartes **Lambert**, bien que la distance en NM diminue avec la latitude, la distance "angulaire" (degrés d'arc) reste constante.

## 4. Milles Aériens (NAM) vs. Milles Terrestres (NGM)
Un avion se déplace dans une masse d'air.
*   **NAM (Nautical Air Miles) :** Distance parcourue par rapport à l'air. Dépend de la **TAS (True Air Speed)**.
*   **NGM (Nautical Ground Miles) :** Distance parcourue sur le sol. Dépend de la **GS (Ground Speed)**.

**L'Effet du Vent :**
*   **Vent de Face :** La GS est inférieure à la TAS. L'avion vole plus de distance aérienne (NAM) que terrestre (NGM).
*   **Vent Arrière :** La GS est supérieure à la TAS. L'avion couvre plus de terrain (NGM) avec moins "d'effort" aérien (NAM).
*   **La Plus Grande Différence :** Se produit en volant à **haute altitude avec des vents de face forts**, car la différence entre TAS et GS est plus prononcée.

**Formule de Conversion :**
$$ \text{NAM} = \text{NGM} \times \frac{\text{TAS}}{\text{GS}} $$

## 5. Rencontres et Vitesse de Fermeture
Lorsque deux avions volent l'un vers l'autre sur la même route, quand se rencontreront-ils ?
*   On additionne leurs vitesses (**Vitesse de fermeture**).
*   **Temps jusqu'à la rencontre = Distance Totale / (Vitesse A + Vitesse B)**.
*   Ceci est utile pour calculer les points de rencontre sur les routes océaniques ou polaires.

## 6. Calculs Verticaux (Montée et Descente)
Pour planifier des descentes ou des montées efficaces :
*   **Distance Horizontale :** Calculée en utilisant la **vitesse sol moyenne** pendant la manœuvre multipliée par le temps de la manœuvre.
*   **Taux de Descente (ROD) :** Pour maintenir une trajectoire de descente de **3 degrés**, multipliez votre Vitesse Sol (GS) par 5.
    *   *Exemple :* Avec 140 kts de GS, vous avez besoin d'environ 700 pieds/min de descente.

## 7. Routes Polaires et Orthodromiques
La distance la plus courte entre deux points sur une sphère est le **Grand Cercle** (Orthodromie).
*   **Cas Spécial (180° de différence) :** Si deux points sont sur le même parallèle mais séparés par 180° de longitude (côtés opposés de la Terre), la route la plus courte n'est pas de suivre le parallèle, mais de voler **par le Pôle**.
*   **Calcul Polaire :** On calcule la distance du point A au Pôle (90° - Latitude) et on ajoute la distance du Pôle au point B.

## 8. Utilisation du Radar pour la Distance
Bien qu'aujourd'hui nous utilisions le GPS, le **Radar Météo (AWR)** a un "Mode Cartographique" (Mapping).
*   En inclinant l'antenne vers le bas, le radar peut détecter les contrastes dans le terrain comme les **côtes, les montagnes ou les villes**.
*   Cela permet au pilote de confirmer sa position ou d'estimer les distances à des références géographiques si d'autres systèmes échouent.

## 9. Conversions Rapides
*   **m/s à km/h :** Multiplier par 3,6 (ou utiliser l'ordinateur de vol).
*   **Km à NM :** Diviser les km par **1,852** (ou multiplier par environ 0,54).
*   **Arc à Temps :** La Terre tourne de 15° de longitude par heure.

Maîtriser ces concepts permet au pilote non seulement de suivre une ligne magenta sur un écran, mais de comprendre la physique de son mouvement sur la planète, optimisant le carburant et le temps.
