from server.config import db
from sqlalchemy_serializer import SerializerMixin

class Restaurant_Pizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant-pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    restaurant = db.relationship('Restaurant', back_populates='RestaurantPizzas')
    pizza = db.relationship('Pizza', back_populates='RestaurantPizzas')

    serialize_rules =('-restaurant.RestaurantPizzas','-pizza.RestaurantPizzas',)