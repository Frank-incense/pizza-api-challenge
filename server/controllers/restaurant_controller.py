from server.models import Restaurant
from server.config import db
from flask import Blueprint, jsonify, make_response, request

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route("/restaurants")
def restaurants():
    restaurants = Restaurant.query.all()
    
    if len(restaurants) > 0:
        response_body = [restaurant.to_dict() for restaurant in restaurants]
        response_status = 200

    else:
        response_body = {
            'Message': 'No restaurants found'
        }
        response_status = 200

    return make_response(jsonify(response_body), response_status)

@restaurants_bp.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurant(id):
    restaurant = Restaurant.query.filter_by(id = id).first()

    if restaurant:
        if request.method == 'GET':
            response_body = restaurant.to_dict()
            response_status = 200

        elif request.method == 'DELETE':
            db.session.delete(restaurant)
            db.session.commit()
            response_body = ''
            response_status = 204
    else:
        response_body = {
            'error': 'Restaurant not found'
        }
        response_status = 404
    
    return make_response(response_body, response_status)


