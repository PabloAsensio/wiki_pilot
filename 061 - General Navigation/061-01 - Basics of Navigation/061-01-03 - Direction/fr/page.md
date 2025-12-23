Naviguer un avion n'est pas aussi simple que de pointer le nez vers la destination et d'accélérer. Dans l'air, il existe des forces invisibles et des références changeantes qui obligent le pilote à calculer constamment sa trajectoire. Pour comprendre comment un aéronef est guidé, nous devons maîtriser trois concepts fondamentaux : les références du nord, l'effet du vent et les corrections en vol.

## 1. Les Trois Nords : Références de Direction

Pour mesurer une direction en degrés (de 0° à 360°), nous avons besoin d'un point de départ ou d'une ligne de référence. En aviation, il n'existe pas un seul "Nord", mais trois distincts :

*   **Direction Vraie (True Direction - T) :** Elle est mesurée par rapport au **Nord Géographique** (le vrai Pôle Nord). C'est la référence constante utilisée par les cartes et les cartes de navigation. Les méridiens de la Terre indiquent cette direction.
*   **Direction Magnétique (Magnetic Direction - M) :** Elle est mesurée par rapport au **Nord Magnétique**. C'est vers où pointe naturellement la boussole. Le problème est que le Nord Magnétique n'est pas au même endroit que le Nord Géographique et se déplace avec le temps.
*   **Direction Compas (Compass Direction - C) :** C'est ce que le pilote lit réellement sur son instrument à bord. Elle ne coïncide souvent pas exactement avec le Nord Magnétique en raison des interférences métalliques et électriques de l'avion lui-même.

## 2. Les Erreurs : Variation et Déviation

Pour pouvoir naviguer, le pilote doit convertir les données de la carte (Vrai) en ce qu'il voit dans son cockpit (Compas). Pour cela, deux corrections angulaires sont appliquées :

*   **Variation (Variation) :** C'est la différence angulaire entre le Nord Vrai et le Nord Magnétique. Elle dépend de la zone géographique dans laquelle nous volons.
    *   Sur les cartes, les lignes qui relient les points avec la même variation sont appelées **lignes isogones**. Si la variation est nulle, on l'appelle **ligne agonique**.
*   **Déviation (Deviation) :** C'est l'erreur spécifique de la boussole de l'avion causée par les champs magnétiques de l'aéronef (moteur, radios). Chaque avion a une **carte de déviation** qui indique cette erreur.

**Règle d'Or pour les Conversions :**
Pour passer d'une référence à une autre, on utilise des règles mnémotechniques :
*   **Variation West, Magnetic Best :** Si la variation est à l'Ouest, le cap Magnétique est supérieur (meilleur) au Vrai.
*   **Variation East, Magnetic Least :** Si la variation est à l'Est, le cap Magnétique est inférieur au Vrai.
*   La même règle s'applique pour la Déviation entre Magnétique et Compas (*Deviation West, Compass Best*).

## 3. Cap vs. Route : L'Effet du Vent

C'est ici qu'intervient la physique du vol. Il y a une grande différence entre où "regarde" l'avion et où il "va" réellement.

*   **Cap (Heading) :** C'est la direction vers laquelle pointe le nez de l'avion.
*   **Route (Track) :** C'est le chemin réel que l'avion dessine sur le sol (**Track Made Good**).

S'il n'y avait pas de vent, le Cap et la Route seraient identiques. Mais le vent pousse généralement l'avion de côté.
*   **Dérive (Drift) :** C'est l'angle que le vent dévie l'avion de son cap.
*   **Angle de Correction de Vent (WCA) :** Pour contrer la dérive, le pilote doit tourner l'avion contre le vent. Si le vent pousse de 10° vers la droite, le pilote doit virer de 10° vers la gauche pour rester sur la ligne droite.

De plus, le vent se décompose en deux forces :
*   **Vent Traversier (Crosswind) :** Pousse latéralement (calculé avec le sinus de l'angle).
*   **Vent de Face/Arrière (Headwind/Tailwind) :** Affecte la vitesse à laquelle nous avançons sur le sol (calculé avec le cosinus).

## 4. Corrections en Vol : La Règle de 1 en 60

Malgré une bonne planification, il est normal de dévier. Pour revenir sur la route, les pilotes utilisent des calculs mentaux basés sur la géométrie, connus sous le nom de **Règle de 1 en 60**. Cette règle dit qu'une erreur de 1 degré nous dévie de 1 mille nautique après avoir volé 60 milles.

Lorsqu'un pilote remarque qu'il s'est écarté de la route, il calcule deux valeurs :
1.  **Erreur de Route (TKE - Track Error Angle) :** Combien de degrés il s'est écarté de la route d'origine.
2.  **Angle de Fermeture (Closing Angle) :** Combien de degrés supplémentaires il doit tourner pour intercepter à nouveau la route avant d'arriver à destination.

La somme de ces angles lui indique combien il doit corriger le cap pour arriver en toute sécurité à sa destination.

## 5. Limitations de la Boussole

Enfin, il est important de savoir que la boussole n'est pas parfaite. Elle fonctionne en détectant la composante horizontale du champ magnétique terrestre. Près des Pôles Magnétiques, les lignes de champ entrent verticalement dans la Terre (**Dip**), rendant la force horizontale très faible. C'est pourquoi, aux latitudes polaires, la boussole devient inutile et il faut naviguer en utilisant des références vraies ou inertielles.
