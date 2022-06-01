from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


# db table
class PostClient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(255))
    image = db.Column(db.String(255))


@app.route('/')
def hello_world():
    return jsonify(hello='world')