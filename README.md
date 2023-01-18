# 🚙 Challenge IA sur les véhicules électriques et infrastructures de recharge  
Challenge IA proposé par [Latitudes](https://latitudes.notion.site/Pr-sentation-des-projets-de-l-Open-Data-University-5abab2bb9a6e453d817fe6bdf3806413), dans le cadre de l’Open Data University.

## :page_facing_up: Description
En lien avec la loi d’orientation des mobilités en France, qui fixe comme objectif la fin de la vente de voitures particulières et de véhicules utilitaires légers neufs utilisant des énergies fossiles d’ici 2040, le nombre de ventes de véhicules électriques a bondi de 128% en 2020 et de 63% en 2021.

Pour que le modèle du véhicule électrique soit viable, il est nécessaire de disposer d’une borne de recharge publique pour 10 voitures (Directive AFI). La France a largement dépassé ces préconisations. Néanmoins, le développement de la mobilité électrique doit passer par une adéquation des infrastructures de recharge aux besoins des usagers.

L'objectif de ce projet est de prédire le nombre de véhicules électriques en France selon la ruralité, pour 2023. Cela nous permettra d'en déduire par la suite le nombre de bornes de recharge.

## :card_index_dividers: Segmentation
Notre répertoire est segmenté en X fichiers python, deux fichiers markdown, un fichier .gitinore et un fichier texte pour les requirements :

```bash 
.
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt 
└── cluster
    ├── cluster_drawing.ipynb
    ├── clustering.py
    └── rurality_pop.py
```

- ``README.md`` contient l'ensemble des informations sur le projet pour pouvoir l'installer.
- ``CONTRIBUTING.md`` contient l'ensemble des informations sur les normes et les pratiques de collaboration et de gestion du projet.
- ``.gitignore`` contient les fichiers qui doivent être ignorés lors de l'ajout de fichiers au dépôt Git.
- ``requirements.txt`` contient la liste des modules et des bibliothèques Python qui doivent être installés, ainsi que leur version spécifique.
- ``cluster`` est le dossier pour implémenter les clusters. Il comprend deux fichiers python et un notebook. 
        - ``cluster_drawing.ipynb`` est le notebook python qui permet de visualiser les clusters.
        - ``clustering.py`` permet de créer les clusters autour des données.
        - ``rurality_pop.py`` permet d'agglomérer les bases de données.

## :pencil2: Auteurs
- HAMDI Ilyes  
- LETAIEF Maram
- LIDAM Soukaina  
- MICHOT Albane
- NONCLERCQ Rodolphe