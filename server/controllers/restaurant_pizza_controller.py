from flask import Blueprint, make_response, request
from server.models import Restaurant_Pizza
from server.config import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def restaurant_pizzas():
    data = request.get_json()
    if 1 > data.get('price') > 30:
        return make_response({'errors':['Price must between 1 and 30']}, 400)
    
    new_restaurant_pizza = Restaurant_Pizza(
        price=data.get('price'),
        restaurant_id = request.form.get('restaurant_id'),
        pizza_id = request.form.get('pizza_id')
    )
    db.session.add(new_restaurant_pizza)
    db.session.commit

    res = new_restaurant_pizza.to_dict()
    stat = 200
    return make_response(res, stat)
