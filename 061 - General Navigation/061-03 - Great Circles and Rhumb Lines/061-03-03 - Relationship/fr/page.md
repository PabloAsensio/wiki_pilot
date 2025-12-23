Pour comprendre la navigation, nous devons d'abord définir les deux trajectoires principales que suit un aéronef :

*   **Grand Cercle (Great Circle) :** Représente la **distance la plus courte** entre deux points à la surface de la Terre. Cependant, en raison de la convergence des méridiens, une route de grand cercle change constamment de direction (cap vrai) à mesure qu'elle avance, sauf à l'Équateur ou lorsqu'on vole directement nord-sud le long d'un méridien.
*   **Ligne de Route (Rhumb Line) :** C'est une ligne qui coupe tous les méridiens avec le **même angle**, ce qui signifie qu'elle maintient une direction constante. Bien qu'elle soit plus facile à voler avec une boussole, la distance parcourue est toujours supérieure à celle du grand cercle (sauf à l'Équateur ou sur des caps nord-sud).

## Différences Clés et Courbure
Sur une carte de projection stéréographique polaire, le Pôle est le point de tangence. Ici, les méridiens sont des lignes droites qui rayonnent depuis le pôle et les parallèles sont des cercles concentriques.

*   **Courbure :** Les lignes de route apparaissent courbes concaves vers le pôle, tandis que les grands cercles sont considérés comme des lignes presque droites près du pôle, bien qu'en réalité ils soient légèrement concaves vers le pôle dans les projections éloignées du centre.
*   **Latitude :** Plus la latitude est élevée (plus près du pôle), **moins la courbure** apparente des grands cercles sur la carte est importante.

La différence entre la route de grand cercle et la ligne de route est plus notable lorsque l'**Angle de Conversion** est plus grand.

## Convergence et Angle de Conversion
La différence angulaire entre ces deux trajectoires est régie par la **Convergence** des méridiens.

*   **Convergence :** C'est l'angle d'inclinaison entre deux méridiens à une latitude donnée. Elle est calculée comme :
    \[ \text{Convergence} = \text{Changement de Longitude} \times \sin(\text{Latitude Moyenne}) \]
*   **Angle de Conversion (CA) :** C'est la différence angulaire entre la direction du grand cercle et la ligne de route. Il équivaut à la moitié de la convergence.
    \[ \text{Angle de Conversion} = \frac{1}{2} \times \text{Convergence} \]

Comme le montre le graphique suivant, tant la convergence que l'angle de conversion augmentent significativement à mesure que nous nous éloignons de l'Équateur vers les pôles.

![Convergence et Angle de Conversion vs Latitude](../assets/Convergencia_y_Angulo_de_Conversión_vs_Latitud.png)

Par conséquent, la discordance entre voler un grand cercle ou une ligne de route est plus grande lorsque :
1.  Le **Changement de Longitude** augmente.
2.  La **Latitude Moyenne** augmente.

## Variation de la Distance
La règle générale établit que la différence de distance entre une route de grand cercle et une de ligne de route **augmente** si :
*   La latitude de la route augmente.
*   La différence de longitude entre les points augmente.

Par exemple, la différence de distance entre deux points séparés par 20° de longitude sera beaucoup plus grande à 60° de latitude qu'à 20° de latitude.

## Règle Pratique : DIID
Pour calculer les caps et corriger la trajectoire entre un grand cercle et une ligne de route, on utilise la règle mnémotechnique **D-I-I-D** pour l'hémisphère nord :

*   **D (Decrease) :** En volant vers l'**Ouest** (West), le cap du grand cercle **Diminue**.
*   **I (Increase) :** En volant vers l'**Est** (East), le cap du grand cercle **Augmente**.

| Hémisphère | Direction | Comportement du Cap (Great Circle) |
| :--- | :--- | :--- |
| **Nord** | Ouest | Diminue (Decrease) |
| **Nord** | Est | Augmente (Increase) |
| **Sud** | Ouest | Augmente (Increase) |
| **Sud** | Est | Diminue (Decrease) |

Lors de l'application de l'angle de conversion, rappelez-vous que le cap de Grand Cercle "tire" toujours vers le pôle par rapport à la Ligne de Route.
