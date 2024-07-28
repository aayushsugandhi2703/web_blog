from app.api.endpoints import api_bp

def register_api(app):
    app.register_blueprint(api_bp, url_prefix='/api')
