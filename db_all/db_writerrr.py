def db_wrtr(total, n2):
    try:
        import time
        import mysql.connector
        from mysql.connector import connect, Error 
        from . import config_real
        print('hello db_writerr fotos')

        config = {
            'user': config_real.user,
            'password': config_real.password,
            'host': config_real.host,
            'port': config_real.port,
            'database': config_real.database,      
        }
        for _ in range(5):
            try:
                conn = mysql.connector.connect(**config)      
                print("Writerr connection established2 fotos")
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                time.sleep(3)
                continue
            
            try:
                cursor = conn.cursor() 
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                time.sleep(3)
                continue
            break
        try:
            print(len(total))
            resPhoto = []
            whiteList_set = set()
            whiteList = []
            n = int(int(n2)/1000)
        except:
            pass
        try:
            for t in total:
                try:
                    resPhoto += t
                except:
                    continue

            resPhoto = list(filter(None, resPhoto))
            if len(resPhoto) == 0:   
                try:
                    semaforr(conn, cursor, n)
                except:
                    pass 
                return print('len_=0')
            print(f"before___{len(resPhoto)}")
            resPhoto = remove_repetitions(resPhoto)
            print(f"arter___{len(resPhoto)}")

            try:
                query1 = "INSERT INTO upz_hotels_photos (hotelid, photo_id, tags, url_square60, url_max) VALUES (%s, %s, %s, %s, %s)"

                for item in resPhoto:
                    try:
                        values = (item["hotelid"], item["photo_id"], item["tags"], item["url_square60"], item["url_max"])
                        cursor.execute(query1, values)                    
                        whiteList_set.add(item["hotelid"])                 
                            
                    except Exception as ex:
                        print(ex)
                        continue

                conn.commit()
            except:
                pass
            whiteList = list(whiteList_set)
            try:
                query9 = "UPDATE upz_hotels SET fotos = %s WHERE hotel_id = %s"

                for item in whiteList:
                    try:
                        try:
                            find_query = "SELECT hotel_id FROM upz_hotels WHERE hotel_id = %s"                  
                            cursor.execute(find_query, (item,))                      
                            row = cursor.fetchone()                   
                        except Exception as ex:
                            print(f"db_writerr__str87__{ex}")

                        if row:
                            try:                          
                               cursor.execute(query9, (1, item))                      
                            except Exception as ex:
                                print(f"db_writerr__str90__{ex}")
                    except Exception as ex:
                        print(f"db_writerr__str95__{ex}")
                        continue

                conn.commit()
            except Exception as ex:
                print(ex)
       
            try:
                semaforr(conn, cursor, n)
            except:
                pass

        except Exception as ex:
            print(ex)

        try:
            cursor.close()
            conn.close()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    except:
        pass
    return

def semaforr(conn, cursor, n):  
    print(n)
    try:
        select_queryF = "SELECT fotos_flag FROM hotels_simafor WHERE id = %s"
        cursor.execute(select_queryF, (n,))
        row = cursor.fetchone()

        if row:
            update_query = "UPDATE hotels_simafor SET fotos_flag = %s WHERE id = %s"
            cursor.execute(update_query, (1, n))
            conn.commit()  
            print('hello simafor commit!')      

    except Exception as ex:
        print(ex)

def remove_repetitions(data):
    unique_values = set()
    result = []
    for item in data:
        unil_value = item.get("photo_id")
        if unil_value not in unique_values:
            result.append(item)
            unique_values.add(unil_value)
    return result











# total = None
# db_opener(total)

# python db_writerrr.py

# resRoomHighlights = []
# with open('result_description__interval_0__1120__Items_982.json', 'r') as f:
#     data_result_descript = json.load(f)
# with open('photos__12_05_2023__16_32__443.json', 'r') as f:
#     resPhoto = json.load(f) 
# with open('facilities__12_05_2023__16_32__1030.json', 'r') as f:
#     resFacilities = json.load(f) 
# with open('room__12_05_2023__16_31__62.json', 'r') as f:
#     resRooms = json.load(f) 
# with open('room_block__12_05_2023__16_31__62.json', 'r') as f:
#     resRoomsBlock = json.load(f)
    # print(resRoomsBlock)



# try:
#     with open(f'photo5.json', "w", encoding="utf-8") as file:
#         json.dump(resPhoto, file, indent=4, ensure_ascii=False)
# except Exception as ex:
#     print(f"str348__{ex}")   


# query = "UPDATE result_description_test1 SET hotelid = %s, enusname = %s"
