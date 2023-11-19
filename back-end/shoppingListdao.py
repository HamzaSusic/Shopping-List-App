from sql_connecter import get_sql_connection
def add_items_to_shopping_list(connection, shopper_id, item_ids):
    cursor = connection.cursor()

    # Insert a new shopping list
    cursor.execute("INSERT INTO ShoppingLists (shopper_id) VALUES (%s)", (shopper_id,))
    shopping_list_id = cursor.lastrowid

    # Insert items into the shopping list
    for item_id in item_ids:
        cursor.execute("INSERT INTO ListItems (list_id, item_id) VALUES (%s, %s)", (shopping_list_id, item_id))

    connection.commit()
    cursor.close()

def get_shopping_list(connection, shopper_id):
    cursor = connection.cursor()

    # Retrieve the shopping list for the specified shopper
    cursor.execute("""
        SELECT i.name as item_name
        FROM ListItems li
        JOIN Items i ON li.item_id = i.item_id
        JOIN ShoppingLists sl ON li.list_id = sl.list_id
        WHERE sl.shopper_id = %s
    """, (shopper_id,))

    shopping_list = [row['item_name'] for row in cursor.fetchall()]

    cursor.close()
    return shopping_list

def check_item_constraint(connection, item_ids):
    cursor = connection.cursor()

    for item_id in item_ids:
        # Check if the item is already in more than three shopping lists
        cursor.execute("SELECT COUNT(*) as count FROM ListItems WHERE item_id = %s", (item_id,))
        count = cursor.fetchone()['count']
        if count >= 3:
            cursor.close()
            return False

    cursor.close()
    return True
