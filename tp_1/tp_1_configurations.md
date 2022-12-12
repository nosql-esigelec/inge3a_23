---
#nosql #atlas 
- Installer Mongo Shell (référencer un lien)
- Loader des fichiers Json, faire des finds dessus
- Créer un compte Atlas
- Créer un cluster gratuit
- user: brice; mdp: bYUwmeLyq8yEW
mongosh mongodb+srv://brice:bYUwmeLyq8yEW@cluster0.rdty5gv.mongodb.net
- [[Load sample Dataset]]
- Opération CRUD depuis le shell, en se connectant à son cluster, en utilisant les data loadées
---
# Installations
### [[Créer une sandbox ou bac à sable ]]
### Installer MongoDB server
Télécharger le serveur Mongo DB via le lie suivant:
https://www.mongodb.com/try/download/community
Choisir le fichier .msi pour installer correctement Mongo.
Une fois l'installation terminée, ajouter le chemin `C:\Program Files\MongoDB\Server\6.0\bin` de Mongo DB à la variable d'envrionnment Path du système.
#### [[Ajouter le bin au Path]]
- Ouvrir la barre de recherche dans démarrage,  cherchez “Edit the system environment variables” ou "Modifier les variables d'environnement système" en Français :
   [![Screenshot of Start Search](https://www.architectryan.com/static/start_menu-91c0473bae32fa3862658e4d6e62d75c-2facb.png)](https://www.architectryan.com/static/start_menu-91c0473bae32fa3862658e4d6e62d75c-2facb.png)
-   Cliquer sur le bouton “Environment Variables…”.[![Screenshot of System Properties](https://www.architectryan.com/static/system_properties-f3a4f86cdd178c48ed9d8398743f85df-39c95.png)](https://www.architectryan.com/static/system_properties-f3a4f86cdd178c48ed9d8398743f85df-39c95.png)
-   Sous la section “System Variables”, trouver la variable **Path** et cliquer sur "Edit"  [![Screenshot of Environment Variables](https://www.architectryan.com/static/select_row_and_edit-48423a2a0724e226bd3f69468d9eaabd-70c4b.png)](https://www.architectryan.com/static/select_row_and_edit-48423a2a0724e226bd3f69468d9eaabd-70c4b.png)
-   L'interface “Edit environment variable” va apparaître. Cliquer sur "New" pour ajouter une nouvelle valeur et insérer le chemin des fichiers binaires de MongoDB soit `C:\Program Files\MongoDB\Server\6.0\bin`.[![Screenshot of Edit Environment Variables](https://www.architectryan.com/static/edit_path_variable-42eb044d39582f04f1f213e17e4fcb30-c532b.png)](https://www.architectryan.com/static/edit_path_variable-42eb044d39582f04f1f213e17e4fcb30-c532b.png)
-   Cliquer sur "OK" pour sauvegarder cette modification.
-   La prise en compte de cette modification pourraît nécessiter le redémarrage de la machine.
-   Pour vérifier l'ajout de cette variable, ouvrir un terminal PowerShell:
    ![[2022-11-12 (3).png]]
  - Exécuter la commande suivante et vérifier que le chemin ajouté est bien dans la liste affichée
	```PowerShell
    $env:PATH
    ```
Si ce n'est pas le cas, redémarrer la machine.
Une fois la machine redémarrée, on peut ajouter des scripts de Mongo dans ce chemin afin de les utiliser.
### Installer Mongo Shell
Télécharger la version zip du Shell de Mongo DB. 
https://www.mongodb.com/try/download/shell
Une fois téléchargée, extraire le contenu du fichier zip.
Ensuite, naviguer jusqu'au dossier bin de cette librairie. Copier et coller le contenu(notamment le script `mongosh`) vers `C:\Program Files\MongoDB\Server\6.0\bin`.
### Installer les outils Mongo
Télécharger la version zip du des outils de BDD de Mongo DB. 
https://www.mongodb.com/try/download/database-tools
Ensuite, naviguer jusqu'au dossier bin de cette librairie. 
![[Pasted image 20221111112638.png]]
Copier et coller le contenu(cf. image) vers `C:\Program Files\MongoDB\Server\6.0\bin`.
![[Pasted image 20221111112824.png]]

Pour vérifier que ces scripts sont exécutables, ouvrir un nouveau terminal et exécutez quelques commandes. 
```PowerShell
mongodump
```
Si le résultat de cette commande est le suivant:
>'mongodump' n’est pas reconnu en tant que commande interne
ou externe, un programme exécutable ou un fichier de commandes.

alors les scripts n'ont pas été correctement installés

---
