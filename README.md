# 🚙 Challenge IA sur les véhicules électriques et infrastructures de recharge  
Challenge IA proposé par [Latitudes](https://latitudes.notion.site/Pr-sentation-des-projets-de-l-Open-Data-University-5abab2bb9a6e453d817fe6bdf3806413), dans le cadre de l’Open Data University.

## :page_facing_up: Description
En lien avec la loi d’orientation des mobilités en France, qui fixe comme objectif la fin de la vente de voitures particulières et de véhicules utilitaires légers neufs utilisant des énergies fossiles d’ici 2040, le nombre de ventes de véhicules électriques a bondi de 128% en 2020 et de 63% en 2021.

Pour que le modèle du véhicule électrique soit viable, il est nécessaire de disposer d’une borne de recharge publique pour 10 voitures (Directive AFI). La France a largement dépassé ces préconisations. Néanmoins, le développement de la mobilité électrique doit passer par une adéquation des infrastructures de recharge aux besoins des usagers.

## ❓ Problématiques
Le projet propose ainsi de répondre aux deux questions suivantes :

1. Comment le nombre d’infrastructures de recharge évolue-t-il en France ? Comparer cette évolution avec celle du parc de véhicules électriques et les objectifs pour 2030 ainsi que d’autres indicateurs qui vous semblent pertinents.

2. La répartition des infrastructures de recharge sur le territoire correspond-elle à une logique de distribution de la population et de trafic routier ? 

## 🎯 Objectifs
L’objectif général du projet et les impacts recherchés sont :

1. de donner une plus grande visibilité aux infrastructures de recharge, un facteur important dans la décision d’achat d’un véhicule électrique, et donc d’encourager le développement de la mobilité électrique

2. aux autorités nationales, régionales et locales de savoir où les infrastructures de recharge sont attendues et seront utilisées pour planifier leurs aménagements. 

## 🤔 Choix techniques
Notre objectif initial de ce projet était de prédire le nombre de véhicules électriques en France par mois pour chaque commune pour 2023. Cela nous permettrait d'en déduire par la suite le nombre de bornes de recharge.

Néanmoins, suite à un manque de données sur un grand nombre de nos variables cibles (bornes de recharge, les transports en commun, les voitures thermiques, les aides de l'état, les prix essence/électricité, l'orientation politique/sociale et les sorties de modèles électriques), nous décidons de faire une prédiction trimestrielle du nombre de véhicules électriques pour 2023 à partir de 40 clusters déterminés en fonction de la population, niveau de vie, position géographique et ruralité de chaque commune, des émissions de CO2 et du traffic routier. Cela nous permettra de prédire le nombre de bornes de recharge nécessaires :

| Variable | Cluster : Population, ruralité et niveau de vie | Émissions de CO2 | Traffic routier |
|---|---|---|---|
| Échelle temporelle | constant | année | année |
| Échelle géographique | commune | national | département |

## :card_index_dividers: Segmentation
Notre répertoire est segmenté en X fichiers python, deux fichiers markdown, un fichier .gitinore et un fichier texte pour les requirements :

```bash 
.
├── README.md 
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt 
├── data 
    ├── Emmision_1960-2021.csv
    ├── ve_par_commune.csv
    └── cluster
        ├── CSV_Pop.csv
        ├── CSV_ruralité.csv
        ├── FRANCE_COMMUNE_NIVEAU_DE_VIE-FIGARO.csv
        └── GEO_TER_ADE_centroide_communes_france.csv
├── data_analysis.ipynb
├── x.ipynb
└── cluster
    ├── cluster_drawing.ipynb
    ├── clustering.py
    └── rurality_pop.py
```

- ``README.md`` contient l'ensemble des informations sur le projet pour pouvoir l'installer.
- ``CONTRIBUTING.md`` contient l'ensemble des informations sur les normes et les pratiques de collaboration et de gestion du projet.
- ``.gitignore`` contient les fichiers qui doivent être ignorés lors de l'ajout de fichiers au dépôt Git.
- ``requirements.txt`` contient la liste des modules et des bibliothèques Python qui doivent être installés, ainsi que leur version spécifique.
- ``data`` contient l'ensemble des données utilisées.
- ``data_analysis.ipynb`` est le notebook pour l'analyse des données.
- ``cluster`` est le dossier pour implémenter les clusters. Il comprend deux fichiers python et un notebook : ``rurality_pop.py`` permet d'agglomérer les bases de données,``clustering.py`` permet de créer les clusters autour des données et ``cluster_drawing.ipynb`` est le notebook python qui permet de visualiser les clusters.

## :wrench: Installation
Pour lancer le code, ouvrez dans un premier temps les fichiers python dans le fichier cluster :

1. Tout d'abord, assurez-vous que vous avez installé une version `python` supérieure à 3.9. Nous vous conseillons un environnement conda avec la commande suivante : 
```bash
conda create --name vehicules_electriques python=3.9
```
- Pour activer l'environnement :
```bash
conda activate vehicules_electriques
```
- Pour accéder au répertoire : 
```bash
cd challenges_ia_vehicules_electriques
```

2. Vous devez ensuite installer tous les `requirements` en utilisant la commande suivante :
```bash
pip install -r requirements.txt
```

3. Exécuter les fichiers python du fichier cluster en utilisant les commandes suivantes :
```bash
cd cluster
python3 [nom du fichier]
```


Exécuter ensuite les notebooks python dans l'ordre suivant : 

1. cluster_drawing.ipynb

2. data_analysis.ipynb

3. X.ipynb


N'oubliez pas de bien changer le chemin d'accès aux données.

## :pencil2: Auteurs
- HAMDI Ilyes  
- LETAIEF Maram
- LIDAM Soukaina  
- MICHOT Albane
- NONCLERCQ Rodolphe