from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Import views after app initialization to avoid circular imports
    from app import views
    
    return app