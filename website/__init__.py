from flask import Flask
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sjdkfbnhljsd sfdhjb'
    # app.config['MONGO_URI'] = "mongodb+srv://newuser:newmongouser@cluster0.zxhpmba.mongodb.net/?retryWrites=true&w=majority"
    # # cluster = MongoClient("mongodb+srv://newuser:newmongouser@cluster0.zxhpmba.mongodb.net/?retryWrites=true&w=majority")
    # mongo = PyMongo(app)
    from .views import views
    # from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    # app.register_blueprint(views, url_prefix="/signup")

    return app
