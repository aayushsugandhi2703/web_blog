from flask import Flask
from config import Config
from app.task.routes import task_bp
from app.models import Base, engine, Session

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Base.metadata.create_all(engine) 

    
    app.register_blueprint(task_bp, url_prefix='/task')
    
    return app
