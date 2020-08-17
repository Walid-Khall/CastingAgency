import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth

# app = Flask(__name__)
# setup_db(app)
# CORS(app)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    CORS(app)


# Get Movies and Actors endpoints:-----------------------------------

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(jwt):
        try:
            selection = Movie.query.order_by(Movie.id).all()
            movies = [movie.format() for movie in selection]
            return jsonify({
                "success": True,
                "movies": movies
            })
        except BaseException:
            abort(404)

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(jwt):
        try:
            selection = Actor.query.order_by(Actor.id).all()
            actors = [actor.format() for actor in selection]
            return jsonify({
                "success": True,
                "actors": actors
            })
        except BaseException:
            abort(404)

    # DELETE Movies and Actors endpoints

    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(jwt, id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.delete()
            return jsonify({
                "success": True,
                "delete": id
            })
        except BaseException:
            abort(404)

    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwt, id):
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.delete()
            return jsonify({
                "success": True,
                "delete": id
            })
        except BaseException:
            abort(404)

    # POST Movies and Actors endpoints----------------------------------------

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(jwt):
        try:
            body = request.get_json()
            new_title = body.get('title')
            new_release = body.get('release')
            movies = Movie(title=new_title, release=new_release)
            movies.insert()
            movies = movies.format()
            return jsonify({
                "success": True,
                "movie": movies
            })
        except BaseException:
            abort(400)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(jwt):
        try:
            body = request.get_json()
            new_name = body.get('name'),
            new_age = body.get('age'),
            new_gender = body.get('gender')
            actors = Actor(name=new_name, age=new_age, gender=new_gender)
            actors.insert()
            actors = actors.format()
            return jsonify({
                "success": True,
                "actors": actors
            })
        except BaseException:
            abort(400)

    # PATCH Movies and Actors endpoints---------------------------------------

    @app.route('/movies/<id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movies(jwt, id):
        body = request.get_json()
        new_title = body.get('title')
        new_release = body.get('release')
        try:
            selection = Movie.query.filter(Movie.id == id).all()
            for movies in selection:
                movies.title = new_title
                movies.release = new_release
            movies.update()
            movies = movies.format()
            return jsonify({
                "success": True,
                "movie": movies
            })
        except BaseException:
            abort(400)

    @app.route('/actors/<id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_actors(jwt, id):
        body = request.get_json()
        new_name = body.get('name'),
        new_age = body.get('age'),
        new_gender = body.get('gender')
        try:
            selection = Actor.query.filter(Actor.id == id).all()
            for actors in selection:
                actors.name = new_name
                actors.age = new_age
                actors.gender = new_gender
            actors.update()
            actors = actors.format()
            return jsonify({
                "success": True,
                "actor": actors
            })
        except BaseException:
            abort(404)

    # Error Handling
    '''
    Example error handling for unprocessable entity
    '''

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    # -------------------------------- done -----------------------------

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(405)
    def not_allowd(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowd"
        }), 405

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    '''
    @TODO implement error handler for AuthError
        error handler should conform to general task above
    '''

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }), 401

    return app

app = create_app()

if __name__ == '__main__':
    app.run()