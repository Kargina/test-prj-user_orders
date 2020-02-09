from flask import Flask, render_template
from sqlalchemy.engine import create_engine
import os

from user_project.config import DB_PATH
from user_project.db import Session, user_list, user_orders, get_user_by_id

import logging

log = logging.getLogger()

if not os.path.isfile(DB_PATH):
    log.error("Database does not exist, please run init_data.py")
    exit(1)

engine = create_engine(f"sqlite:///{DB_PATH}")
Session.configure(bind=engine)

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html.j2")


@app.route("/users")
def users_page():
    users = user_list()
    return render_template("users.html.j2", users=users)

@app.route("/orders/<id>")
def user_order(id):
    user = get_user_by_id(id)
    if not user:
        return render_template("404.html"), 404
    orders = user_orders(user.id)
    if not orders.count():
        orders = None
    return render_template("orders.html.j2", user=user, orders=orders)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
