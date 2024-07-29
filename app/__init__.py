from flask import Flask
from app.models import Base, engine, Session
from app.routes.auth import auth, init_login_manager
from app.routes.blog import post
from app.api.endpoints import api_bp

def create_app():
    app = Flask(__name__)
   

    # Initialize database
    Base.metadata.create_all(engine)

    # Register Blueprints
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(post, url_prefix='/post')
    app.register_blueprint(api_bp, url_prefix='/api')

    # Initialize login manager
    init_login_manager(app)

    return app
