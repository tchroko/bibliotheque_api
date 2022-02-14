import sys
#from crypt import methods
import os
from unicodedata import category
from click import Abort
import psycopg2  
from flask import Flask, jsonify, request, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from dotenv import load_dotenv 
load_dotenv()


'''import os
from flask import Flask, abort, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from dotenv import load_dotenv '''


app = Flask(__name__)

password=quote_plus(os.getenv('password'))
local=os.getenv('local')
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:{}@{}:5432/projet".format(password,local)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Livre(db.Model):
    __tablename__ = 'livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer,unique=True, nullable=False)
    titre = db.Column(db.String(100),nullable=False)
    datepublication = db.Column(db.DateTime,nullable=False)
    auteur = db.Column(db.String(100),nullable=False)
    editeur = db.Column(db.String(100),nullable=False)
    categorie_id = db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=False)

    def format(self):
        return {
            'ISBN':self.isbn,
            'titre':self.titre,
            'date_publication':self.datepublication,
            'nomAuteur':self.auteur,
            'nomEditeur':self.editeur,
            'cat':self.categorie_id

        }
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


    def insert(self):
        db.session.add(self)
        db.session.commit()
    db.create_all()

class Categorie(db.Model):
    __tablename__ ='categories'
    id=db.Column(db.Integer, primary_key=True)
    libelle=db.Column(db.String(100), nullable=False)
    livres=db.relationship("Livre", backref=db.backref("categories", lazy=True))
     


    def __init__(self,libelle):
        self.libelle=libelle

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format_cat(self):
        return {
            'Id':self.id,
            'libelle':self.libelle
        }

    def update(self):
        db.session.commit()
    def insert(self):
        db.session.add(self)
        db.session.commit()
    db.create_all()

# Listes tous les livres

@app.route('/livres',methods=['GET'])
def get_all_books():
    livres=Livre.query.all()
    books=[livre.format() for livre in livres ]
    return jsonify({
        'succes':True,
        'Livre':books,
        'total':Livre.query.count()
    })

#Chercher un livre en particulier par son id


@app.route('/livres_one_/<int:id>',methods=['GET'])
def get_one_book(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return jsonify({
            "sucess":True,
            "selected_id":id,
            "selected_student":livre.format()
        })

# Lister la liste des livres d’une catégorie       

@app.route('/livreeee/<int:categorie_iid>' )
def liste_categorie(categorie_iid):
    try:
        categorie=Categorie.query.get(categorie_iid)
        if categorie is None :
            abort(404)
        else:

            query=Livre.query.filter_by(categorie_id=categorie_iid) 
            livre=query.all()
            formater_livre=[livred.format() for livred in livre]
            return jsonify({
                'succes':True,
                'id_categorie':categorie_iid,
                'les livres ':formater_livre,
                'total':query.count()
            })
    except:
        abort(400)


#Listes toutes les catégories

@app.route('/categories',methods=['GET'])
def get_all_categories():
    categories=Categorie.query.all()
    format_categorie=[categorie.format_cat() for categorie in categories ]
    return jsonify({
        'succes':True,
        'Categorie':format_categorie,
        'total':Categorie.query.count()
 
    })


# Chercher une catégorie par son id

@app.route('/categorie_one/<int:id>',methods=['GET'])
def get_one_categorie(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return jsonify({
            "sucess":True,
            "selected_id":id,
            "selected_categorie":categorie.format_cat()
        })


#nouvelle categorie

@app.route('/categories_new',methods=['POST'])
def newcat():
    body=request.get_json()
    libelle=body.get('nom',None)
    lib=Livre(libelle=libelle)
    lib.insert()
    ca=Livre.query.all()
    categ=[c.forma() for c in ca]
    return jsonify({
                'succes':True,
                'Categorie':categ,
                'total':Categorie.query.count()

            })


#Supprimer un livre

@app.route('/supre_livre/<int:id>')
def delete_livre(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        livre.delete()
        return jsonify({
            "deleted_id":id,
            "success":True,
            "total":Livre.query.count(),
            "deleted_livre":livre.format()
        })


#- Supprimer une categorie

@app.route('/categories_livres_Supr/<int:categorie_iid>' )
def delete_categorie(categorie_iid):
    categorie=Categorie.query.get(categorie_iid)
    if categorie is None:
        abort(404)
    else:
        livre=Livre.query.filter_by(categorie_id=categorie_iid) 
        livre.delete()
        categorie.delete()
        formatt=[liv.format() for liv in livre]
        return jsonify({
            'succes':True,
            'delete_id':categorie_iid,
            'livre_categories':formatt,
            'total':Categorie.query.count()
            
        }) 



#- Modifier le libellé d’une categorie

@app.route('/Update_cat/<int:id>',methods=['PATCH'])
def update_cate(id):
    categorie=Categorie.query.get(id)
    if categorie is None :
        abort(400)
    else: 
        body=request.get_json()
        categorie.libelle=body.get('libelle',None)
        categorie.update()
        return jsonify({
            "success":True,
            "updated_id_student":id,
            "new_student":categorie.format_cat()
        })



# Modifier un livre


@app.route('/modifier_livre/<int:id>',methods=['PATCH'])
def update_livre(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        body=request.get_json()
        livre.isbn=body.get('id')
        livre.isbn=body.get('isbn')
        livre.titre=body.get('titre')
        livre.datepublication=body.get('datepublication')
        livre.auteur=body.get('auteur')
        livre.editeur=body.get('editeur')
        livre.categorie_id=body.get('categorie_id')
        livre.update()
        return jsonify({
            "success":True,
            "updated_id_livre":id,
            "new_livre":livre.format()
        })

if __name__ == "__main__":
    app.run(debug=True)




#   capturer la liste des erreurs
     
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404
    
@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False, 
        "error": 500,
        "message": "----Internal server error----"
        }), 500
       
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False, 
        "error": 400,
        "message": "Bad request"
        }), 400




    


