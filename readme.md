
DEVELOPPEMENT D’API

Getting Started

Installing Dependencies
Python 3.9.7
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.9)

Follow instructions to install the latest version of python for your platform in the python docs
Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs
PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the /plants_api directory and running:

pip install -r requirements.txt
or
pip3 install -r requirements.txt

This will install all of the required packages we selected within the requirements.txt file.
Key Dependencies

    Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

    SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

    Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

Running the server

From within the plants_api directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

To run the server on Windows, execute:

set FLASK_APP=flaskr
set FLASK_ENV=development
flask run

Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.



API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.
Error Handling

Errors are retourned as JSON objects in the following format: { "success":False "error": 400 "message":"Bad request" }

The API will return four error types when requests fail: . 400: Bad request . 500: Internal server error . 422: Unprocessable . 404: Not found
Endpoints

. ## GET/livres

GENERAL: cet endpoint permet istes tous les livres 

    
SAMPLE: curl -i http://localhost:5000/livres

        {
  "Livre": [
    {
      "ISBN": 1756, 
      "cat": 1, 
      "date_publication": "Thu, 03 Feb 2022 00:00:00 GMT", 
      "nomAuteur": "Fr\u201ad\u201aric Quinonero", 
      "nomEditeur": "Archipel", 
      "titre": "Julien Dor\u201a"
    }, 
    {
      "ISBN": 4175, 
      "cat": 2, 
      "date_publication": "Thu, 01 Jul 1999 00:00:00 GMT", 
      "nomAuteur": " Laurent Baffie", 
      "nomEditeur": " Le Livre de Poche", 
      "titre": "Le Dico 2"
    }, 
    {
      "ISBN": 784745, 
      "cat": 7, 
      "date_publication": "Tue, 12 Dec 2017 00:00:00 GMT", 
      "nomAuteur": "yokolo", 
      "nomEditeur": "vilio", 
      "titre": "SERPENTO"
    }
  ], 
  "succes": true, 
  "total": 17
}


## GET/categories 

ENERAL: cet endpoint permet de lister toutes les catégories


    
SAMPLE: curl -i http://localhost:5000/categories

{
  "Categorie": [
    {
      "Id": 1, 
      "libelle": "cin\u201ama"
    }, 
    {
      "Id": 2, 
      "libelle": "Humour"
    }, 
    {
      "Id": 4, 
      "libelle": "Cusine"
    }, 
    {
      "Id": 5, 
      "libelle": "Histoire"
    }, 
    {
      "Id": 6, 
      "libelle": "Scolaire"
    }, 
    {
      "Id": 7, 
      "libelle": "Litt\u201arature"
    }
  ], 
  "succes": true, 
  "total": 6
}


## GET/livres

GENERAL: cet endpoint permet de chercher un livre en particulier par son id 

    
SAMPLE: curl -i http://localhost:5000/livres_one_/<int:id>


{
  "selected_id": 5, 
  "selected_student": {
    "ISBN": 56058, 
    "cat": 2, 
    "date_publication": "Thu, 21 Jan 2021 00:00:00 GMT", 
    "nomAuteur": "Laurent Ruquier", 
    "nomEditeur": " Flammarion", 
    "titre": "Finement Con"
  }, 
  "sucess": true
}



## GET/livres

GENERAL: cet endpoint permet de  lister la liste des livres d’une catégorie

    
SAMPLE: curl -i http://localhost:5000/livreeee/<int:categorie_iid>'

{
  "id_categorie": 1, 
  "les livres ": [
    {
      "ISBN": 1756, 
      "cat": 1, 
      "date_publication": "Thu, 03 Feb 2022 00:00:00 GMT", 
      "nomAuteur": "Fr\u201ad\u201aric Quinonero", 
      "nomEditeur": "Archipel", 
      "titre": "Julien Dor\u201a"
    }
  ], 
  "succes": true, 
  "total": 1
}


## GET/livres

GENERAL: cet endpoint permet de chercher une catégorie par son id

    
SAMPLE: curl -i http://localhost:5000/categorie_one/<int:id>

{
  "selected_categorie": {
    "Id": 4, 
    "libelle": "Cusine"
  }, 
  "selected_id": 4, 
  "sucess": true
}



## GET/ suppression de livre

GENERAL: cet endpoint permet de supprimer un livre supprimer un livre

    
SAMPLE: curl -i http://localhost:5000/supre_livre/<int:id>


{
  "deleted_id": 4, 
  "deleted_livre": {
    "ISBN": 4175, 
    "cat": 2, 
    "date_publication": "Thu, 01 Jul 1999 00:00:00 GMT", 
    "nomAuteur": " Laurent Baffie", 
    "nomEditeur": " Le Livre de Poche", 
    "titre": "Le Dico 2"
  }, 
  "success": true, 
  "total": 16
}


## GET/ suppression d'une categorie

GENERAL: cet endpoint permet de supprimer un livre supprimer une ategorie

    
SAMPLE: curl -i http://localhost:5000/categories_livres_Supr/<int:categorie_iid>

{
  "delete_id": 1, 
  "livre_categories": [], 
  "succes": true, 
  "total": 4
}


PATCH/Modification d'une categorie

GENERAL: cet endpoint permet de modifier  le libellé d’une categorie

SAMPLE: curl -i http://localhost:5000/Update_cat/<int:id>



 "new_student": {
        "Id": 7,
        "libelle": "le_Monde"
    },
    "success": true,
    "updated_id_student": 7
}





PATCH/Modification d'un livre

GENERAL: cet endpoint permet de modifier un livre

SAMPLE: curl -i http://localhost:5000/modifier_livre/<int:id>

"new_livre": {
        "ISBN": 588995,
        "cat": 7,
        "date_publication": "Sat, 15 Jan 2022 00:00:00 GMT",
        "nomAuteur": "MOHAMED",
        "nomEditeur": "SADOME",
        "titre": "LEMONDE"
    },
    "success": true,
    "updated_id_livre": 27
}





## Testing
To run the tests, run
