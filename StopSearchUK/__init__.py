import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()



# Ensure the form media folder exists
UPLOAD_FOLDER = './StopSearchUK/assets'



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)
baseDir = os.path.abspath(os.path.dirname(__file__))

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if __name__ == "__main__":
    app.run(
        debug=True,
        port=os.environ["API_PORT"],
        host=os.environ["API_HOST"],
    )

from StopSearchUK.main import *
