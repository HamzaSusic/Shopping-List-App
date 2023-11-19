from sql_connecter import get_sql_connection
def get_all_shoppers(connection):
    cursor = connection.cursor()

    query="SELECT * FROM shopping_list.Shoppers;"

    cursor.execute(query)

    response = []

    for (shopper_id, name) in cursor:
        response.append(
            {
                'shopper_id': shopper_id,
                'name': name
            }
        )
    
    return response
    
if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_shoppers(connection))