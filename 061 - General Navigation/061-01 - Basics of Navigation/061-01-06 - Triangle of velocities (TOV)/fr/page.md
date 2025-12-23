Naviguer un avion est très différent de conduire une voiture. Alors qu'une voiture adhère fermement à la route, un avion se déplace dans une masse d'air qui, elle-même, se déplace sur la terre. Pour comprendre où va réellement l'avion et à quelle vitesse, les pilotes utilisent un concept fondamental appelé **Triangle des Vitesses**.

Voici une explication simple de comment ces forces fonctionnent et comment les pilotes les calculent pour arriver à destination avec précision.

## Les Trois Vecteurs Fondamentaux

Pour résoudre tout problème de navigation, nous devons visualiser trois forces ou **vecteurs** interagissant entre eux. Un vecteur est simplement une flèche qui nous indique une direction et une intensité (vitesse).

1.  **Vecteur Air (Air Vector) :** Représente le mouvement de l'avion à travers l'air. Il est composé de :
    *   **Cap Vrai (True Heading - TH) :** La direction vers laquelle pointe le nez de l'avion.
    *   **Vitesse Vraie (True Airspeed - TAS) :** La vitesse réelle de l'avion par rapport à l'air qui l'entoure.

2.  **Vecteur Vent (Wind Vector - W/V) :** Représente le mouvement de la masse d'air sur la terre. Il est défini par sa direction (d'où il souffle) et sa vitesse (intensité en nœuds).

3.  **Vecteur Sol (Ground Vector) :** C'est le résultat final ; ce que l'avion fait réellement sur la carte. Il est composé de :
    *   **Route (True Track - TT) :** La ligne réelle que l'avion trace sur le sol.
    *   **Vitesse Sol (Ground Speed - GS) :** La vitesse à laquelle l'avion se déplace sur le terrain.

### La Somme des Vecteurs
Le principe physique derrière cela est la **somme vectorielle**. Imaginez que vous marchez vers l'avant sur un tapis roulant qui se déplace de côté. Votre mouvement final est une diagonale. En aviation, pour additionner ces vecteurs, nous plaçons la queue du **Vecteur Vent** à la tête (pointe) du **Vecteur Air** ; le résultat, du début à la fin, est le **Vecteur Sol**.

## Concepts de Navigation Pratique

### Dérive et Correction
Lorsque le vent souffle de côté, il pousse l'avion hors de sa route souhaitée.
*   **Dérive (Drift) :** C'est l'angle de différence entre où pointe l'avion (Cap) et où il va réellement (Route). Si le vent vient de la droite, il nous poussera vers la gauche, créant une dérive à gauche.
*   **Angle de Correction de Vent (WCA) :** Pour contrer la dérive, le pilote doit "pointer" l'avion vers le vent. Si le vent vous pousse de 10° vers la gauche, vous devez virer de 10° vers la droite pour compenser.

### Composantes du Vent
Le vent souffle rarement exactement de face ou arrière ; il vient généralement en angle. Les pilotes divisent ce vent en deux effets :
*   **Vent de Face/Arrière (Headwind/Tailwind) :** Affecte la vitesse à laquelle vous avancez sur le sol (Ground Speed).
*   **Vent Traversier (Crosswind - XWC) :** Est responsable de pousser l'avion latéralement (Dérive) et est critique pendant l'atterrissage.

## Outils de Calcul

### L'Ordinateur de Vol (CRP-5 / E6-B)
Les pilotes utilisent un calculateur mécanique circulaire pour résoudre ce triangle. Il existe une règle d'or pour marquer le vent sur le disque selon les données dont vous disposez :
*   Si vous connaissez le **Cap (Heading)**, marquez le vent vers le **BAS** depuis le centre du disque.
*   Si vous connaissez la **Route (Track)**, marquez le vent vers le **HAUT** depuis le centre.

### Calcul Mental (MDR - Mental Dead Reckoning)
En vol, il n'y a parfois pas le temps d'utiliser l'ordinateur. Il existe des astuces mathématiques rapides :

*   **Règle de l'Horloge (Clock Code) pour le Vent Traversier :**
    Sert à estimer combien de vent traversier nous avons selon l'angle du vent :
    *   **15°** de différence : Équivaut à 1/4 de la force du vent (25 %).
    *   **30°** de différence : Équivaut à une demi-heure, c'est-à-dire la moitié de la force (50 %).
    *   **45°** de différence : Équivaut à 3/4 de la force (75 %).
    *   **60°** ou plus : Considéré comme affectant à 100 %.

*   **Règle 1:60 pour la Dérive :**
    Pour savoir de combien de degrés le vent corrige, on utilise la formule :
    $$ \text{Angle} = \frac{\text{Vent Traversier} \times 60}{\text{TAS}} $$
    Cela nous dit rapidement combien de degrés nous devons virer pour maintenir la route.

## Préparation des Données

Avant de calculer, les données doivent être cohérentes :
1.  **De CAS à TAS :** L'indicateur de vitesse dans le cockpit (Calibrated Airspeed - CAS) n'est pas parfait. Il doit être corrigé pour l'altitude et la température pour obtenir la **Vitesse Vraie (TAS)**. Parfois, cela implique de convertir d'abord un Nombre de Mach en TAS.
2.  **Magnétique vs. Vrai :** Les cartes et la météorologie utilisent des références différentes. Le vent est généralement donné par rapport au **Nord Vrai**, tandis que les boussoles utilisent le **Nord Magnétique**. Il est vital d'appliquer correctement la **Déclinaison Magnétique (Variation)** (en ajoutant ou soustrayant selon qu'elle est Est ou Ouest) avant de mélanger les données.
