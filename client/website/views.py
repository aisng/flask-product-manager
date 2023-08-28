import json
from flask import Blueprint, render_template, redirect, url_for, flash
from config import Config
import requests
from .forms import ProductForm, SelectProductForm


views = Blueprint("views", __name__)


@views.route("/")
def index():
    return render_template("index.html")


@views.route("/all_products", methods=["GET"])
def all_products():
    r = requests.get(Config.API_URL)
    all_products = json.loads(r.text)
    return render_template("all_products.html", all_products=all_products)


@views.route("/update_product/<product_id>", methods=["GET", "POST", "PUT"])
def update_product(product_id):
    product_url = Config.API_URL + f"/{product_id}"
    r = requests.get(product_url)
    product = json.loads(r.text)

    form = ProductForm(
        name=product["name"],
        description=product["description"],
        price=product["price"],
        quantity=product["qty"],
    )

    if form.validate_on_submit():
        updated_product = {
            "name": form.name.data,
            "description": form.description.data,
            "price": form.price.data,
            "qty": form.quantity.data,
        }
        requests.put(product_url, json=updated_product)
        return redirect(url_for("views.all_products"))
    return render_template("update_product.html", form=form)


@views.route("/delete_product/<product_id>", methods=["GET", "DELETE", "POST"])
def delete_product(product_id):
    product_url = Config.API_URL + f"/{product_id}"
    r = requests.get(product_url)
    product = json.loads(r.text)
    print(product)
    product_name = product["name"]
    flash(f"Are you sure you want to delete product {product_name}?")
    requests.delete(product_url)
    return redirect(url_for("views.all_products"))


@views.route("/new_product", methods=["GET", "POST"])
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = {
            "name": form.name.data,
            "description": form.description.data,
            "price": form.price.data,
            "qty": form.quantity.data,
        }
        requests.post(Config.API_URL, json=new_product)
        return redirect(url_for("views.all_products"))
    return render_template("new_product.html", form=form)
