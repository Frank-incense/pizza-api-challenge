# Pizza API Challenge
## Introduction

My task was to build a RESTful API for a Pizza Restaurant using flask. I am expected to implement models validations and routes. The API will be tested using Postman. 

## Project Setup
1. Fork and clone the github repository to your local environment.
    ```
    git clone git@github.com:<Your-username>/pizza-api-challenge.git
    ```
2. Change directory to the cloned repo and initialise a virtual environment.
    ```
    cd pizza-api-challenge
    python -m venv .venv
    source .venv/bin/activate
    ```
3. Install project dependencies.
    ```
    pip install -r requirements.txt
    ``` 
4. Configure environment variables.
    ```
    FLASK_SQLACHEMY_DATABASE_URI=postgresql://<username>:<password>@localhost:5432/pizza_api

    ```
5. Run the application
    ```
    export FLASK_APP=server.app  # Or set in .flaskenv
    export FLASK_ENV=development
    flask run
    ```
## Database setup
1. Initialize Migrations
```
flask db init
```
2. Generate Migration Scripts
```
flask db migrate -m "Initial migration"
```
3. Apply Migrations
```
flask db upgrade
```
## Seeding the Database

After setting up your tables, populate them with data:
```
python -m server.seed
```
## API Endpoints
### List All Pizzas

GET /pizzas
```
[
  {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Pepperoni, Cheese"
  }
]
```
### List All Restaurants

GET /restaurants
```
[
  {
  "id": 1,
  "name": "Pizza Inn",
  "address": "Ngong Road",
  "pizzas": [
    {
      "id": 1,
      "name": "Pepperoni",
      "ingredients": "Pepperoni, Cheese"
    }
    ]
  },
  ...
]
```
### Get One Restaurant and Its Pizzas

GET /restaurants/<id>
```
{
  "id": 1,
  "name": "Pizza Inn",
  "address": "Ngong Road",
  "pizzas": [
    {
      "id": 1,
      "name": "Pepperoni",
      "ingredients": "Pepperoni, Cheese"
    }
  ]
}
```
### Add a Pizza to a Restaurant

POST /restaurant_pizzas

Request Body:
```
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1
}
```
Response:
```
{
  "id": 10,
  "price": 10,
  "pizza_id: 1,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella"
  },
  "restaurant_id": 1,
  "restaurant": {
    "id": 2,
    "name": "Slice of Heaven",
    "address": "456 Market St"
  }
}
```
### Validation Rules
Field	    Rule
name	    Required, non-empty string
address	    Required for restaurants
ingredients	Required for pizzas
price	    Integer, must be between 1 and 30
pizza_id	Must reference an existing pizza
restaurant_id	Must reference an existing restaurant
### Testing with Postman

- Open Postman.
- Set the base URL to http://127.0.0.1:5000.
- Create requests to:
    ```
        GET /pizzas

        GET /restaurants

        GET /restaurants/<int:id>

        DELETE /restaurants/<int:id>

        POST /restaurant_pizzas with a JSON body
    ```
- Save your requests into a Postman Collection.
- You can import/export your collection to collaborate or reuse.

### Folder Structure
    ```
    pizza-api/
    ├── server/
    │   ├── app.py
    │   ├── config.py
    │   ├── seed.py
    │   ├── models/
    │   └── controllers/
    ├── migrations/
    ├── .env
    ├── requirements.txt
    ├── README.md
    ```

