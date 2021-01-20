from flask import render_template
from app import app
from app.models.destinations import orders

@app.route("/")
def index():
    return render_template("index.html", title="Travel", orders=orders)

@app.route("/orders/<index>")
def order(index):
    lookup_order = orders[int(index)]
    return render_template("order.html", title="Customer", order=lookup_order)