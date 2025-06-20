from server.config import db
from sqlalchemy_serializer import SerializerMixin

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    RestaurantPizzas = db.relationship('Restaurant_Pizza', back_populates='pizza')

    serialize_rules = ('-RestaurantPizzas.pizza',)
    serialize_only = ('id', 'name', 'ingredients',)

    def __repr__(self):
        return f"Pizza {self.id}, {self.name}"