import flask, json, datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

app = flask.Flask("TipTop Karniz")
app.config.from_object(Config)
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import models
db.create_all()

session_data = []
session_ips = {}

# @app.route("/")
# def index():
#     return flask.render_template("index.html")

# @app.route("/get_tt")
# def send_token():
#     responce = app.response_class(response=f'{{"table": \"{json.loads(open("config.json", "r").read())["table_token"]}\"}}', status=200, mimetype="application/json")
#     responce.headers['Access-Control-Allow-Origin'] = '*'
#     return responce

# @app.route("/send", methods = ['POST'])
# def get_support_data():
#     responce = app.response_class()
#     request_json = flask.request.json
#     request_json["timestamp"] = datetime.datetime.now().timestamp() // (30 * 60)
#     request_json["ip"] = flask.request.remote_addr
#     print(request_json)
#     if flask.request.remote_addr not in session_ips:
#         session_ips[flask.request.remote_addr] = 0
#     if datetime.datetime.now().timestamp() - session_ips[flask.request.remote_addr] > 30:
#         if request_json not in session_data:
#             responce.status = 200
#             session_data.append(request_json)
#             session_ips[flask.request.remote_addr] = datetime.datetime.now().timestamp()
#         else:
#             responce.status = 208
#     else:
#         if request_json not in session_data:
#             responce.status = 230
#         else:
#             responce.status = 208
#     return responce

# if __name__ == "__main__":
    # db.create_all()
    # product = app.models.Products(name="test", img="123")
    # db.session.add(product)
    # db.session.commit()
#     print(db.session.query(app.models.Products).all())
#     print(product)
#     app.run(debug=True)