# Import SQL connection
from sql_connector import get_sql_connection

# Define SQL queries as constants
SELECT_ALL_PRODUCTS_QUERY = "SELECT * FROM shopping_list.items;"
INSERT_PRODUCT_QUERY = "INSERT INTO items (item_name, item_price) VALUES (%s, %s)"
DELETE_PRODUCT_QUERY = "DELETE FROM items WHERE item_id = %s"

# Function to show all products from the database
def get_all_products(connection):
    cursor = connection.cursor()

    cursor.execute(SELECT_ALL_PRODUCTS_QUERY)

    response = []

    for (item_id, item_name, item_price) in cursor:
        response.append(
            {
                'item_id': item_id,
                'item_name': item_name,
                'item_price': item_price
            }
        )
    
    return response

# Function to add a product to the database
def add_product(connection, product):
    cursor = connection.cursor()
    data = (product['item_name'], product['item_price'])

    try:
        cursor.execute(INSERT_PRODUCT_QUERY, data)
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        print(f"Error adding product: {e}")
        connection.rollback()
        return None

# Function to delete a product from the database
def delete_product(connection, product_id):
    cursor = connection.cursor()

    try:
        cursor.execute(DELETE_PRODUCT_QUERY, (product_id,))
        connection.commit()
    except Exception as e:
        print(f"Error deleting product: {e}")
        connection.rollback()

# Checking delete function functionality
if __name__ == "__main__":
    connection = get_sql_connection()

    # Example of deleting a product
    delete_product(connection, 6)

    # Close the database connection
    connection.close()
