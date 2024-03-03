from flask import Flask
from stopsearch_api.index import index
from stopsearch_api.manual import manual
from stopsearch_api.home import home


app = Flask(__name__)

# register your routes here
app.route("/")(index)
app.route("/docs")(manual)
app.route("/home")(home)

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000,
        host="127.0.0.1"
    )