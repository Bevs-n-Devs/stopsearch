import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
baseDir = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    app.run(
        debug=True,
        port=os.environ["API_PORT"],
        host=os.environ["API_HOST"],
    )

from StopSearchUK.main import *
