# Twitter Graph
[![to complete](https://img.shields.io/badge/TP_3_:Neo4j_with_Browser_and_Python-2ea44f)](README.md)

Dans ce TP, nous allons analyser nos interactions sur Twitter, car les réseaux sociaux sont un très bon cas d'usage pour les bases de données de type graphe.

Au programme, nous allons :
- Explorer nos comptes Twitter 
- Trouver les personnes qui ne nous **"FOLLOW BACK"** pas 


Nous allons utiliser pour ce TP, Neo4j sandbox. Il est donc important d'avoir créé un compte via ce lien : https://sandbox.neo4j.com/.

Une fois votre compte créé, nous allons créer un projet. 

Cliquer sur ![new_project.png](../data/images/new_project.png)
![account_created.png](../data/images/account_created.png)

Aller dans la section "Your own data", sélectionner **Twitter** et cliquer sur **Create**.
![twitter.png](../data/images/twitter.png)

Ensuite, autorisez l'accès à votre compte Twitter en renseignant vos identifiants, puis cliquer sur "Autoriser l'application"

![auth.png](../data/images/auth.png)

Une fois l'application, vos données Twitter vont commencer à être chargées dans votre projet.

![load.png](../data/images/load.png)

Une fois le chargement terminé, cliquer sur le bouton "Open with Browser"

![open.png](../data/images/open.png)

L'interface Neo4j Browser va s'ouvrir et vous pouvez commencer à exécuter les requêtes préparées.

![twitter_graph.png](../data/images/twitter_graph.png)

Notez vos résultats et commentez-les.

Exécutez la requête suivante pour trouver les personnes qui ne vous **FOLLOW BACK** pas.
```CYPHER
MATCH
    (me:User:Me)-[:FOLLOWS]->(f)
WHERE
    NOT (f)-[:FOLLOWS]->(me)
RETURN
    f.name, f.following, f.followers
ORDER BY
    f.followers DESC
```