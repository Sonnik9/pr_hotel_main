def db_wrtr(total, n2):
    try:
        import time
        import mysql.connector
        from mysql.connector import connect, Error 
        from . import config_real
        print('hello db_writerr')

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
                print("Writerr connection established fotos")
                break
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                time.sleep(3)
                continue
            
        try:
            cursor = conn.cursor() 
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
                # time.sleep(3)
                   
        try:
            print(len(total))
            resPhoto = []       
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

        except:
            pass
        try:
            whiteList = writerr_table(conn, cursor, resPhoto)
        except:
            pass
        try:
            changing_hotelsCritery(cursor, conn, whiteList)   
        except:
            pass
        try:
           semaforr(conn, cursor, n)
        except:
            pass 
        try:
            cursor.close()
            conn.close()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    except:
        pass
    return

def writerr_table(conn, cursor, resPhoto):
    whiteList = []
    photo_white = []
    photo_white_add = []
    photo_white_set = set()

    try:
        query1 = "INSERT INTO upz_hotels_photos (hotelid, photo_id, tags, url_square60, url_max) VALUES (%s, %s, %s, %s, %s)"              

        batch_size = 250
        batch_values = []

        for item in resPhoto:
            try:
                values = (item["hotelid"], item["photo_id"], item["tags"], item["url_square60"], item["url_max"])
                batch_values.append(values)
                photo_white_set.add(item["hotelid"])

                if len(batch_values) >= batch_size:
                    try:
                        cursor.executemany(query1, batch_values)
                        conn.commit()
                        batch_values = []
                    except Exception as ex:
                        print(f"117___{ex}")                        
                        photo_white_add = insert_rows_individually_room(conn, cursor, query1, batch_values)
                        photo_white += photo_white_add
                        batch_values = []
                        continue                   

            except Exception as ex:
                print(f"122___{ex}")
                continue

        if batch_values:
            try:
                cursor.executemany(query1, batch_values)
                conn.commit()
            except Exception as ex:
                print(f"130___{ex}")
                photo_white_add = insert_rows_individually_room(conn, cursor, query1, batch_values)
                photo_white += photo_white_add
    except Exception as ex:
        print(f"123___{ex}")
        pass

    try:
        photo_white += list(photo_white_set)
    except Exception as ex:
        print(ex)

    return whiteList


def insert_rows_individually_room(conn, cursor, query, data):
    photo_white_set = set()
    photo_white = []
    try:
        data = eval(data)
    except:
        data = data
    for hotelid, photo_id, tags, url_square60, url_max in data:
        try:
            values = (hotelid, photo_id, tags, url_square60, url_max)
            cursor.execute(query, values)            
            photo_white_set.add(hotelid)
        except Exception as ex:
            # print(f"204___: {ex}")
            continue
    try:
        conn.commit()
    except:
        photo_white = []
        return photo_white
    photo_white = list(photo_white_set)
    return photo_white

def changing_hotelsCritery(cursor, conn, whiteList):
    try:       
        query12 = "UPDATE upz_hotels SET fotos = %s WHERE hotel_id = %s"

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
                        cursor.execute(query12, (1, item))                      
                    except Exception as ex:
                        print(f"db_writerr__str90__{ex}")

            except Exception as ex:
                print(f"db_writerr__str95__{ex}")
                continue
        conn.commit()           

    except Exception as ex:
        print(ex)

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
    return 

def remove_repetitions(data):
    unique_values = set()
    result = []
    for item in data:
        unil_value = item.get("photo_id")
        if unil_value not in unique_values:
            result.append(item)
            unique_values.add(unil_value)
    return result





# def db_wrtr(total, n2):
#     try:
#         import time
#         import mysql.connector
#         from mysql.connector import connect, Error 
#         from . import config_real
#         print('hello db_writerr fotos')

#         config = {
#             'user': config_real.user,
#             'password': config_real.password,
#             'host': config_real.host,
#             'port': config_real.port,
#             'database': config_real.database,      
#         }
#         for _ in range(5):
#             try:
#                 conn = mysql.connector.connect(**config)      
#                 print("Writerr connection established2 fotos")
#             except Error as e:
#                 print(f"Error connecting to MySQL: {e}")
#                 time.sleep(3)
#                 continue
            
#             try:
#                 cursor = conn.cursor() 
#             except Error as e:
#                 print(f"Error connecting to MySQL: {e}")
#                 time.sleep(3)
#                 continue
#             break
#         try:
#             print(len(total))
#             resPhoto = []
#             whiteList_set = set()
#             whiteList = []
#             n = int(int(n2)/1000)
#         except:
#             pass
#         try:
#             for t in total:
#                 try:
#                     resPhoto += t
#                 except:
#                     continue

#             resPhoto = list(filter(None, resPhoto))
#             if len(resPhoto) == 0:   
#                 try:
#                     semaforr(conn, cursor, n)
#                 except:
#                     pass 
#                 return print('len_=0')
#             print(f"before___{len(resPhoto)}")
#             resPhoto = remove_repetitions(resPhoto)
#             print(f"arter___{len(resPhoto)}")


#             try:
#                 query1 = "INSERT INTO upz_hotels_photos (hotelid, photo_id, tags, url_square60, url_max) VALUES (%s, %s, %s, %s, %s)"              

#                 batch_size = 150
#                 batch_values = []

#                 for item in resPhoto:
#                     try:
#                         values = (item["hotelid"], item["photo_id"], item["tags"], item["url_square60"], item["url_max"])
#                         batch_values.append(values)
#                         whiteList_set.add(item["hotelid"])

#                         if len(batch_values) == batch_size:
#                             cursor.executemany(query1, batch_values)
#                             conn.commit()
#                             batch_values = []

#                     except Exception as ex:
#                         print(ex)
#                         continue

#                 if batch_values:
#                     cursor.executemany(query1, batch_values)
#                     conn.commit()
#             except:
#                 pass

#             whiteList = list(whiteList_set)
#             try:
#                 query9 = "UPDATE upz_hotels SET fotos = %s WHERE hotel_id = %s"

#                 for item in whiteList:
#                     try:
#                         try:
#                             find_query = "SELECT hotel_id FROM upz_hotels WHERE hotel_id = %s"                  
#                             cursor.execute(find_query, (item,))                      
#                             row = cursor.fetchone()                   
#                         except Exception as ex:
#                             print(f"db_writerr__str87__{ex}")

#                         if row:
#                             try:                          
#                                cursor.execute(query9, (1, item))                      
#                             except Exception as ex:
#                                 print(f"db_writerr__str90__{ex}")
#                     except Exception as ex:
#                         print(f"db_writerr__str95__{ex}")
#                         continue

#                 conn.commit()
#             except Exception as ex:
#                 print(ex)
       


#         except Exception as ex:
#             print(ex)
#         try:
#             semaforr(conn, cursor, n)
#         except:
#             pass

#         try:
#             cursor.close()
#             conn.close()
#         except Error as e:
#             print(f"Error connecting to MySQL: {e}")
#     except:
#         pass
#     return

# def semaforr(conn, cursor, n):  
#     print(n)
#     try:
#         select_queryF = "SELECT fotos_flag FROM hotels_simafor WHERE id = %s"
#         cursor.execute(select_queryF, (n,))
#         row = cursor.fetchone()

#         if row:
#             update_query = "UPDATE hotels_simafor SET fotos_flag = %s WHERE id = %s"
#             cursor.execute(update_query, (1, n))
#             conn.commit()  
#             print('hello simafor commit!')      

#     except Exception as ex:
#         print(ex)

# def remove_repetitions(data):
#     unique_values = set()
#     result = []
#     for item in data:
#         unil_value = item.get("photo_id")
#         if unil_value not in unique_values:
#             result.append(item)
#             unique_values.add(unil_value)
#     return result









