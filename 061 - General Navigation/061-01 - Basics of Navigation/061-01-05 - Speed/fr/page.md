Dans le monde de l'aviation, la "vitesse" n'est pas un nombre unique comme dans une voiture. Pour qu'un avion vole en toute sécurité et arrive à l'heure, les pilotes doivent gérer et calculer différents types de vitesses, en tenant compte de facteurs tels que l'altitude, la température et le vent. Voici ces concepts fondamentaux expliqués.

## Les Types de Vitesse

Pour comprendre comment un avion se déplace et comment les instruments réagissent, nous devons distinguer cinq définitions clés :

1.  **Indicated Airspeed (IAS) :** C'est la lecture directe de l'instrument (anémomètre) sans correction.
2.  **Calibrated Airspeed (CAS) :** C'est l'IAS corrigée pour les erreurs d'instrument et d'installation. Elle mesure la **pression dynamique**, c'est-à-dire la force avec laquelle l'air frappe l'avion. C'est la vitesse critique pour le contrôle de l'aéronef (comme éviter le décrochage).
3.  **Equivalent Airspeed (EAS) :** C'est la CAS corrigée pour la **compressibilité** de l'air. À vitesses élevées et grandes altitudes, l'air se comprime devant le tube pitot, faussant la lecture. L'EAS est fondamentale pour les calculs d'ingénierie et d'aérodynamique à haute vitesse.
4.  **True Airspeed (TAS) :** C'est la **vitesse vraie** de l'avion à travers la masse d'air (c'est l'EAS corrigée pour la densité). À mesure que nous montons, l'air est moins dense. Pour maintenir la même pression dynamique (CAS/EAS), l'avion doit physiquement voler plus vite. C'est pourquoi, en altitude, la **TAS** est significativement supérieure à la **CAS**.
5.  **Ground Speed (GS) :** C'est la vitesse par rapport au sol. C'est le résultat de prendre la **TAS** et d'y ajouter ou soustraire l'effet du vent. C'est la seule vitesse que nous utilisons pour savoir combien de temps il faudra pour arriver à destination.

De plus, il existe le **Nombre de Mach**, qui est le rapport entre la vitesse de l'avion (TAS) et la vitesse locale du son (**LSS**). C'est la référence principale pour les vols à haute altitude.

## Relation entre Altitude, Température et Vitesse

L'environnement change à mesure que l'avion monte, ce qui affecte les vitesses de diverses manières :

*   **La Règle des 2 %** : Comme règle générale rapide, la **TAS** augmente d'environ **2 %** par rapport à la **CAS** pour chaque **1 000 pieds** d'altitude. Par exemple, à 10 000 pieds, votre vitesse réelle est 20 % supérieure à celle indiquée sur l'instrument.
*   **Température et Son :** La vitesse du son (**LSS**) dépend uniquement de la **température absolue** (Kelvin). Le son voyage plus lentement dans l'air froid. La formule est **LSS = 38,95 × √Température(K)**. Comme il fait plus froid à des altitudes plus élevées, la vitesse du son diminue, ce qui fait augmenter le **Nombre de Mach** même si nous maintenons la même TAS.

### Comportement en Montée et Descente (Graphiques ECTM)
Il existe une relation stricte entre **EAS**, **CAS**, **TAS** et **Mach** lors des changements de niveau. Un outil utile est les graphiques **ECTM** (EAS, CAS, TAS, Mach) :
*   Si nous montons en maintenant une **CAS constante**, tant la **TAS** que le **Mach** augmentent.
*   Si nous montons en maintenant un **Mach constant**, tant la **TAS** que la **CAS** diminuent.
*   Si nous descendons à **Mach constant**, tant la **TAS** que la **CAS** augmentent.

## L'Effet du Vent

L'air dans lequel vole l'avion se déplace par rapport au sol :

*   **Vent de Face (Headwind) :** Soustrait de la vitesse. **GS = TAS - Vent**.
*   **Vent Arrière (Tailwind) :** Ajoute à la vitesse. **GS = TAS + Vent**.
*   **Vent Traversier (Crosswind) :** Pousse l'avion de côté.

Pour voler en ligne droite sur le sol (**Track**), le pilote doit pointer le nez de l'avion (**Heading**) vers le vent pour contrer la poussée latérale. La différence angulaire entre le Heading et le Track s'appelle **Dérive (Drift)**.

## Calculs Pratiques en Vol

Les pilotes utilisent des outils comme l'**ordinateur de vol (Flight Computer)** pour résoudre des problèmes mathématiques en vol :

*   **Distance et Temps :** La formule de base est **Vitesse = Distance / Temps**. Si nous arrivons en retard à un point de contrôle, nous devons augmenter la **Ground Speed** pour rattraper le temps perdu.
*   **Taux de Descente :** Pour descendre confortablement vers la piste (généralement avec un angle de 3°), on utilise une règle mentale : Multipliez votre **Ground Speed par 5**. Si vous volez à 120 nœuds sur le sol, vous devez descendre à **600 pieds par minute**.
*   **Gestion du Carburant :** Le carburant est consommé par heure de vol. Si nous avons beaucoup de vent de face, notre **GS** diminue, nous mettrons plus de temps à arriver et, par conséquent, nous aurons besoin de plus de carburant pour parcourir la même distance.
