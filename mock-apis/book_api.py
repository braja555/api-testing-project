from flask import Flask, request, jsonify
import json
import os
import uuid

app = Flask(__name__)

# Get the directory path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the books.json file in the source folder
books_file_path = os.path.join(current_dir, 'source', 'books.json')

# Construct the path to the users.json file in the source folder
users_file_path = os.path.join(current_dir, 'source', 'users.json')


# Load books from JSON file
with open(books_file_path, 'r') as f:
    books_db = json.load(f)

# Load users from JSON file
with open(users_file_path, 'r') as f:
    users_db = json.load(f)

@app.route('/book/search', methods=['GET'])
def get_books_by_title():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    # Search books by title
    matching_books = [book for book in books_db if title.lower() in book['title'].lower()]

    if not matching_books:
        return jsonify({"message": "No books found with the given title"}), 404

    return jsonify(matching_books)


@app.route("/users/<userId>/cart", methods=["POST"])
def add_to_cart(userId):
    # Check for the clear_cart parameter
    clear_cart = request.args.get('clear_cart', 'false').lower() == 'true'

    # Check if user exists, if not create a new one
    if userId not in users_db:
        users_db[userId] = {"userId": userId, "cart": []}

    user = users_db[userId]

    if clear_cart:
        # Clear the user's cart
        user["cart"] = []
        return jsonify({"message": "Cart cleared successfully", "user": user}), 200

    # Parse the request JSON
    cart_item = request.json

    # Validate the input
    if not cart_item or not cart_item.get("bookId") or not cart_item.get("quantity"):
        return jsonify({"error": "Invalid input"}), 400

    # Check if the book exists and is available
    book = next((book for book in books_db if book["bookId"] == cart_item["bookId"]), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    if not book["availability"]:
        return jsonify({"error": "Book is not available"}), 400

    # Check if the item is already in the cart
    existing_item = next((item for item in user["cart"] if item["bookId"] == cart_item["bookId"]), None)
    if existing_item:
        existing_item["quantity"] += cart_item["quantity"]
    else:
        user["cart"].append(cart_item)

    return jsonify({"message": "Item added to cart successfully", "user": user}), 200

#Checkout API
@app.route("/users/<userId>/checkout", methods=["POST"])
def checkout(userId):

    # Check if user exists
    if userId not in users_db:
        return jsonify({"error": "User not found"}), 404

    user = users_db[userId]
    cart_item = {"bookId": "1-e51969c6-df00-4829-afa9-1104749015b", "quantity": 1}
    user["cart"].append(cart_item)

    # Get the user's cart
    cart = user["cart"]

    # Check if the cart is empty
    if not cart:
        return jsonify({"error": "Cart is empty"}), 400

    # Validate the quantity of each book in the cart
    for item in cart:
        book = next((book for book in books_db if book["bookId"] == item["bookId"]), None)
        if not book:
            return jsonify({"error": f"Book with ID {item['bookId']} not found"}), 404
        if book["quantity"] < item["quantity"]:
            return jsonify({"error": f"Not enough stock for book {book['title']}. Available: {book['quantity']}, Requested: {item['quantity']}"}), 400

    # Generate a random order ID
    order_id = str(uuid.uuid4())

    # Return the checkout details
    return jsonify({
        "orderId": order_id,
        "userId": userId,
        "message": "Your order is successful",
    }), 200


if __name__ == "__main__":
    app.run(debug=True)


