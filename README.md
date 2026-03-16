# Lancement de l'API REST
## Installations préalables
Dans une venv (créée avec ```virtualenv -p python3 venv``` puis activée avec ```source venv/bin/activate``` ), réalisez les installations suivantes : 
- ```pip install flask``` 
- ```pip install flask-sqlalchemy```
- ```pip install python-dotenv```
- ```pip install flask-cors```

Ou lancez directement le fichier requirements.txt : 
- ```pip install -r requirements.txt```

## Lancement de l'API
Une fois dans la venv, effectuer un ```flask syncdb``` à la racine du projet afin de créer la base de données et/ou de remettre à 0 les données affichées

Pour lancer l'application, il suffit de faire un ```flask run```.

## Lancement de l'application
A la racine du projet vue (le repertoire qwizz), effectuez la commande suivante :
- ```npm run dev```

Cela permetera de lancer l'application de quizz et de naviguer sur l'application.