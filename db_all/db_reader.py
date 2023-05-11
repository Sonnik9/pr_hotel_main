def db_opener(n1, n2, limit):
    import mysql.connector
    from mysql.connector import connect, Error 
    import pyperclip

    pyperclip.copy('')
    clipboard_text = pyperclip.paste()


    user = 'hote_tophot77_db'
    password = '8dGBX2Kx'
    database = 'hote_tophot77_db'
    host =  '5.75.140.137'
    port = '3306'

    data_DB = []
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
        # select_query  = ("SELECT id, hotel_id, url, fotos, description, room, facility, otziv FROM upz_hotels ")
        select_query  = ("SELECT id, hotel_id, url, fotos, description, room, facility, otziv FROM upz_hotels "
        f"WHERE id BETWEEN {n1} AND {n2} "
        f"LIMIT {limit}")
        cursor.execute(select_query)
        hotels_data = cursor.fetchall()
    except Exception as e:
        print(f"db_reader___str46: {e}")

    try:
        for id, hotel_id, url, fotos, description, room, facility, otziv in hotels_data:
            data_DB.append({
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
        cursor.close()
        conn.close()
        # print(result[100000:100002])
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    return data_DB
