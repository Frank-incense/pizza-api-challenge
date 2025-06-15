from server.config import db
from sqlalchemy_serializer import SerializerMixin

class Restaurant_Pizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant-pizzas'

    id = db.Column(db.Integer, primary_key=True)
    _price = db.Column(db.Integer, nullable=False)
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    restaurant = db.relationship('Restaurant', back_populates='RestaurantPizzas')
    pizza = db.relationship('Pizza', back_populates='RestaurantPizzas')

    serialize_rules =('-restaurant.RestaurantPizzas','-pizza.RestaurantPizzas',)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, val):
        
        if isinstance(val, int) and 1 < val < 30:
            self._price = val
        else:
            raise ValueError('Price must be between 1 and 30')
        
    def __repr__(self):
        return f"Restaurant Pizza: {self.id}, {self.price}"