from server.config import db
from sqlalchemy_serializer import SerializerMixin

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    RestaurantPizzas = db.relationship('Restaurant_Pizza', back_populates='restaurant', cascade='all, delete-orphan')

    serialize_rules = ("-RestaurantPizzas.restaurant",)

    def __repr__(self):
        return f"Restaurant: {self.id}, {self.name}"