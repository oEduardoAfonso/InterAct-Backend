from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)

app.config.from_object('config')

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
io = SocketIO(app)
migrate = Migrate(app, db)
CORS(app)

from .views import usuario_view, sala_view, pergunta_view