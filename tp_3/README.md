# TP 3 : Neo4j with Browser and Python

Dans ce TP, nous allons découvrir l'utilisation de Neo4j avec le driver officiel Python : **neo4j**.

Ce TP s'articulera en 2 parties :
### **Twitter Graph** 

Nous allons créer un projet Twitter grâce à un compte [Sandbox](https://sandbox.neo4j.com/) créé au préalable et nos identifiants Twitter. Les consignes à suivre pour cette partie sont les suivantes [Neo4j Desktop with sandbox](sandbox.md).
### **Validalab**

Nous utiliserons le projet **Validalab**, en guise de cas pratique. 
Validalab est une organisation à but non lucratif donc le but est d'aider les citoyens à mieux s'informer et à être acteurs de leur consommation d'informations.
Durant le TP, nous allons mettre en place des requêtes permettant de :

- Évaluer la quantité de médias en France 
- Avoir un listage d'un certain nombre de médias
- Retrouver des médias spécifiques
- Afficher le résumé Wikipédia d'un média donné
- Déterminer la fiabilité d'un média selon les citations positives ou négatives dont il fait l'objet
- Déterminer les propriétaires finaux des médias
- Déterminer le nombre de médias que possèdent ces propriétaires

Ce TP s'effectuera en python à l'aide d'un [notebook](validalab.ipynb).

À la fin de ce TP, vous devrez être capable de :

- Se connecter à une base de données Neo4j via PyMongo
- Exécuter des requêtes CYPHER depuis une application python via Mongo
- Modifier des nœuds, relations dans une application python (#TODO)
- Supprimer des nœuds, relations dans une application python (#TODO)

Afin de mener à bien ce TP, bien vouloir prendre connaissance des informations suivantes :

- Avoir Anaconda installé
- Installer neo4j via la commande :
```shell
pip install neo4j
```
