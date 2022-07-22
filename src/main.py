
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users,Planetas,Personajes



app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def handle_hello():
    users = Users.query.all()
    listUsers = list(map(lambda obj: obj.serialize(),users))
    response_body = {
        "result":listUsers
    }
    return jsonify(response_body), 200

@app.route('/personajes', methods=['GET'])
def handle_personajes():
    personajes = Personajes.query.all()
    listPersonajes = list(map(lambda obj:obj.serialize(),personajes))
    response_body={
        "result":listPersonajes
    }
    return jsonify(response_body), 200
    
@app.route('/personajes/<int:id>', methods = ['GET'])
def handle_single_personaje():
    single_personajes = Personajes.query.get(id)
    characters = single_personajes.serialize()
    response_body = {
        "result":personajes
    }
    return jsonify(response_body), 200

@app.route('/planetas', methods=['GET'])
def handle_planetas():
    planetas = Planetas.query.all()
    listPlanetas = list(map(lambda obj:obj.serialize(),planetas))
    response_body={
        "result":listPlanetas
    }
    return jsonify(response_body), 200
    
@app.route('/planetas/<int:id>', methods = ['GET'])
def handle_single_planeta():
    single_planetas = Planetas.query.get(id)
    planetas = single_planetas.serialize()
    response_body = {
        "result":planetas
    }
    return jsonify(response_body), 200


@app.route('/users/favorite', methods = ['GET'])
def favorito_users(users_id):
    favorito_personaje=Users.query.filter_by(id=users_id).first().personajes
    favorito_planeta= Users.query.filter_by(id=users_id).first().planetas
    lista_favoritos=[]
    for i in favorito_personaje:
        lista_favoritos.append(i.serialize())
    for x in favorito_planeta:
        lista_favoritos.append(x.serialize())
    return jsonify(lista_favoritos), 200


@app.route('/favorite/planeta/<int:planeta_id>', methods=['POST'])
def add_favorito_planeta(planetas_id):
    planet=Planetas.query.get(planetas_id)
    usuario=Users.query.get(1)
    usuario.planetas.append(planet)
    db.session.commit()
    return jsonify({"succes":"planet agregado"}), 200


@app.route('/favorite/personaje/<int:personaje_id>', methods=['POST'])
def add_favorito_personaje(personajes_id):
    character=Personajes.query.get(personajes_id)
    usuario=Users.query.get(1)
    usuario.personajes.append(character)
    db.session.commit()
    return jsonify({"succes":"character agregado"}), 200

@app.route('/favorite/planeta/<int:planeta_id>', methods=['DELETE'])
def delete_favorito_planeta(planetas_id):
    planet= Planetas.query.get(planetas_id)
    usuario= Users.query.get(1)
    usuario.planetas.remove(planet)
    db.session.commit()
    return jsonify({"succes":"planeta eliminado"}), 200

@app.route('/favorite/personaje/<int:personaje_id>', methods=['DELETE'])
def delete_favorito_personaje(personajes_id):
    character= Personajes.query.get(personajes_id)
    usuario= Users.query.get(1)
    usuario.planetas.remove(planet)
    db.session.commit()
    return jsonify({"succes":"planeta eliminado"}), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)