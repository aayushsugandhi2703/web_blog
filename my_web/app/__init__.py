from flask import Flask
from config import Config
from app.task.routes import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(task_bp)
    
    return app
