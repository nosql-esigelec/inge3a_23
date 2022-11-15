# Création d'un bac à sable 

## Créer un compte Atlas
Aller sur la page: https://www.mongodb.com/docs/atlas/.
Cliquer sur **Try Free** et créer un compte en remplissant le formulaire.
Une fois le compte créé, MongoDB vous propose la création d'un cluster.
### Créer un cluster gratuit/sandbox
#### Choix du fournisseur Cloud
Vous devez choisir un fournisseur cloud pour votre serveur de base de données. 
L'option **Shared** vous donne accès à des clusters gratuits. Les providers vous proposent différentes régions où sont hébergés les serveurs. 
En règle général, pour l'efficacité des interactions avec le serveur, il est recommandé de choisir la région la plus proche de sa position géographique. 
>Dans notre cas, il s'agit de **Paris** pour le provider AWS. Si l'on souhaite travailler avec Google Cloud, la région la plus proche est la Belgique.

![[Pasted image 20221112115148.png]]
Une fois la région choisie, donner un nom au cluster. 
>Les autres configurations ne sont pas à modifier.

![[Pasted image 20221112115908.png]]
Cliquer sur **Create Cluster** pour valider l'opération.

#### Création d'un projet
Une fois un cluster créé, on peut ajouter un projet. Créer un projet en lui associant un nom.
![[Pasted image 20221112124118.png]]
#### Création d'une base de données
Une fois votre projet créée, créer un base de données à déployer rapidement. Cliquer sur **Build a Database**.
![[Pasted image 20221112123939.png]]
Choisir l'option **Shared** une nouvelle fois car elle gratuite.
![[Pasted image 20221112120442.png]]
#### Création d'un utilisateur
Créer un utilisateur(username+password) pour sa base de données.
Vous pouvez utiliser ces identifiants, ou les personnaliser:
**Username** es901-student 
**Password** es901-mongodb-intro
<span style="background:red; color:white"><b>Attention:</b> Pour la suite des TPs, ne pas mettre de caractères spéciaux dans votre mot de passe.</span> 
![[Pasted image 20221112120652.png]]
Une fois l'utilisateur créée et la base de données provisionnée, il faut gérer l'accès réseau à cette dernière. 
#### Sécurité réseaux
Dans cette étape, il faut spéciier les adresses IP depuis lesquelles un utilisateur peut se connecter.
![[Pasted image 20221112120730.png]]
Les configurations terminées, on obtient cet écran avec une base de données déployée, à laquelle nous pourrons nous connecter plus tard.
![[Pasted image 20221112120805.png]]
Afin de se connecter, nous aurons besoin d'un chaine de connexion. Récupérez là en cliquant sur **Connect**.
Ensuite, choisissez **Connect using MongoDB Compass**, sélectionner votre système d'exploitation, puis copier l'URL de connextion qui ressemble à celle ci:  `mongodb+srv://brice:<password>@cluster0.5cy4vr9.mongodb.net/test`.
![[Pasted image 20221112124524.png]]
Nous nous servirons de cette URL dans nos prochaines séances de TP.