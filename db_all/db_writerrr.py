def db_wrtr(total, n2):
    import json
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real
    print('hello db_writerr rew')

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database, 
        # 'charset': 'utf8mb4'     
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Writerr connection established2")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    print(len(total))
    # print(total)
    n = n2/1000
    resReviews = []
    rew_whiteList_set = set()
    rew_whiteList = []
    try:
        for t in total:
            try:
                resReviews += t
            except Exception as ex:
                # print(f"writerr__str13__{ex}")
                continue   
        try:
            resReviews = list(filter(None, resReviews))
        except:
            pass
        if len(resReviews) == 0:
            return

        try:
            query7 = "INSERT INTO upz_hotels_review_test1 (hotelid, title, cons, pros, dt1, average_score, author_name, room_id, checkin, checkout, languagecode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                  
            for item in resReviews:
                try:
                    values = (item["hotelid"], item["title"], item["cons"], item["pros"], item["dt1"], item["average_score"], item["author_name"], item["room_id"], item["checkin"], item["checkout"], item["languagecode"])
                    cursor.execute(query7, values)
                    rew_whiteList_set.add(item["hotelid"])           
                except Exception as ex:
                    print(f"db_writerr__str65__{ex}")
                    continue
            conn.commit()
        except:
            pass
        try:
            query7 = "INSERT INTO upz_hotels_review (hotelid, title, cons, pros, dt1, average_score, author_name, room_id, checkin, checkout, languagecode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                  
            for item in resReviews:
                try:
                    values = (item["hotelid"], item["title"], item["cons"], item["pros"], item["dt1"], item["average_score"], item["author_name"], item["room_id"], item["checkin"], item["checkout"], item["languagecode"])
                    cursor.execute(query7, values)
                    rew_whiteList_set.add(item["hotelid"])           
                except Exception as ex:
                    print(f"db_writerr__str65__{ex}")
                    continue
            conn.commit()
        except:
            pass
        rew_whiteList = list(rew_whiteList_set)
        try:
            query9 = "UPDATE upz_hotels SET otziv = %s WHERE hotel_id = %s"

            for item in rew_whiteList:
                try:
                    try:
                        find_query = "SELECT hotel_id FROM upz_hotels WHERE hotel_id = %s"
                        # print("true1")
                        cursor.execute(find_query, (item,))
                        # print("true2")
                        row = cursor.fetchone()
                        # print("true3")
                    except Exception as ex:
                        print(f"db_writerr__str87__{ex}")

                    if row:
                        try:
                        #    print('true4')
                           cursor.execute(query9, (1, item))
                        #    print('true5')
                        except Exception as ex:
                            print(f"db_writerr__str90__{ex}")

                    else:
                        print(f"No row found for hotel_id: {item['hotelid']}")
                except Exception as ex:
                    print(f"db_writerr__str95__{ex}")
                    continue

            conn.commit()
        except Exception as ex:
            print(f"An error occurred: {ex}")

        
        try:
            select_queryF = "SELECT otziv_flag FROM hotels_simafor WHERE id = %s"
            cursor.execute(select_queryF, (n,))
            row = cursor.fetchone()

            if row:
                update_query = "UPDATE hotels_simafor SET otziv_flag = %s WHERE id = %s"
                cursor.execute(update_query, (1, n))
                conn.commit()        

        except Exception as ex:
            print(ex)        

    except Exception as ex:
        print(f"db_writerr__str63__{ex}")
        # pass
    try:
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    return 























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
                        # pros_value = item["pros"].encode('utf8', 'ignore').decode('utf8')
                    # except:
