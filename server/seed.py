from models import Restaurant, Restaurant_Pizza, Pizza
from faker import Faker
import random
fake = Faker()

flavors = ['Pepperoni', 'Hawaaian', 'Margherita', 'Barberque', 'Chicken-macon']
restaurants = [Restaurant(name=fake.company(),
                          address=fake.address()) 
                          for i in range(10)]
print(restaurants)

pizzas = [Pizza(name=p,
                ingredients=f"{fake.word()}, {fake.word()}, {fake.word()}") for p in flavors]

print(pizzas)

res_pizzas = [Restaurant_Pizza(price=random.randint(1,30),
                               restaurant_id=random.choice(restaurants).id,
                               pizza_id=random.choice(pizzas).id) for i in range(10)]

print(res_pizzas)