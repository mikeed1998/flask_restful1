from flask import Flask, jsonify
from products import products

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({'message': 'pong!'})


@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Products List"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    # print(product_name)
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)

