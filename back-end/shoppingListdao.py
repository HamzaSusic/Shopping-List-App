# Import SQL connection
from sql_connecter import get_sql_connection

# Define SQL queries as constants
INSERT_SHOPPING_LIST_QUERY = "INSERT INTO ShoppingLists (shopper_id) VALUES (%s)"
INSERT_LIST_ITEMS_QUERY = "INSERT INTO ListItems (list_id, item_id) VALUES (%s, %s)"
SELECT_SHOPPING_LIST_QUERY = """
    SELECT i.name as item_name
    FROM ListItems li
    JOIN Items i ON li.item_id = i.item_id
    JOIN ShoppingLists sl ON li.list_id = sl.list_id
    WHERE sl.shopper_id = %s
"""
SELECT_ITEM_COUNT_QUERY = "SELECT COUNT(*) as count FROM ListItems WHERE item_id = %s"

# Function to add items to the shopping list
def add_items_to_shopping_list(connection, shopper_id, item_ids):
    cursor = connection.cursor()

    try:
        cursor.execute(INSERT_SHOPPING_LIST_QUERY, (shopper_id,))
        shopping_list_id = cursor.lastrowid
        
        for item_id in item_ids:
            cursor.execute(INSERT_LIST_ITEMS_QUERY, (shopping_list_id, item_id))

        connection.commit()
    except Exception as e:
        print(f"Error adding items to shopping list: {e}")
        connection.rollback()
    finally:
        cursor.close()

# Function to display shopping list
def get_shopping_list(connection, shopper_id):
    cursor = connection.cursor()

    try:
        cursor.execute(SELECT_SHOPPING_LIST_QUERY, (shopper_id,))
        shopping_list = [row['item_name'] for row in cursor.fetchall()]
        return shopping_list
    except Exception as e:
        print(f"Error retrieving shopping list: {e}")
    finally:
        cursor.close()

# Function to check if the item is already in more than three shopping lists
def check_item_constraint(connection, item_ids):
    cursor = connection.cursor()

    try:
        for item_id in item_ids:
            cursor.execute(SELECT_ITEM_COUNT_QUERY, (item_id,))
            count = cursor.fetchone()['count']
            if count >= 3:
                return False
        return True
    except Exception as e:
        print(f"Error checking item constraint: {e}")
         
