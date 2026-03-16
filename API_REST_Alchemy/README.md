# Lancement de l'API REST
## Installations préalables
Dans une venv (créée avec ```virtualenv -p python3 venv``` puis activée avec ```source venv/bin/activate``` ), réalisez les installations suivantes : 
- ```pip install flask``` 
- ```pip install flask-sqlalchemy```
- ```pip install python-dotenv```

## Lancement de l'API
Une fois dans la venv, effectuer un ```flask syncdb``` à la racine du projet afin de créer la base de données et/ou de remettre à 0 les données affichées

Pour lancer l'application, il suffit de faire un ```flask run```.

## Commandes CURL
Afin de tester les différentes commandes CURL du fichier ```Commandes_curl.sh```, il est nécessaire d'ouvrir un second terminal avec la venv d'activée. Une fois ceci fait, les commandes CURL sont prêtes à être testées.