from flask import Blueprint, make_response, request
from server.models import Restaurant_Pizza
from server.config import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def restaurant_pizzas():
    data = request.get_json()
        
    try:
        new_restaurant_pizza = Restaurant_Pizza(
            price=data.get('price'),
            restaurant_id = data.get('restaurant_id'),
            pizza_id = data.get('pizza_id')
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        res = new_restaurant_pizza.to_dict()
        stat = 200

        return make_response(res, stat)
    
    except ValueError as val:
        return make_response({'errors':[f'{val}']}, 400)


    
