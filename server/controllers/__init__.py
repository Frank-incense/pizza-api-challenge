from .restaurant_controller import restaurants_bp
from .pizza_controller import pizza_bp
from .restaurant_pizza_controller import restaurant_pizza_bp

def register_routes(app):
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)