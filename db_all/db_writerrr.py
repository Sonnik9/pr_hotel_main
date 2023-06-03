from . import photos_writerr, descr_writerr, facility_writerr, rooms_writerr 

def db_wrtr(total, n2):
    print('hello db_writerr')
    print(len(total))
    resPhoto = []
    resDescription = []
    resFacilities = []
    resRooms = []
    resRoomsBlock = []
    try:
        n = int(int(n2)/1000)
    except:
        pass

    try:
        for t in total:
            try:
                resPhoto += t[0]
            except:
                continue

        resPhoto = list(filter(None, resPhoto))   
        photos_writerr.photo_db_wrtr(resPhoto, n)
    except:
        pass
    try:
        for t in total:
            try:
                resDescription += t[1]
            except Exception as ex:
                continue

        resDescription = list(filter(None, resDescription))
        descr_writerr.descr_db_wrtr(resDescription, n)
    except:
        pass 
    try:
        for t in total:
            try:
                resFacilities += t[2]
            except:
                continue
        resFacilities = list(filter(None, resFacilities))
        facility_writerr.facility_db_wrtr(resFacilities, n)
    except:
        pass
    try:            
        for t in total:
            try:
                resRooms += t[3]
            except:
                continue
        for t in total:
            try:
                resRoomsBlock += t[4]
            except:
                continue            
        try:
            resRooms = list(filter(None, resRooms))
            resRoomsBlock = list(filter(None, resRoomsBlock))
        except:
            pass
        rooms_writerr.rooms_db_wrtr(resRooms, resRoomsBlock, n)
    except:
        pass  

    return




# def db_wrtr(total):
#     import json
#     import datetime
#     import mysql.connector
#     from mysql.connector import connect, Error 
#     from . import config_real
#     print('hello db_writerr')

#     config = {
#         'user': config_real.user,
#         'password': config_real.password,
#         'host': config_real.host,
#         'port': config_real.port,
#         'database': config_real.database,      
#     }

#     try:
#         conn = mysql.connector.connect(**config)      
#         print("Writerr connection established2")
#     except Error as e:
#         print(f"Error connecting to MySQL: {e}")
    
#     try:
#         cursor = conn.cursor() 
#     except Error as e:
#         print(f"Error connecting to MySQL: {e}")

#     print(len(total))
#     resPhoto = []
#     resDescription = []
#     resFacilities = []
#     resRooms = []
#     resRoomsBlock = []
#     photos_white = []
#     deskr_white = []
#     facil_white = []
#     room_white = []
#     roomBlock_white = []
#     set_id_list = set()
#     id_list = []

#     whiteList = []
#     try:
#         for t in total:
#             try:
#                 resPhoto += t[0][0]
#             except:
#                 continue

#         resPhoto = list(filter(None, resPhoto))

#         try:
#             with open(f'photo4.json', "w", encoding="utf-8") as file:
#                 json.dump(resPhoto, file, indent=4, ensure_ascii=False)
#         except Exception as ex:
#             print(f"str348__{ex}")
#         # return

#         try:
#             query1 = "INSERT INTO upz_hotels_photos_test1 (hotelid, photo_id, tags, url_square60, url_max) VALUES (%s, %s, %s, %s, %s)"

#             for item in resPhoto:
#                 try:
#                     values = (item["hotelid"], item["photo_id"], item["tags"], item["url_square60"], item["url_max"])
#                     cursor.execute(query1, values)
#                     photos_white.append(item["hotelid"])
#                     set_id_list.add(item["hotelid"])
#                 except Exception as ex:
#                     print(ex)
#                     continue

#             conn.commit()
#         except:
#             pass

#         for t in total:
#             try:
#                 resDescription.append(t[0][1])
#             except Exception as ex:
#                 continue

#         resDescription = list(filter(None, resDescription))

#         try:
#             query2 = "INSERT INTO upz_hotels_description_test1 (hotelid, runame, dename, frname, enusname, esname, ptptname, itname, trname, arname, zhcnname, idname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

#             for item in resDescription:
#                 try:
#                     values = (item["hotelid"], item["runame"], item["dename"], item["frname"], item["enusname"], item["esname"], item["ptptname"], item["itname"], item["trname"], item["arname"], item["zhcnname"], item["idname"])
#                     cursor.execute(query2, values)
#                     deskr_white.append({
#                         "hotelid": item["hotelid"],
#                         "checkin": item["checkin"],
#                         "checkout": item["checkout"]
#                     })
#                     set_id_list.add(item["hotelid"])
#                 except Exception as ex:
#                     print(ex)
#                     continue

#             conn.commit()
#         except:
#             pass

#         for t in total:
#             try:
#                 resFacilities += t[0][2]
#             except:
#                 continue

#         resFacilities = list(filter(None, resFacilities))

#         try:
#             query3 = "INSERT INTO upz_hotels_facilityties_test1 (hotelid, facilitytype_id, name, facilitytype_name, hotelfacilitytype_id, uniq) VALUES (%s, %s, %s, %s, %s, %s)"

#             for item in resFacilities:
#                 try:
#                     values = (item["hotelid"], item["facilitytype_id"], item["name"], item["facilitytype_name"], item["hotelfacilitytype_id"], item["uniq"])
#                     cursor.execute(query3, values)
#                     facil_white.append(item["hotelid"])
#                     set_id_list.add(item["hotelid"])
#                 except Exception as ex:
#                     print(ex)
#                     continue
#             conn.commit()
#         except:
#             pass

#         for t in total:
#             try:
#                 resRooms += t[0][3]
#             except:
#                 continue

#         resRooms = list(filter(None, resRooms))

#         try:
#             query4 = "INSERT INTO upz_hotels_rooms_test1 (hotelid, roomid, endescription, allow_children, photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, private_bathroom_highlight, bed_configurations) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

#             for item in resRooms:
#                 try:
#                     values = (item["hotelid"], item["roomid"], item["endescription"], item["allow_children"], item["photo1"], item["photo2"], item["photo3"], item["photo4"], item["photo5"], item["photo6"], item["photo7"], item["photo8"], item["photo9"], item["photo10"], item["private_bathroom_highlight"], item["bed_configurations"])
#                     cursor.execute(query4, values)
#                     room_white.append(item["hotelid"])
#                     set_id_list.add(item["hotelid"])
#                 except Exception as ex:
#                     print(ex)
#                     continue

#             conn.commit()
#         except:
#             pass

#         for t in total:
#             try:
#                 resRoomsBlock += t[0][4]
#             except:
#                 continue

#         resRoomsBlock = list(filter(None, resRoomsBlock))

#         try:
#             query5 = "INSERT INTO upz_hotels_rooms_blocks_test1 (hotelid, room_id, room_name, nr_children, max_occupancy, mealplan, nr_adults) VALUES (%s, %s, %s, %s, %s, %s, %s)"

#             for item in resRoomsBlock:
#                 try:
#                     values = (item["hotelid"], item["room_id"], item["room_name"], item["nr_children"], item["max_occupancy"], item["mealplan"], item["nr_adults"])
#                     cursor.execute(query5, values)
#                     roomBlock_white.append(item["hotelid"])
#                     set_id_list.add(item["hotelid"])
#                 except Exception as ex:
#                     print(ex)
#                     continue

#             conn.commit()
#         except Exception as ex:
#             print(ex)        

        
#         # print(current_date)

#         try:
#             current_date = datetime.datetime.now().strftime("%Y-%m-%d")
#             id_list = list(set_id_list)         
#             room_white_total = [item for item in roomBlock_white if item in room_white]
#             whiteList = []

#             for item in id_list:
#                 whiteItem = {}
#                 done_count = 0      
#                 checkin = '00:00:00'
#                 checkout = '00:00:00'
#                 flagDeskChecker = False
#                 whiteItem["hotelid"] = item
               

#                 if item in photos_white:
#                     whiteItem["fotos"] = 1
#                     done_count +=1
#                 else:
#                     whiteItem["fotos"] = 0
#                 for deskr in deskr_white:
#                     if item == deskr["hotelid"]:
#                         # print('hello deskr')
#                         whiteItem["description"] = 1
#                         checkin = deskr["checkin"]
#                         checkout = deskr["checkout"]                     
#                         done_count +=1
#                         flagDeskChecker = True
#                         break
                    
#                 else:
#                     whiteItem["description"] = 0

#                 if item in facil_white:
#                     whiteItem["facility"] = 1
#                     done_count +=1
#                 else:
#                     whiteItem["facility"] = 0

#                 if item in room_white_total:
#                     whiteItem["room"] = 1
#                     done_count +=1
#                 else:
#                     whiteItem["room"] = 0

#                 if done_count > 0:
#                     whiteItem["done"] = 1
#                 else:
#                     whiteItem["done"] = 0

#                 if done_count == 4 and flagDeskChecker == True:
#                     whiteItem["updated"] = current_date
#                     whiteItem["checkin"] = checkin
#                     whiteItem["checkout"] = checkout
#                 else:
#                     whiteItem["updated"] = '0000-00-0'
#                     whiteItem["checkin"] = '00:00:00'
#                     whiteItem["checkout"] = '00:00:00'
                    
#                 whiteList.append(whiteItem)

#         except Exception as ex:
#             print(ex)
#         print(whiteList)

#         try:
#             query9 = "UPDATE upz_hotels_copy SET fotos = %s, description = %s, facility = %s, room = %s, checkin = %s, checkout = %s, updated = %s, done = %s WHERE hotel_id = %s"

#             for item in whiteList:
#                 try:
#                     try:
#                         find_query = "SELECT hotel_id FROM upz_hotels_copy WHERE hotel_id = %s"
#                         # print("true1")
#                         cursor.execute(find_query, (item["hotelid"],))
#                         # print("true2")
#                         row = cursor.fetchone()
#                         # print("true3")
#                     except Exception as ex:
#                         print(f"db_writerr__str87__{ex}")

#                     if row:
#                         try:
#                         #    print('true4')
#                            cursor.execute(query9, (item["fotos"], item["description"], item["facility"], item["room"], item["checkin"], item["checkout"], item["updated"], item["done"], item["hotelid"]))
#                         #    print('true5')
#                         except Exception as ex:
#                             print(f"db_writerr__str90__{ex}")

#                     else:
#                         print(f"No row found for hotel_id: {item['hotelid']}")
#                 except Exception as ex:
#                     print(f"db_writerr__str95__{ex}")
#                     continue

#             conn.commit()
#         except Exception as ex:
#             print(ex)

#     except Exception as ex:
#         print(ex)

#     try:
#         cursor.close()
#         conn.close()
#     except Error as e:
#         print(f"Error connecting to MySQL: {e}")

#     return 

# # total = None
# # db_opener(total)

# # python db_writerrr.py



# # resRoomHighlights = []
# # with open('result_description__interval_0__1120__Items_982.json', 'r') as f:
# #     data_result_descript = json.load(f)
# # with open('photos__12_05_2023__16_32__443.json', 'r') as f:
# #     resPhoto = json.load(f) 
# # with open('facilities__12_05_2023__16_32__1030.json', 'r') as f:
# #     resFacilities = json.load(f) 
# # with open('room__12_05_2023__16_31__62.json', 'r') as f:
# #     resRooms = json.load(f) 
# # with open('room_block__12_05_2023__16_31__62.json', 'r') as f:
# #     resRoomsBlock = json.load(f)
#     # print(resRoomsBlock)


#             # query = "UPDATE result_description_test1 SET hotelid = %s, enusname = %s"
