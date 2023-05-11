import mysql.connector
def create_tables():
    import mysql.connector
    from mysql.connector import connect, Error 
    from config_copy import user, password, database, host, port
    import pyperclip
    print([user, password, database, host, port])
    pyperclip.copy('')
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    # return

    config = {
        'user': user,
        'password': password,
        'host': host,
        # 'port': port,
        'database': database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Connection2 established")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    create_table_query1 = '''
        CREATE TABLE upz_hotels_copy (
        # id INT AUTO_INCREMENT PRIMARY KEY,
        hotel_id VARCHAR(255),
        url VARCHAR(255),
        fotos INT,
        description INT,
        room INT,
        facility INT,
        otziv INT
    )
    '''

    cursor.execute(create_table_query1)
    # conn.commit()
    cursor.close()
    conn.close()
    
    return print("the tables was created successfully")


create_tables()


# sudo mysql -u root -p

# CREATE USER 'sonnik12'@'localhost' IDENTIFIED BY '6687vono';
# CREATE DATABASE upz_hotels_copy1;
# GRANT ALL PRIVILEGES ON upz_hotels_copy1.* TO 'sonnik12'@'localhost';

# FLUSH PRIVILEGES;
# EXIT;





















    # import clipboard

# Создание таблицы
    # create_table_query1 = '''
    # CREATE TABLE result_photos (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     hotelid VARCHAR(255),
    #     url_max VARCHAR(255),
    #     url_square60 VARCHAR(255),
    #     preview_list_photo TEXT DEFAULT '',
    #     photo_item_src VARCHAR(255),
    #     photo_item_id VARCHAR(255),
    #     photo_item_title TEXT, 
    #     all_photos TEXT DEFAULT '',
    #     id_photo VARCHAR(255),
    #     photo_max1280x900 VARCHAR(255),
    #     photo_max1024x768 VARCHAR(255),
    #     photo_max200 VARCHAR(255)
    # )

#     create_table_query1 = '''
#         CREATE TABLE upz_hotels_copy (
#         # id INT AUTO_INCREMENT PRIMARY KEY,
#         hotel_id VARCHAR(255),
#         url VARCHAR(255),
#         fotos INT,
#         description INT,
#         room INT,
#         facility INT,
#         otziv INT
#     )
#     '''

#     # ['id', 'hoid', 'max', 'square60', 'list_photo', 'src', 'idF', 'pTtl', 'all_photos', 'id_ph', 'p1', 'p2', 'p3']
#     # Создание таблиц
#     # create_table_query2 = '''
#     # CREATE TABLE result_description (
#     #     id INT AUTO_INCREMENT PRIMARY KEY,
#     #     hotelid VARCHAR(50),
#     #     enusname TEXT
#     # )
#     # '''

#     # create_table_query3 = '''
#     # CREATE TABLE result_facilities (
#     #     id INT AUTO_INCREMENT PRIMARY KEY,
#     #     hotelid VARCHAR(255),
#     #     result_facilities_upz_list TEXT DEFAULT '',
#     #     name TEXT,
#     #     facilitytype_id VARCHAR(255),
#     #     facilitytype_name_list TEXT DEFAULT '',
#     #     facilitytype_name VARCHAR(255),
#     #     hotelfacilitytype_id VARCHAR(255),
#     #     uniq VARCHAR(255)
#     # )
#     # '''

#     # create_table_query4 = '''
#     # CREATE TABLE result_room (
#     #     id INT AUTO_INCREMENT PRIMARY KEY,
#     #     hotelid VARCHAR(50),
#     #     result_room_upz_list TEXT DEFAULT '',
#     #     room_id VARCHAR(50),
#     #     name_room VARCHAR(255),
#     #     endescription TEXT,
#     #     allow_children VARCHAR(255),
#     #     private_bathroom_highlight VARCHAR(255),
#     #     bed_configurations VARCHAR(255),
#     #     apartament_photo_list TEXT DEFAULT '',
#     #     photo1 VARCHAR(255),
#     #     photo2 VARCHAR(255),
#     #     photo3 VARCHAR(255),
#     #     photo4 VARCHAR(255),
#     #     photo5 VARCHAR(255),
#     #     photo6 VARCHAR(255),
#     #     photo7 VARCHAR(255),
#     #     photo8 VARCHAR(255),
#     #     photo9 VARCHAR(255),
#     #     photo10 VARCHAR(255)
#     # )
#     # '''
#     # create_table_query5 = '''
#     #     CREATE TABLE result_room_block (
#     #     id INT AUTO_INCREMENT PRIMARY KEY,
#     #     hotelid VARCHAR(255),
#     #     result_room_block_upz_list TEXT DEFAULT '',
#     #     room_id VARCHAR(255),
#     #     room_name VARCHAR(255),
#     #     gross_price DECIMAL(10,2),
#     #     currency VARCHAR(10),
#     #     nr_children VARCHAR(255),
#     #     max_occupancy VARCHAR(255),
#     #     mealplan VARCHAR(255),
#     #     room_surface_in_m2 VARCHAR(255),
#     #     nr_adults VARCHAR(255),
#     #     all_inclusive VARCHAR(255),
#     #     all_facilities_of_room TEXT
#     # )
#     # '''
#     cursor.execute(create_table_query1)
#     # cursor.execute(create_table_query2)
#     # cursor.execute(create_table_query3)
#     # cursor.execute(create_table_query4) 
#     # cursor.execute(create_table_query5) 
#     # conn.commit()
#     cursor.close()
#     conn.close()
    
#     return print("the tables was created successfully")


# create_tables()



