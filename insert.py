import psycopg2

def create_connection():
    conn = psycopg2.connect(
        dbname='postgres',
        user='mojika_r',
        password='mozhgan2001m',
        host='localhost'
    )
    return conn


def create_inventory_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            quantity INT,
            price DECIMAL,
            type VARCHAR(50),
            weight DECIMAL,
            dimensions VARCHAR(100),
            file_size DECIMAL,
            download_link VARCHAR(255)
        )
    ''')
    conn.commit()
    cursor.close()


create_inventory_table()


def insert_item(item):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO inventory (name, quantity, price, type, weight, dimensions, file_size, download_link)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (item.name, item.quantity, item.price, type(item).__name__,
          getattr(item, 'weight', None),
          getattr(item, 'dimensions', None),
          getattr(item, 'file_size', None),
          getattr(item, 'download_link', None)))
    conn.commit()
    cursor.close()
    conn.close()


def update_stock_in_db(item_id, new_quantity):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE inventory SET quantity = %s WHERE id = %s
    ''', (new_quantity, item_id))
    conn.commit()
    cursor.close()
    conn.close()


def retrieve_all_items():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items


def find_items_below_threshold(threshold):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory WHERE quantity < %s', (threshold,))
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items


def total_inventory_value():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(price * quantity) FROM inventory')
    total_value = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total_value


def find_items_by_type(item_type):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory WHERE type = %s', (item_type,))
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items


def average_price():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(price) FROM inventory')
    avg_price = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return avg_price


def delete_item(item_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM inventory WHERE id = %s', (item_id,))
    conn.commit()
    cursor.close()
    conn.close()


def update_item_price(item_id, new_price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE inventory SET price = %s WHERE id = %s', (new_price, item_id))
    conn.commit()
    cursor.close()
    conn.close()


#
def retrieve_oldest_items():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory ORDER BY date_added ASC')  # Assuming date_added is a column
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items
