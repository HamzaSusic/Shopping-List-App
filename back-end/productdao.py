from sql_connecter import get_sql_connection
def get_all_products(connection):
    cursor = connection.cursor()

    query="SELECT * FROM shopping_list.items;"

    cursor.execute(query)

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

def add_product(connection, product):
    cursor=connection.cursor()
    query=("INSERT INTO items" 
           "(item_name, item_price)"
           "VALUES(%s, %s)")
    data = (product['item_name'], product['item_price'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor=connection.cursor()
    query=("DELETE FROM items WHERE item_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()
    
if __name__ == "__main__":
    connection = get_sql_connection()
    print(delete_product(connection, 6))
