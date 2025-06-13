from pizza import db
from restaurant_pizza import Restaurant_Pizza

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    RestaurantPizzas = db.relationship('Restaurant_pizza', back_populates='restaurant')