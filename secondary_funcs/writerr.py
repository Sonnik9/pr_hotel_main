def writerr(total):
    import json
    from datetime import datetime

    print(len(total))
    resPhoto = []
    resDescription = []
    resFacilities = []
    resRooms = []
    # resRoomHighlights = []
    resRoomsBlock = []

    try:
        for t in total:
            try:
                resPhoto += t[0][0]
            except:
                continue 

        try:
            resPhoto = list(filter(None, resPhoto))
            resPhoto = list(filter("", resPhoto)) 
        except:
            pass
        for t in total:
            try:
                resDescription.append(t[0][1])
            except Exception as ex:
                print(f"writerr__str30__{ex}")
                continue 
        try:
            resDescription = list(filter(None, resDescription))
            resDescription = list(filter("", resDescription)) 
        except:
            pass

        for t in total:
            try:
               resFacilities +=t[0][2]
            except:
                continue 
        try:
            resFacilities = list(filter(None, resFacilities))
            resFacilities = list(filter("", resFacilities)) 
        except:
            pass
        for t in total:
            try:
               resRooms += t[0][3]
            except:
                continue 
        try:
            resRooms = list(filter(None, resRooms))
            resRooms = list(filter("", resRooms)) 
        except:
            pass
        for t in total:
            try:
               resRoomsBlock += t[0][4]
            except:
                continue 
        try:
            resRoomsBlock = list(filter(None, resRoomsBlock))
            resRoomsBlock = list(filter("", resRoomsBlock)) 
        except:
            pass
        # for t in total:
        #     try:
        #        resRoomHighlights.append(t[0][6])
        #     except:
        #         continue 
        #     try:
        #         resRoomHighlights = list(filter(None, resRoomHighlights))
        #         resRoomHighlights = list(filter("", resRoomHighlights)) 
        #     except:
        #         pass

    except Exception as ex:
        print(f"str342__{ex}")
    
    now = datetime.now() 
    curentTimeForFile = now.strftime("%d_%m_%Y__%H_%M")

    try:
        if resPhoto != None and resPhoto != []:
            print(f"len_photos___{len(resPhoto)}")
            try:
                with open(f'./result_hotels_upz/photos__{curentTimeForFile}__{len(resPhoto)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resPhoto, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str210__{ex}")
        if resDescription != None and resDescription != []:
            print(f"len_resDescription ___{len(resDescription)}")
            try:
                with open(f'./result_hotels_upz/description__{curentTimeForFile}__{len(resDescription)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resDescription, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"writerr__str86__{ex}") 

        if resFacilities != None and resFacilities != []:
            print(f"len_resFacilities___{len(resFacilities)}")
            try:
                with open(f'./result_hotels_upz/facilities__{curentTimeForFile}__{len(resFacilities)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resFacilities, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str221__{ex}") 
        if resRooms != None and resRooms != []:
            print(f"len_resRooms___{len(resRooms)}")
            try:
                with open(f'./result_hotels_upz/room__{curentTimeForFile}__{len(resRooms)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resRooms, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str221__{ex}")

        if resRoomsBlock != None and resRoomsBlock != []:
            print(f"len_resRoomsBlock___{len(resRoomsBlock)}")
            try:
                with open(f'./result_hotels_upz/room_block__{curentTimeForFile}__{len(resRoomsBlock)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resRoomsBlock, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str221__{ex}")
    except Exception as ex:
        print(f"writerr__str136__{ex}")

