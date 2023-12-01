from flask import Flask
from .views import views
from .auth import auths

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auths, url_prefix='/')
    
    return app