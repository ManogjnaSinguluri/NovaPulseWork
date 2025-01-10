from flask import Flask
from .routes.arbitrage import arbitrage_blueprint

def create_app():
    app = Flask(__name__, static_folder='../frontend', static_url_path='')
    
    # Register Blueprints
    app.register_blueprint(arbitrage_blueprint)

    # Serve static files
    @app.route('/')
    def serve_index():
        return app.send_static_file('index.html')

    @app.route('/<path:path>')
    def serve_static(path):
        return app.send_static_file(path)

    return app