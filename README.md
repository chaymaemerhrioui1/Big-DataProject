# Introduction
Ce projet a consisté à développer un site web dédié aux brevets de drones, en exploitant les données issues de plusieurs bases de brevets (Google Patent, PatentScoop,WIPO, PubMed, etc.) grâce aux techniques de Big Data. Dans Un premier temps, un scraping des sites web de brevets a été réalisé pour récupérer les données pertinentes. Celles-ci ont ensuite été stockées dans une
base de données MongoDB.Des analyses approfondies ont été menées sur ces données à l'aide de Spark, permettant d'extraire des informations clés sur les tendances en matière de brevets de drones.
Les résultats de ces analyses ont été liés à PowerBI pour créer des visualisations interactives et intuitives, facilitant l'exploration et la compréhension des données par les utilisateurs.
Enfin, un site web a été développé, intégrant les données et analyses sur les brevets de drones. Ce site offre une interface conviviale pour consulter les brevets, visualiser
les tendances et générer des rapports personnalisés.
Ce projet a permis de démontrer l'intérêt des technologies de Big Data et de Data Visualization pour exploiter efficacement les données issues de multiples sources et offrir une plateforme innovante dans le domaine des brevets de drones.

# Objectif 
Ce projet vise à créer un site web dédié aux brevets de drones, en intégrant les données issues de plusieurs sources et en offrant des outils de visualisation pour faciliter l'exploration et la compréhension des données. Ce site web devrait offrir une plateforme unique pour les chercheurs, les entrepreneurs, et les professionnels du domaine des drones, permettant de consulter, d'analyser et de comprendre les brevets de drones de manière efficace.

# Architecture de Projet 
![image](https://github.com/user-attachments/assets/44e26604-323a-492f-aac9-6042cc15e42e)

## Collection de Données : 
Pour ce projet, plusieurs sources de données ont été identifiées comme pertinentes pour collecter des informations sur les brevets de drones. Les principales sources incluent Google Patent, PatentScoop, WIPO,
PubMed, et d'autres bases de données spécialisées dans les brevets.
Un processus de web scraping a été mis en place pour extraire les données des sites web des différentes sources. Des scripts ont été développés pour automatiser la collecte des informations telles que les titres des brevets, les inventeurs, les dates de dépôt, les résumés, et d'autres données pertinentes.

## Stockage de Données : 
Les données extraites via le web scraping ont été stockées dans une base de données MongoDB. Ce choix a été fait pour sa flexibilité et sa capacité à gérer des données non structurées, typiques des informations sur les brevets.

## Analyse des Données : 

### Nettoyage de données : 
Avant d'analyser les données, un processus de nettoyage a été effectué pour éliminer les doublons, les données manquantes et les erreurs potentielles. Cela a permis d'assurer la qualité des données avant de les utiliser pour les analyses ultérieures.

### Utilisation de Spark : 
Les données nettoyées ont été analysées en utilisant Apache Spark, un framework de traitement de données distribué. Spark a permis d'effectuer des analyses en parallèle sur de grands ensembles de données, facilitant l'extraction d'informations pertinentes sur les tendances des brevets de drones.

## Visualisation des Données : 
Les résultats de l'analyse des données ont été intégrés avec PowerBI, un outil de visualisation de données interactif. Cela a permis de créer des tableaux de bord dynamiques et des graphiques visuels pour présenter les informations sur les brevets de drones de manière claire et compréhensible.Ce processus méthodologique détaillé a permis de collecter, traiter, analyser et visualiser les données sur les brevets de drones de manière efficace, en utilisant des outils et des techniques adaptés pour chaque étape du projet.



