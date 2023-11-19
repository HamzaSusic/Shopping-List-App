# Importing Flask, sql connection, needed .py and and CORS
from flask import Flask, request, jsonify
from flask_cors import CORS
import productdao
import shopperdao
import shoppingListdao
from sql_connecter import get_sql_connection

app = Flask(__name__)
CORS(app)

connection = get_sql_connection()

# FUnction to display Products
@app.route('/getProducts', methods=['GET'])
def get_products():
    try:
        response = productdao.get_all_products(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred"}), 500

# FUnction to display Shoppers
@app.route('/getShoppers', methods=['GET'])
def get_shoppers():
    try:
        response = shopperdao.get_all_shoppers(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred"}), 500
    
# Function to add items to a shopping list
@app.route('/addItemsToShoppingList', methods=['POST'])
def add_items_to_shopping_list():
    try:
        data = request.get_json()
        shopper_id = data['shopper_id']
        item_ids = data['item_ids']
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred"}), 500
    
    # Check if adding these items would violate the constraint
    if not shoppingListdao.check_item_constraint(connection, item_ids):
        return jsonify({"message": "Adding these items would violate the constraint."})

    # Add items to the shopping list
    shoppingListdao.add_items_to_shopping_list(connection, shopper_id, item_ids)

    return jsonify({"message": "Items added to the shopping list successfully."})

# Function to display the shopping list for a specific shopper
@app.route('/getShoppingList', methods=['GET'])
def get_shopping_list():
    try:
        shopper_id = request.args.get('shopper_id')
        shopping_list = shopping_list.get_shopping_list(connection, shopper_id)
        return jsonify(shopping_list)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred"}), 500
    
# Start the server on port 4999
if __name__ == "__main__":
    print("starting flask server")
    app.run(port=4999)