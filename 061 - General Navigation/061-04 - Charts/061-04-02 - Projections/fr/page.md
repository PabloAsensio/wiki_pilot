Naviguer dans le monde nécessite de traduire une sphère tridimensionnelle (la Terre) sur une carte plane bidimensionnelle. Ce processus se réalise au moyen de **projections**, et chacune a ses propres règles et distorsions. Voici une explication simple du fonctionnement des principales projections utilisées en aviation, intégrant tous les concepts théoriques et mathématiques essentiels.

## Concepts Fondamentaux de Navigation

Avant d'étudier les cartes, nous devons comprendre comment se comportent les lignes et les angles sur la surface terrestre :

*   **Orthodromie (Great Circle) :** C'est la distance la plus courte entre deux points sur une sphère. Sa direction change constamment à mesure que nous traversons les méridiens. Sur la plupart des cartes, nous cherchons à ce que ces routes apparaissent comme des lignes droites.
*   **Loxodromie (Rhumb Line) :** C'est une ligne qui maintient une direction constante, coupant tous les méridiens avec le même angle. Elle est facile à voler (il suffit de suivre un cap fixe sur la boussole), mais ce n'est pas la route la plus courte. Sur les cartes polaires, c'est une courbe concave vers le pôle.
*   **Convergence (Convergency) :** C'est l'angle d'inclinaison entre deux méridiens. Sur la Terre, les méridiens se rejoignent aux pôles.
    *   Formule : **Convergence = Changement de Longitude × Sinus (Latitude Moyenne)**.
*   **Angle de Conversion :** C'est la différence angulaire entre la direction de l'Orthodromie et la Loxodromie.
    *   Règle clé : **Angle de Conversion = ½ Convergence**.

***

## 1. Projection Stéréographique Polaire

Cette carte est créée en imaginant un plan plat qui touche la Terre à l'un des Pôles (point de tangence). Elle est idéale pour la navigation aux hautes latitudes.

*   **Graticule (Réseau Géographique) :** Les **méridiens** sont des lignes droites qui rayonnent depuis le pôle. Les **parallèles** sont des cercles concentriques dont la distance augmente en s'éloignant du pôle.
*   **Facteur de Convergence (n=1) :** Sur cette carte, la convergence est maximale et identique à la réalité polaire.
    *   **Convergence de Carte = Changement de Longitude**.
*   **Comportement des Routes :**
    *   Une ligne droite tracée passant par le pôle est un méridien.
    *   Les **Orthodromies** (grands cercles) sont presque droites près du pôle, mais techniquement ce sont des courbes légèrement concaves vers le pôle.
    *   Les **Loxodromies** sont des courbes prononcées, toujours concaves vers le pôle de projection.
*   **Échelle :** Elle est correcte seulement au Pôle. Elle s'agrandit à mesure que nous nous éloignons (proportionnelle à la sécante au carré de la moitié de la co-latitude).

***

## 2. Projection Conique Conforme de Lambert

C'est la carte standard pour l'aviation aux latitudes moyennes. On utilise un cône qui "coupe" la Terre, l'intersectant sur deux **Parallèles Standards**.

*   **Parallèle d'Origine :** C'est la latitude centrale mathématique de la projection, située à mi-chemin entre les deux parallèles standards. Ici la convergence de la carte est égale à la convergence de la Terre.
    *   Calcul : *(Parallèle Standard 1 + Parallèle Standard 2) / 2*.
*   **Constante du Cône (n) :** Définit à quel point le cône a été "aplati" (0 est un cylindre, 1 est un plan).
    *   **Constante du Cône = Sinus (Parallèle d'Origine)**.
*   **Convergence de Carte :** Elle est constante sur toute la carte.
    *   **Convergence = Changement de Longitude × Constante du Cône**.
*   **Échelle :** Elle est exacte sur les parallèles standards. Elle se **contracte** (se réduit) entre eux (minimale au parallèle d'origine) et **s'agrandit** (augmente) en dehors d'eux. L'erreur d'échelle est généralement maintenue inférieure à **1 %**.
*   **Orthomorphe :** Oui, comme toutes les cartes de navigation, elle préserve les angles et les formes dans les petites zones.

***

## 3. Projection Mercator Directe

C'est une projection cylindrique où le cylindre enveloppe la Terre en touchant l'**Équateur** (son parallèle d'origine).

*   **Graticule :** Les **méridiens** sont des lignes droites parallèles et espacées uniformément. Les **parallèles** sont des lignes droites parallèles qui s'écartent davantage à mesure qu'elles s'éloignent de l'Équateur.
*   **Convergence Zéro :** Comme les méridiens sont parallèles, ils ne se touchent jamais. La convergence de la carte est nulle.
*   **Routes :**
    *   Les **Loxodromies** sont des lignes droites parfaites (son grand avantage).
    *   Les **Orthodromies** sont des courbes convexes vers le pôle (concaves à l'Équateur).
*   **Échelle Variable :** L'échelle est correcte seulement à l'Équateur et augmente rapidement vers les pôles (comme la sécante de la latitude).
*   **La Formule "ABBA" :** Pour calculer les distances ou les échelles à différentes latitudes en Mercator, nous utilisons cette relation mathématique :
    *   **Distance A × Cos(Latitude B) = Distance B × Cos(Latitude A)**.

***

## Règles Pratiques de Direction

Pour résoudre les problèmes de direction entre deux points (A et B) :

1.  **Calculer la Convergence :** Selon la projection (Changement de Longitude pour Polaire ; Changement de Longitude × Sinus de Latitude pour Lambert).
2.  **Calculer l'Angle de Conversion :** Diviser la convergence par 2.
3.  **Appliquer la Règle de l'Hémisphère :**
    *   L'**Orthodromie** est toujours plus proche du Pôle que la Loxodromie.
    *   Sur une carte Lambert ou Polaire, l'Orthodromie est la ligne la plus droite ; la Loxodromie se courbe vers l'équateur.
    *   **GCT (Cap Orthodromique) = RLT (Cap Loxodromique) ± Angle de Conversion**.