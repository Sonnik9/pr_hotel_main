def db_opener(n1, n2):
    data_DB = []
    try:
        import time
        import mysql.connector
        from mysql.connector import connect, Error 
        from . import config_real
        print(n1, n2)       
        config = {
            'user': config_real.user,
            'password': config_real.password,
            'host': config_real.host,
            'port': config_real.port,
            'database': config_real.database,      
        }

        for _ in range(3):

            try:
                conn = mysql.connector.connect(**config)      
                print("REader connection established fotos")
                break
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                time.sleep(3)
                continue           
        
        try:
            cursor = conn.cursor() 
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

        try:
            query_last_item = "SELECT COUNT(*) FROM upz_hotels;"
            cursor.execute(query_last_item)
            # # Извлечение результата запроса
            last_item = cursor.fetchone()[0]
            # p2 = int(last_item) - n1
            # p1 = int(last_item) - n2
            p2 = int(last_item) - int(n1) + 1
            p1 = int(last_item) - int(n2) + 1
        except:
            pass

        try:
            select_query  = ("SELECT id, hotel_id, url, fotos FROM upz_hotels "
            f"WHERE id BETWEEN {p1} AND {p2} "
            )
            cursor.execute(select_query)
            hotels_data = cursor.fetchall()
        except Exception as e:
            print(f"db_reader___str46: {e}")

        try:
            for id, hotel_id, url, fotos in hotels_data:
                data_DB.append({
                    'id': id,
                    'hotel_id': hotel_id,
                    'url': url,
                    'fotos': fotos
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
        try:
            print(f"data_DB _____{data_DB[0]}")
            print(f"data_DB _____{data_DB[-1]}")
        except:
            pass
        return data_DB
    except:
        return data_DB
        

# python db_reader.py
# python -m db_all.db_reader
