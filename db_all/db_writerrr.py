def db_wrtr(total, n2):
    import json
    import datetime
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real
    print('hello db_writerr_descript')

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
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
    resDescription = []
    whiteList = []
    n = n2/1000
    try:
        for t in total:
            try:
                resDescription += t[0]
            except Exception as ex:
                continue

        resDescription = list(filter(None, resDescription))

        try:
            query2 = "INSERT INTO upz_hotels_description_test1 (hotelid, runame, dename, frname, enusname, esname, ptptname, itname, trname, arname, zhcnname, idname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            for item in resDescription:
                try:
                    values = (item["hotelid"], item["runame"], item["dename"], item["frname"], item["enusname"], item["esname"], item["ptptname"], item["itname"], item["trname"], item["arname"], item["zhcnname"], item["idname"])
                    cursor.execute(query2, values)
                    whiteList.append({
                        "hotelid": item["hotelid"],
                        "description": 1,
                        "checkin": item["checkin"],
                        "checkout": item["checkout"]
                    })
                    # print(item["checkin"])
                    # print(item["checkout"])                  
                except Exception as ex:
                    print(ex)
                    continue

            conn.commit()
        except:
            pass
        try:
            query9 = "UPDATE upz_hotels_copy SET description = %s, checkin = %s, checkout = %s WHERE hotel_id = %s"
            # print('query9_1')

            for item in whiteList:
                try:
                    try:
                        find_query = "SELECT hotel_id FROM upz_hotels_copy WHERE hotel_id = %s"
                        # print("true1")
                        cursor.execute(find_query, (item["hotelid"],))
                        # print("true2")
                        row = cursor.fetchone()
                        # print("true3")
                    except Exception as ex:
                        print(f"db_writerr__str87__{ex}")

                    if row:
                        try:
                        #    print('true4')
                           cursor.execute(query9, (item["description"], item["checkin"], item["checkout"], item["hotelid"]))
                        #    print('true5')
                        except Exception as ex:
                            print(f"db_writerr__str90__{ex}")

                except Exception as ex:
                    print(f"db_writerr__str95__{ex}")
                    continue

            conn.commit()
        except Exception as ex:
            print(ex)

        try:
            select_queryF = "SELECT deskription_flag FROM hotels_simafor WHERE id = %s"
            cursor.execute(select_queryF, (n,))
            row = cursor.fetchone()
            # print('helo simafor')
            if row:
                update_query = "UPDATE hotels_simafor SET deskription_flag = %s WHERE id = %s"
                cursor.execute(update_query, (1, n))
                conn.commit()
        except Exception as ex:
            print(ex)
    except Exception as ex:
        print(ex)
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


            # query = "UPDATE result_description_test1 SET hotelid = %s, enusname = %s"
