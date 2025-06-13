from pizza import db, Pizza
from restaurant import Restaurant


class Restaurant_Pizza(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    restaurant = db.relationship('Restaurant', back_populates='RestaurantPizzas')
    pizzas = db.relationship('Pizza', back_populates='RestaurantPizzas')