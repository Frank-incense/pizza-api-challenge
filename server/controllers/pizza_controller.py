from flask import Blueprint, make_response
from server.models import Pizza

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas')
def pizzas():
    pizzas = Pizza.query.all()
    if len(pizzas) > 0:
        response_body = pizzas.to_dict()
        response_status = 200
    else:
        response_body = {
            'Message': 'Pizza could not be found'
        }
        response_status = 200

    return make_response(response_body,response_status)