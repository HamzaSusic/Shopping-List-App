# Import SQL connection
from sql_connector import get_sql_connection

# Define SQL query as a constant
SELECT_ALL_SHOPPERS_QUERY = "SELECT * FROM shopping_list.Shoppers;"

# Function to display all shoppers
def get_all_shoppers(connection):
    cursor = connection.cursor()

    try:
        cursor.execute(SELECT_ALL_SHOPPERS_QUERY)

        response = []

        for (shopper_id, name) in cursor:
            response.append(
                {
                    'shopper_id': shopper_id,
                    'name': name
                }
            )
    
        return response
    except Exception as e:
        print(f"Error retrieving shoppers: {e}")
    finally:
        cursor.close()

# Testing get_all_shoppers function   
if __name__ == "__main__":
    connection = get_sql_connection()

    try:
        print(get_all_shoppers(connection))
    finally:
        connection.close()
