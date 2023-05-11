import mysql.connector


def delete_tables():
        
    conn = mysql.connector.connect(
        host='localhost',
        user='sonnik11',
        password='9283sono',
        database='upz_hotels_test2'
    )
    # Создание объекта Cursor
    cursor = conn.cursor() 
    try:
        cursor.execute("DROP TABLE result_photos")
    except:
        pass 
    try:
        cursor.execute("DROP TABLE result_photo_metadata")
    except:
        pass 
    try:
        cursor.execute("DROP TABLE result_description")
    except:
        pass 
    try:
       cursor.execute("DROP TABLE result_facilities")  
    except:
        pass 
    try:  
        cursor.execute("DROP TABLE result_room")
    except:
        pass 
    try:
       cursor.execute("DROP TABLE result_room_block")
    except:
        pass
    # conn.commit()
    cursor.close()
    conn.close()
    return print('the tables was deleted successfully')


delete_tables()