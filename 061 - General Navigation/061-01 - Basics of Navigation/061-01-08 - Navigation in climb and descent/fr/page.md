La navigation pendant les phases de montée et de descente nécessite des calculs spécifiques pour déterminer la vitesse, le temps et la distance avec précision. Contrairement au vol de croisière en palier, où les conditions sont relativement constantes, la montée et la descente impliquent des changements continus d'altitude, ce qui affecte la **Vitesse Vraie (TAS)** et l'effet du vent. Voici les concepts et règles clés pour maîtriser ces calculs.

## Détermination du Vent et de la TAS Moyenne

Pour résoudre les problèmes de navigation dans ces phases, on n'utilise pas le vent ou la TAS d'une seule altitude, mais une moyenne représentative. Les normes d'apprentissage établissent les règles empiriques suivantes pour calculer la **Vitesse Sol (GS)** moyenne :

*   **Pour les problèmes de Montée :** On utilise la TAS et le Vent (W/V) à l'altitude correspondant à **2/3 de l'altitude de croisière** (ou 2/3 de la différence d'altitude ajoutés à la base).
*   **Pour les problèmes de Descente :** On utilise la TAS et le Vent (W/V) à l'altitude correspondant à **1/2 de l'altitude de descente** (ou la moitié de la couche à descendre).

Par exemple, si un aéronef monte du niveau de la mer (0 ft) jusqu'à **FL270** (27 000 ft), l'altitude de référence pour les calculs serait 18 000 ft ($27 000 \times 2/3$). Si la montée est entre 4 000 ft et 8 000 ft, l'altitude à utiliser serait 6 667 ft ($4 000 + 2/3 \times 4 000$).

## Calcul de la Vitesse Sol (Groundspeed)

Une fois l'altitude de référence déterminée, on doit obtenir la **Vitesse Sol (GS)**. Cela implique généralement trois étapes :

1.  **Trouver la Température :** Calculer la température standard (ISA) pour cette altitude et l'ajuster avec la déviation donnée (par exemple, ISA +5°C).
2.  **Calculer la TAS :** Utiliser un ordinateur de vol (comme l'E6B ou CRP-5) pour convertir la Vitesse Calibrée (CAS) en **Vitesse Vraie (TAS)**, en appliquant des corrections de compressibilité si la vitesse est élevée (supérieure à 300 kt).
3.  **Appliquer le Vent :** Utiliser la direction et la vitesse du vent à l'altitude de référence pour trouver la GS effective. Si des données exactes pour cette altitude ne sont pas données, on doit interpoler entre les vents donnés aux niveaux supérieurs et inférieurs.

## Gradients et Taux de Montée/Descente

Il est crucial de distinguer entre l'angle de montée/descente et la vitesse verticale.

*   **Gradient de Montée/Descente :** C'est la relation entre le changement de hauteur et la distance horizontale parcourue, généralement exprimée en pourcentage (%).
    *   Formule : $\text{Gradient (\%)} = \frac{\text{Changement de Hauteur}}{\text{Distance Horizontale}} \times 100$
*   **Taux de Montée (ROC) / Descente (ROD) :** C'est la vitesse verticale, mesurée en pieds par minute (ft/min ou fpm).

Il existe une relation directe entre le gradient, la vitesse sol et le taux vertical. Une règle pratique (basée sur la règle 1:60) pour estimer le **Taux de Descente** nécessaire est :

$$ROD (ft/min) \approx \text{Gradient (\%)} \times GS (kt)$$

Ou pour un angle de descente standard de 3 degrés :
$$ROD \approx 5 \times GS$$

Par exemple, pour une **GS** de 120 kt sur une pente de 3° (environ 5 %), le taux serait d'environ 600 fpm.

## Calcul du Temps et de la Distance

Enfin, pour déterminer combien de temps il faudra pour atteindre une altitude ou parcourir une distance pendant ces manœuvres :

*   **Temps de Montée/Descente :** On divise la différence de hauteur totale par le **Taux de Montée (ROC)** ou **Taux de Descente (ROD)** moyen.
    *   $\text{Temps} = \frac{\text{Différence de Hauteur}}{\text{Taux (fpm)}}$
*   **Distance Sol :** On multiplie la **Vitesse Sol (GS)** moyenne par le temps calculé.
    *   $\text{Distance} = GS \times \text{Temps}$

Il est fondamental de se rappeler que les altitudes et distances doivent être dans les mêmes unités pour les calculs de gradient (généralement des pieds, où 1 Mille Nautique (NM) ≈ 6 080 pieds).
