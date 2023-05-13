def bl_db_wrtr(black_list):
    import mysql.connector
    from mysql.connector import connect, Error 
    import pyperclip
    from . import config_real
    from . import b_db_filter_func
    pyperclip.copy('')
    clipboard_text = pyperclip.paste()

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Connection established3")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    print(len(black_list))
    resBlackList = []

    try:
        resBlackList = eval(b_db_filter_func.black_filter(black_list))
    except Exception as ex:
        print(f"b_db_filter_func___35{ex}")
        resBlackList = black_list

    #         CREATE TABLE black_list_test1 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     hotelid VARCHAR(20),
    #     url TEXT,
    #     fotos INT,
    #     description INT,
    #     facility INT,
    #     otziv VARCHAR(4),
    #     room INT,
    #     room_block INT

    # )
    # '''
    try:
        query6 = "INSERT INTO black_list_test1 (hotelid, url, fotos, description, facility, otziv, room, room_block) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        for item in resBlackList:
            try:
                values = (item["hotel_id"], item["url"], item["fotos"], item["description"], item["facility"], item["otziv"], item["room"], item["room_block"])
                cursor.execute(query6, values)
            except Exception as ex:
                print(f"b_db_filter_func___59{ex}")
                continue
        conn.commit()
    except Exception as ex:
        print(f"b_db_filter_func___63{ex}")

    try:
        cursor.close()
        conn.close()
    except Error as e:
        print(f"b_db_filter_func_Error connecting to MySQL: {e}")

    return 

