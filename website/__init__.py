from flask import Flask
# from flask_restx import Api


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sjdkfbnhljsd sfdhjb'
    # api = Api()

    
    from .views import weather_dashboard
    # from .auth import auth

    app.register_blueprint(weather_dashboard, url_prefix="/")
    # app.register_blueprint(auth, url_prefix="/")

    return app
