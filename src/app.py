from flask import Flask
from routes import routes 
from flask_cors import CORS
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
CORS(app, resources={"*": {"origins": "*"}})

# Registra el blueprint en la aplicación Flask
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=4000)