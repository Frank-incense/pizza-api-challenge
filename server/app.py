from flask import Flask
from dotenv import load_dotenv
from server.config import db
from server.models import Restaurant, Restaurant_Pizza, Pizza
from flask_migrate import Migrate
from .controllers import register_routes

load_dotenv()

app = Flask(__name__)

app.config.from_prefixed_env(prefix='FLASK')

db.init_app(app=app)
migrate = Migrate(app=app, db=db)

register_routes(app=app)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
