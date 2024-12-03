from flask import Flask
from config.config import Config
from config.database import init_db
from routes.user_bp import user_bp
import os

app = Flask(__name__)
app.config.from_object(Config)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Initialize the database
init_db(app)  

# Register the blueprint
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
