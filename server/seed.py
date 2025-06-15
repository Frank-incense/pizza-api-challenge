from server.models import Restaurant, Restaurant_Pizza, Pizza
from server.app import app
from server.config import db
from faker import Faker
import random

fake = Faker()

with app.app_context():
    Restaurant_Pizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()
    db.session.commit()

    flavors = ['Pepperoni', 'Hawaaian', 'Margherita', 'Barberque', 'Chicken-macon']
    restaurants = [Restaurant(name=fake.company(),
                            address=fake.address()) 
                            for i in range(5)]

    pizzas = [Pizza(name=p,
                    ingredients=f"{fake.word()}, {fake.word()}, {fake.word()}") for p in flavors]

    db.session.add_all(restaurants+pizzas)
    db.session.commit()

    res_pizzas = [Restaurant_Pizza(price=random.randint(1,30),
                                restaurant_id=random.choice(restaurants).id,
                                pizza_id=random.choice(pizzas).id) for i in range(5)]


    db.session.add_all(res_pizzas)
    db.session.commit()
