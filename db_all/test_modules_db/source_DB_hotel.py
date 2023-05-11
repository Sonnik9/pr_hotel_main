def db_opener():
    import mysql.connector
    from mysql.connector import connect, Error 
    from config_real import user, password, database, host, port
    # print([user, password, database, host, port])
    import json
    # import clipboard
    import pyperclip

    pyperclip.copy('')
    clipboard_text = pyperclip.paste()

    copy_DB = []
    config = {
        'user': user,
        'password': password,
        'host': host,
        'port': port,
        'database': database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Connection established")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    try:
        select_query  = ("SELECT id, hotel_id, url, fotos, description, room, facility, otziv FROM upz_hotels ")
        # select_query  = ("SELECT hotel_id, url, fotos, description, room, facility FROM upz_hotels "
        # "WHERE id BETWEEN 1 AND 100 "
        # "LIMIT 100")
        cursor.execute(select_query)
        hotels_data = cursor.fetchall()
    except:
        pass

    try:
        for id, hotel_id, url, fotos, description, room, facility, otziv in hotels_data:
            copy_DB.append({
                'id': id,
                'hotel_id': hotel_id,
                'url': url,
                'fotos': fotos,
                'description': description,
                'room': room,
                'facility': facility,
                'otziv': otziv, 

            })
            # print(hotel_id)
    except Exception as ex:
        print(f"source_DB_hotel_46str___{ex}")
    
    try:
        with open(f'hotels_copy2.json', "w", encoding="utf-8") as file: 
            json.dump(copy_DB, file, indent=4, ensure_ascii=False)
    except Exception as ex:
        print(f"writerr__str86__{ex}") 
    try:
        cursor.close()
        conn.close()
        # print(result[100000:100002])
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    return 

db_opener()

# python source_DB_hotel.py



# GRANT ALL PRIVILEGES ON *.* TO 'hotel_test1'@'5.75.140.137' IDENTIFIED BY '6687vono' WITH GRANT OPTION;




# import mysql.connector

# # установка соединения с базой данных
# cnx = mysql.connector.connect(user='user', password='password',
#                               host='host', database='database')
# cursor = cnx.cursor()

# # выполнение запроса
# query = ("SELECT column1, column2 FROM my_table "
#          "WHERE id BETWEEN 1000 AND 2000 "
#          "LIMIT 1000")
# cursor.execute(query)

# # обработка результатов
# for (column1, column2) in cursor:
#     print("{} - {}".format(column1, column2))

# # закрытие соединения с базой данных
# cursor.close()
# cnx.close()


# select_query  = ("SELECT hotel_id, url, fotos, description, room, facility FROM upz_hotels "
#         "WHERE id BETWEEN 1 AND 100000 "
#         "LIMIT 100000")

# select_query = "SELECT * FROM upz_hotels"







