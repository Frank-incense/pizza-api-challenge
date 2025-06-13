from flask import Flask
from dotenv import load_dotenv
from .models.pizza import db
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)

app.config.from_prefixed_env(prefix='FLASK')
db.init_app(app=app)

migrate = Migrate(app=app, db=db)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
