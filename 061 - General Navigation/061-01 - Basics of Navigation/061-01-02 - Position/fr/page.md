En navigation aérienne, la **position** est définie par un système de coordonnées utilisant la latitude et la longitude. Bien que nous considérions souvent la Terre comme une sphère parfaite pour simplifier les calculs, la réalité est plus complexe et nécessite des modèles précis comme l'**ellipsoïde WGS 84** pour garantir la sécurité et l'exactitude du vol.

## Forme de la Terre et Références

La Terre n'est pas une sphère parfaite ; en raison de sa rotation, elle est légèrement aplatie aux pôles et élargie à l'équateur. Cette forme est connue sous le nom de **sphéroïde oblat** ou ellipsoïde.
*   **Sphère** : Supposée pour les calculs généraux, où 1 degré de latitude équivaut à **60 NM**.
*   **Ellipsoïde (WGS 84)** : Modèle mathématique utilisé par les systèmes comme le GPS. Ici, la longueur de 1 degré de latitude varie : elle est plus courte à l'équateur (environ 59,7 NM) et plus longue aux pôles (environ 60,3 NM).

## Latitude : Géodésique vs. Géocentrique

La latitude est mesurée comme un angle depuis l'Équateur (0°) jusqu'aux Pôles (90° N/S). Il existe deux définitions clés :
*   **Latitude Géocentrique** : C'est l'angle mesuré depuis le **centre de la Terre**.
*   **Latitude Géodésique (ou Géographique)** : C'est l'angle entre le plan équatorial et une ligne **perpendiculaire** à la surface de l'ellipsoïde au point de l'observateur. C'est la latitude utilisée sur les **cartes de navigation**.

Comme la Terre n'est pas une sphère parfaite, ces deux latitudes ne coïncident qu'à l'Équateur et aux Pôles. La différence maximale se produit près de 45° N/S.

Pour calculer le **Changement de Latitude** entre deux points :
*   S'ils sont dans le **même hémisphère**, on soustrait les angles. Par exemple : 36°42'37'' - 27°48'05'' = **8°54'32''**.
*   S'ils sont dans des **hémisphères opposés**, on les additionne.

## Longitude et Méridiens

La **longitude** est mesurée comme l'angle dans le plan équatorial entre le **Méridien de Greenwich** (Premier Méridien) et le méridien du point en question. Contrairement à la latitude, la longitude géocentrique et géodésique sont identiques car elles partagent le même sommet au centre de la Terre.

Pour calculer le changement de longitude :
*   Même hémisphère (Est/Est ou Ouest/Ouest) : Soustraire.
*   Hémisphères différents (Est/Ouest) : Additionner. Par exemple, entre 45°34'E et 09°18'W, la différence est de **54°52'**.

## Lignes de Navigation : Grand Cercle et Ligne de Route

À la surface de la Terre, nous distinguons deux types de trajectoires principales :
*   **Grand Cercle (Great Circle)** : C'est la ligne qui divise la Terre en deux moitiés égales (elle passe par le centre). Elle représente la **distance la plus courte** entre deux points. L'Équateur et tous les méridiens sont des Grands Cercles.
*   **Ligne de Route (Rhumb Line)** : C'est une ligne de **direction constante** qui coupe tous les méridiens avec le même angle. Les parallèles de latitude sont des Lignes de Route (ils coupent les méridiens à 90°).

| Caractéristique | Grand Cercle | Ligne de Route |
| :--- | :--- | :--- |
| **Définition** | Rayon égal à celui de la Terre | Coupe les méridiens au même angle |
| **Propriété Principale** | Distance la plus courte | Direction constante |
| **Exemples** | Équateur, Méridiens | Parallèles, Équateur, Méridiens |

## Écart et Effets Environnementaux

L'**Écart (Departure)** est la distance en milles nautiques (NM) le long d'un parallèle de latitude. Il est calculé avec la formule :
$$ \text{Écart} = \text{Changement de Longitude (min)} \times \cos(\text{Latitude}) $$
Par exemple, un changement de longitude de 500 NM à une latitude de 17°46' résulte en un changement de longitude d'environ **8°45'**.

Enfin, il est crucial de considérer la température dans la navigation verticale (**Baro-VNAV**). Des températures plus basses que la norme provoquent un vol de l'aéronef sur une trajectoire verticale réelle plus basse (angle moins prononcé), ce qui peut être dangereux près du terrain.
