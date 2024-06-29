from flask import Flask
from flask_cors import CORS
from routes.recommendation_routes import recommendation_bp

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000"]}})

app.register_blueprint(recommendation_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
