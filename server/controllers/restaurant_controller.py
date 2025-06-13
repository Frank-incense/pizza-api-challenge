from server.models import Restaurant
from flask import Blueprint, jsonify, make_response

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route("/restaurants")
def restaurants():
    restaurants = Restaurant.query.all()
    if len(restaurants) > 0:
        response_body = restaurants.to_dict()
        response_status = 200
    else:
        response_body = {
            'Message': 'No restaurants found'
        }
        response_status = 403

    return make_response(response_body, response_status)
