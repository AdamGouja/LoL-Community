# LOL Community

Clément Maurer & Adam Gouja


## Introduction : 

### Présentation des données :

Le dataset utilisé lors de ce projet est à la scène Esport Européene du jeu Ligue of Legends.
Les données utilisés par ce projet on entièrement été recupérées depuis twitter en utilisant du scrapping.
Ces données nous permettent de voir les différentes interactions entre les différentes equipes de la ligue Française (LFL), de la ligue Européene (LEC) et de leurs communautés.

## User guide : 

Afin d'executer le code plusieurs étapes sont nécessaires : 

Tout d'abord on peut cloner le projet : `git clone https://github.com/AdamGouja/LoL-Community.git`

Ensuite, il faut télécharger les paquets nécessaires. Ces paquets sont listés dans le fichiers *requirements.txt*.

Afin de les installer on peut utiliser la commande suivante après s'être placé dans le repertoire du projet : `python -m pip install -r requirements.txt`

Enfin on peut lancer le main grace à : 

* Linux / MacOS : `python3 visu.py`
* Windows : `python visu.py`

A cause de la création des dataframes le dashboard met un peu de temps à se lancer. 

Une fois que le dashboard est lancé suivez l'adresse indiquée.


## Le rapport

Le jeu de données récupéré par Scrapping Twitter nous a permis de voir les interactions entre les idfférentes structures et les fanbase de chacune d'entre elles. Nous serions tentés dans un premier temps de nous dire que les équipes de plus haut niveau (Ligue Européenne) ont un public plus vaste donc plus investi. Cependant, nous pouvons voir que certaines équipes de LEC ne possèdent pas une très grande fanbase.

Grâce au jeu de données, nous pouvons voir que la Karmine Corp, gagnante de la Ligue Française en 2020, possède une fanbase énorme, surpassant même les plus grandes équipes de LEC. C'est notamment pour cela que cette équipe est la mieux placée afin d'avoir accès à une place en ligue européenne afin d'être possiblement qualifiée pour les championnats du Monde.

Gràace à nos données nous pouvons donc affirmer que la popularité dd'une équipe est représentative de son classement dans les ligues. Cependant elles ne sont pas représentatives de la ligue dans laquelle l'équipe évolue comme a pu le prouver la Karmine Corp.
