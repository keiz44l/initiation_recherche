# Analyse expérimentale et benchmarking de modèles et algorithmes d’IA

## Prérequis
```bash	
pip install numpy
pip install matplotlib
pip install statsmodels
```
La plupart du code a été réalisé sous forme de Jupyter Notebook, et une partie a été réalisée en Python. La version de Python utilisée est la 3.10.5.

## Introduction

Ce projet a pour objectif de comparer les performances de différents modèles et algorithmes d'intelligence artificielle sur 10 fonctions séparées en 5 classes. Les classes sont les suivantes :
- Fonctions séparables
- Fonctions à conditionnement faible ou modéré
- Fonctions à conditionnement fort et unimodales
- Fonctions multimodales avec structure globale
- Fonctions multimodales avec structure globale faible

## Arborescence et fichiers

- **Algorithmes** : Contient les algorithmes utilisés pour comparer les performances, les données tdata et une fonction globale permettant de sauvegarder en png les résultats obtenus dans les dossiers ECDF, Instances et Median.

- **Separable** : Contient les notebooks liés aux fonctions séparables, ainsi qu'un dossier Pictures contenant les images des résultats obtenus, et un dossier Tables contenant les résultats obtenus sous forme de tableau.
- **Low or moderate conditioning** : Contient les notebooks liés aux fonctions à conditionnement faible ou modéré, ainsi qu'un dossier Pictures contenant les images des résultats obtenus, et un dossier Tables contenant les résultats obtenus sous forme de tableau.
- **High conditioning and unimodal** : Contient les notebooks liés aux fonctions à conditionnement fort et unimodales, ainsi qu'un dossier Pictures contenant les images des résultats obtenus, et un dossier Tables contenant les résultats obtenus sous forme de tableau.
- **Multimodal with global structure** : Contient les notebooks liés aux fonctions multimodales avec structure globale, ainsi qu'un dossier Pictures contenant les images des résultats obtenus, et un dossier Tables contenant les résultats obtenus sous forme de tableau.
- **Multimodal with weak global structure** : Contient les notebooks liés aux fonctions multimodales avec structure globale faible, ainsi qu'un dossier Pictures contenant les images des résultats obtenus, et un dossier Tables contenant les résultats obtenus sous forme de tableau.


## Utilisation
Si vous souhaitez étudier chaque algorithme, vous pouvez lancer le fichier python de chaque algorithme (eg: *borg_instances.py*), ce qui va sauvegarder les résultats sous forme de graphiques dans les trois dossiers correspondants.\
Si vous souhaitez étudier quel algorithme est le plus performant selon votre budget et votre classe de fonctions, vous pouvez lancer les notebooks correspondants à chaque classe de fonctions, ce qui va générer des graphiques et des tableaux comparatifs des performances des algorithmes.


## Modèles et algorithmes

Les modèles et algorithmes suivants ont été utilisés pour comparer les performances :
- Random Search 5 : Témoin de base
- Borg Adaptative
- RM-MEDA

## Lien avec le rapport

La partie **5. MÉTHODES UTILISÉES ET OBSERVATION** est liée à **Algorithmes/Borg/borg_f01.ipynb** et **Algorithmes/Borg/borg_instances.py**.\ pour la sauvegarde des résultats.\
La partie **6. RESULTATS** est liée à \
**Separable/separable.ipynb** \
**Low or moderate conditioning/low_or_moderate_conditioning.ipynb** \
**High conditioning and unimodal/high_conditioning_and_unimodal.ipynb** \
**Multimodal with global structure/multimodal_with_global_structure.ipynb** \
**Multimodal with weak global structure/multimodal_with_weak_global_structure.ipynb** \
pour l'analyse des résultats.\
Les tables sont sous forme de dictionnaires avec les différents seuils et les valeurs, et les graphiques sont sous forme d'images dans les dossiers Pictures.

## Auteurs
- **Leflaëc Pierre**
- **Tétart Julian**

## License
Ce projet est sous licence MIT - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations.

