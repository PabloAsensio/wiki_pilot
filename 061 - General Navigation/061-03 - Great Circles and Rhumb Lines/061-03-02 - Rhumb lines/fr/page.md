Dans la navigation globale, il est crucial de comprendre comment les lignes sont tracées sur la surface courbe de la Terre. Les deux concepts les plus importants qui définissent ces trajectoires sont la **Loxodromie** (Rhumb Line) et l'**Orthodromie** (Great Circle).

## Qu'est-ce qu'une Loxodromie ?
Une **Loxodromie** (ou *Rhumb Line*) est une ligne sur la surface de la Terre qui **coupe tous les méridiens avec le même angle**. Cela signifie que c'est une ligne de **direction constante**. Pour un pilote ou navigateur, suivre une loxodromie est pratique car elle permet de maintenir un cap fixe sur la boussole sans avoir à l'ajuster continuellement.

Visuellement, une loxodromie a une caractéristique géométrique unique : **elle forme une spirale vers le Pôle le plus proche**, sauf si sa direction est Nord, Sud, Est ou Ouest vrai.
*   **Cas Spéciaux :**
    *   Les **Parallèles de latitude** sont des loxodromies car ils coupent tous les méridiens à 90°.
    *   Les **Méridiens** et l'**Équateur** sont des loxodromies car ils maintiennent une direction constante (Nord-Sud ou Est-Ouest) et sont aussi des Grands Cercles.

## Qu'est-ce qu'une Orthodromie ?
Un **Grand Cercle** (ou *Great Circle*) est un cercle tracé sur la surface de la Terre dont le centre et le rayon coïncident avec ceux de la sphère terrestre. C'est la plus grande intersection possible qu'on peut obtenir sur une sphère.
Ses propriétés clés sont :
*   Il représente la **distance la plus courte** entre deux points sur la surface terrestre.
*   Il n'existe qu'un seul Grand Cercle entre deux points (sauf s'ils sont antipodaux).
*   Sa direction change continuellement par rapport aux méridiens (ce n'est pas une ligne de cap constant).

## Relation entre Loxodromie et Orthodromie

Bien que l'orthodromie offre la route la plus courte, la direction change constamment, ce qui est difficile à voler manuellement. La loxodromie est plus longue mais plus facile à suivre.
La relation positionnelle entre les deux est fixe :

*   La **Loxodromie** se trouve toujours du côté **équatorial** de l'orthodromie équivalente.
*   L'**Orthodromie** se trouve toujours du côté **polaire** (plus près du pôle) de la loxodromie.

Sur une carte, la différence angulaire entre la route orthodromique et celle de la loxodromie s'appelle **Angle de Conversion**, qui est égal à la moitié de la **Convergence**.

## Calculs de Navigation

Pour convertir entre ces caps, des formules spécifiques sont utilisées :

1.  **Convergence** : Elle est calculée en multipliant le changement de longitude par le sinus de la latitude moyenne.
    *   *Formule : Convergence = Changement de Longitude × Sinus (Latitude Moyenne)*
2.  **Angle de Conversion** : C'est la moitié de la convergence.
    *   *Formule : Angle de Conversion = ½ Convergence*

**Exemple Pratique :**
Si nous volons entre deux points dans l'hémisphère nord avec une latitude moyenne de 55°N et un changement de longitude de 10° :
*   Convergence = 10° × Sin(55°) ≈ 8°.
*   Angle de Conversion = 4°.
Le cap de loxodromie sera la somme (ou soustraction, selon le sens) du cap initial d'orthodromie et de cet angle de conversion. Au point milieu de la route, le cap de la loxodromie et celui de l'orthodromie sont **parallèles**.

## Résumé des Propriétés

| Caractéristique | Loxodromie (Rhumb Line) | Orthodromie (Great Circle) |
| :--- | :--- | :--- |
| **Définition** | Ligne de **direction constante** qui coupe les méridiens au même angle. | Cercle avec le même centre et rayon que la Terre. |
| **Avantage** | Facile à naviguer (cap fixe). | **Distance la plus courte** entre deux points. |
| **Trajectoire** | Se courbe en spirale vers le pôle. | Cercle direct autour de la sphère. |
| **Relation** | Se situe vers l'**Équateur**. | Se situe vers le **Pôle**. |
| **Exemples** | Méridiens, Équateur, Parallèles. | Méridiens, Équateur. |
