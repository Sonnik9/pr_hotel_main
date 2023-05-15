import requests
import random 
from random import choice
import time
import math
import re
import atexit
import shutil
import tempfile
import sys 
try:
    import secondary_funcs
    import scrapers_funcs
    import db_all
except Exception as ex:
    print(f"16____{ex}")

try:
   from secondary_funcs import smart_headers, b_filter_func
#    print('success secondary_funcs')
except Exception as ex:
    print(f"12____{ex}")
try:
   from scrapers_funcs import photos_func, description_func, faciclities_func, rooms_func, rooms_block_func
#    print('success scrapers_funcs') 
except Exception as ex:
    print(f"17____{ex}")

try:
   from db_all import db_reader, db_writerrr, bl_writerr
#    print('success db_all') 
except Exception as ex:
    print(f"25____{ex}")

# ////////// grendMather_controller block/////////////////////////////////////

def grendMather_controller(data):
    # print('hello controler')
    flagCount = 0
    # flagTest = True
    flag_photo = True
    flag_description = True 
    flag_facilities = True 
    flag_room = True 
    flag_room_block = True    
    black_list = []
    photoInd = 0
    descriptionInd = 0
    facilityInd = 0
    roomInd = 0
    room_blockInd = 0
    try:
        data_upz_hotels_item = data.split('SamsonovNik')[1]
    except Exception as ex:
        # print(f"48____{ex}")
        pass
    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item)
    except Exception as ex:
        # print(f"53____{ex}")
        data_upz_hotels_item_dict = data_upz_hotels_item 
    try:
        hotelid = data_upz_hotels_item_dict["hotel_id"] 
    except Exception as ex:
        # print(f"61____{ex}")
        hotelid = 'not found'
    # print(hotelid)
    try:
        prLi_str = data.split('SamsonovNik')[0]
        try:
            prLi = eval(prLi_str)
        except Exception as ex:
            # print(f"str68___{ex}")
            prLi = prLi_str
            pass
    except Exception as ex:
        # print(f"str72___{ex}")
        pass 
    try:
        link = ''
        link = data_upz_hotels_item_dict["url"] 
        try:
            fixed_url = re.sub(r'\\/', '/', link)  
        except Exception as ex:
            # print(f"74____{ex}")
            fixed_url = data_upz_hotels_item_dict["url"]
    except Exception as ex:
        # print(f"str83___{ex}")
        try:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "fotos": 0,
                "description": 0,
                "facility": 0,
                "otziv": "?",
                "room": 0,
                "room_block": 0,
            })
        except Exception as ex:
            # print(f"91____{ex}")
            pass
        return [[None], black_list] 
    try:
        photoInd = data_upz_hotels_item_dict["fotos"]
    except:
        pass 
    try:
        descriptionInd = data_upz_hotels_item_dict["description"]
    except:
        pass 
    try:
        facilityInd = data_upz_hotels_item_dict["facility"] 
    except:
        pass
    try:
        roomInd = data_upz_hotels_item_dict["room"]
    except:
        pass
    try:
        room_blockInd = data_upz_hotels_item_dict["room_block"]
    except:
        room_blockInd = None     
    # try:
    #     if photoInd == "1" or photoInd == 1:
    #         flag_photo = False
    #         flagCount += 1  
    #     if descriptionInd == "1" or descriptionInd == 1:
    #         flag_description = False
    #         flagCount += 1 
    #     if facilityInd == "1" or facilityInd == 1:
    #         flag_facilities = False
    #         flagCount += 1 
    #     if roomInd == "1" or roomInd == 1:
    #         flag_room = False
    #         flagCount += 1
    #     if room_blockInd == "1" or room_blockInd == 1:
    #         flag_room_block = False
    # except:
    #     pass
    if flagCount == 7:  
        return [[None], black_list]     
    else:
        for _ in range(2):
            try:
                result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks = '', '', '', '', ''
          
                black_list = []
                proxy_item = {       
                    "https": f"http://{choice(prLi)}"          
                } 
                # print(proxy_item)
                k = 2 / random.randrange(1, 5)
                m = 1 / random.randrange(1, 11)
                g = random.randrange(1, 5)
                n = round(g + k + m, 2) 
                time.sleep(n)  
                try:     
                    r = requests.get(fixed_url, headers=smart_headers.random_headers(), proxies=proxy_item, timeout=(3.15, 21.15))
                    r.raise_for_status()
                    print(r.status_code)
                    if r.status_code == 404: 
                        return None
                    if r.status_code == 200 and r.text is not None and r.text != '':
                        try:
                            # result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks = scraper_gr_mather_func.scraper_grendmather(r.text, hotelid, photoInd, descriptionInd, facilityInd, roomInd)
                            if flag_photo == True:
                                try:
                                    result_photos_upz = photos_func.page_scraper_photos(r.text, hotelid)
                                except:
                                    result_photos_upz = None  
                            if flag_description == True:
                                try:                       
                                    result_description_upz = description_func.page_scraper_description(r.text, hotelid)                           
                                except:
                                    result_description_upz = None 
                                    # print(result_description_upz)
                            if flag_facilities == True:
                                try:
                                    result_facilities_upz = faciclities_func.page_scraper_facilities(r.text, hotelid)
                                except:
                                    result_facilities_upz = None

                            if flag_room == True:
                                try:
                                    result_rooms_upz = rooms_func.page_scraper_room(r.text, hotelid)
                                except:
                                    result_rooms_upz = None 

                            if flag_room_block == True:
                                try:
                                    upz_hotels_rooms_blocks = rooms_block_func.page_scraper_room_block(r.text, hotelid)
                                except:
                                    upz_hotels_rooms_blocks = None 
                            if result_photos_upz is None or result_description_upz is None  or result_facilities_upz is None or result_rooms_upz is None or upz_hotels_rooms_blocks is None:
                                continue                                                  
                        except Exception as ex:
                            # print(f"str225___{ex}")
                            # continue
                            pass
                        break
                    else:
                        continue
                except requests.exceptions.HTTPError as ex:
                    print(f"str44___HTTP error occurred: {ex}") 
                    continue

            except Exception as ex:
                # print(f"237____{ex}")
                continue
                # return [[None], black_list] 
        if flag_photo == True and result_photos_upz is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "fotos": 0,
            })
        if flag_description == True and result_description_upz is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "description": 0,
            })

        if flag_facilities == True and result_facilities_upz is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "facility": 0,
            }) 
        if flag_room == True and result_rooms_upz is None:
            # print("room condition")
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "room": 0,
            })

        if flag_room == True and upz_hotels_rooms_blocks is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "room_block": 0,
            })        
        try:
            return [[result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks], black_list] 
        
        except Exception as ex:
            # print(f"220____{ex}")
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "fotos": 0,
                "description": 0,
                "facility": 0,
                "otziv": "?",
                "room": 0,
                "room_block": 0,
            })
            return [[None], black_list] 
        
# ////////// grendMather_controller block end/////////////////////////////////////
#         
def proxy_reader():
    with open("proxy_booking.txt", encoding="utf-8") as f1:    
        prLi = ''.join(f1.readlines()).split('\n')
        prLi= list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
    return prLi

def father_multiprocessor(data_upz_hotels, cpu_count):
    # import mpire
    print('hello multi')
    from mpire import WorkerPool   
    # n = multiprocessing.cpu_count() * 10  
    # print(data_upz_hotels)
    try:
        data_upz_hotels_new = eval(data_upz_hotels) 
    except Exception as ex:
        # print(f"277____{ex}")
        data_upz_hotels_new = data_upz_hotels
    try:
        prLi = proxy_reader()
    except Exception as ex:
        # print(f"283____{ex}")
        pass
    # try:
    #     cpu_count = int(cpu_count)
    # except:
    #     return None
    try:        
        data_upz_hotels_args = list(f"{prLi}SamsonovNik{item}" for item in data_upz_hotels_new)
    except Exception as ex:
        # print(f"288____{ex}")
        pass
    try:
        with WorkerPool(n_jobs = cpu_count) as p2:
            # print('hello multi')                                
            finRes = p2.map(grendMather_controller, data_upz_hotels_args)
    except Exception as ex:
        print(f"295____{ex}")
        pass
    # writerr.writerr(finRes) 
    try:  
        return finRes
    except Exception as ex:
        # print(f"300____{ex}")
        return None

def pattern_cycles(data, cpu_count):
    print('helo pattern_cycles')
    finRes = []
    black_list = []
    try:
        finRes = father_multiprocessor(data, cpu_count)
    except Exception as ex:
        print(f"422____{ex}")
        pass
    # try:
    #     writerr.writerr(finRes)
    # except Exception as ex:
    #     # print(f"378____{ex}")
    #     pass
    try:
        db_writerrr.db_wrtr(finRes)
    except Exception as ex:
        # print(f"378____{ex}")
        pass
    try:
        black_list = b_filter_func.black_filter(finRes) 
    except Exception as ex:
        # print(f"390____{ex}")
        pass
    try:
       return black_list
    except:
        return None

def cycles_worker(exeptions_data, n1, n2, len_const_data, counter, flag_end_cycles, cpu_count):   
    black_list = []
    ex_list = []

    try:
        for item in exeptions_data:
            ex_list += item
    except:
        pass
    try:
        if flag_end_cycles == True:
            print('hello end_flag_cycles')
            try:
                black_list = pattern_cycles(ex_list, cpu_count)
                # try:
                #    b_writerr_func.b_w_writerr(black_list)
                # except Exception as ex:
                #    print(f"351____{ex}") 
                try:
                   bl_writerr.bl_db_wrtr(black_list)
                except Exception as ex:
                   print(f"355____{ex}") 
                cleanup_cache()
            except Exception as ex:
                print(f"358____{ex}")

            return print('Finish')
        else:            
            try:
                counter +=1
                n1 = (counter*1000) - 1000 + 1
                n2 = counter*1000

                interval_chekcer = len_const_data - n2
                if interval_chekcer <= 1000:
                    n2 = len_const_data
                    flag_end_cycles = True
                else:
                    pass

                    # print(f"362___{n2}")
            except Exception as ex:
                # print(f"343____{ex}")
                pass
            # print(f"348___{n1, n2}")

            if len(ex_list) != 1000 and len(ex_list) < 1000:
                try:       
                    # const_data = json_reader_test.data_upz_hotels_func()    
                    const_data = db_reader.db_opener(n1, n2)
                    # print(const_data)
                except Exception as ex:
                    print(f"443____{ex}")
                try:
                    black_list = pattern_cycles(const_data, cpu_count)
                except:
                    pass
                try:
                    exeptions_data.append(black_list)
                except Exception as ex:
                    # print(f"398____{ex}")
                    pass
                try:
                    cycles_worker(exeptions_data, n1, n2, len_const_data, counter, flag_end_cycles, cpu_count) 
                except Exception as ex:
                    # print(f"408____{ex}")
                    pass
            elif len(ex_list) == 1000 or len(ex_list) > 1000:
                # print('hello exlist')
                exeptions_data = []
                black_list = pattern_cycles(ex_list, cpu_count)   
                # try:             
                #     b_writerr_func.b_w_writerr(black_list)
                # except Exception as ex:
                #     print(f"408____{ex}")
                try:
                    bl_writerr.bl_db_wrtr(black_list)
                except Exception as ex:
                    print(f"412____{ex}") 
                # bl_db_wrtr(black_list)
                try:
                    cycles_worker(exeptions_data, n1, n2, len_const_data, counter, flag_end_cycles, cpu_count) 
                except Exception as ex:
                    # print(f"408____{ex}")
                    pass

    except Exception as ex:
        # print(f"334____{ex}")
        pass

def cleanup_cache():
    import os
    try:
        cache_dir = tempfile.mkdtemp()
    except Exception as ex:
        # print(f"386____{ex}")
        pass    
    try:
        if os.path.exists("__pycache__"):
            shutil.rmtree("__pycache__")
    except Exception as ex:
        # print(f"392____{ex}")
        pass  
    try:
        if os.path.exists("./secondary_funcs/__pycache__"):
            shutil.rmtree("./secondary_funcs/__pycache__")
    except Exception as ex:
        print(f"445____{ex}")
        pass 
    try:
        if os.path.exists("./scrapers_funcs/__pycache__"):
            shutil.rmtree("./scrapers_funcs/__pycache__")
    except Exception as ex:
        print(f"451____{ex}")
        pass 
    try:
        if os.path.exists("./db_all/__pycache__"):
            shutil.rmtree("./db_all/__pycache__")
    except Exception as ex:
        print(f"457____{ex}")
        pass  
    # secondary_funcs  
    try:
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
    except Exception as ex:
        # print(f"396____{ex}")
        pass

def speed_determinants():
    len_items = input("Please enter the length of source table", )
    try:
        len_items = int(len_items.strip())
    except:        
        len_items = 10000
    cpu_count = input('Please enter cpu_count', )
    try:
        cpu_count = int(cpu_count.strip())
    except:        
        cpu_count = 30
    return len_items, cpu_count
  
def main():   
    n1 = 0
    n2 = 1000
    counter = 0
    exeptions_data = [] 
    flag_end_cycles = False
    len_items, cpu_count = 10000, 12

    try:
        cycles_worker(exeptions_data, n1, n2, len_items, counter, flag_end_cycles, cpu_count)
    except Exception as ex:
        print(f"454____{ex}")

if __name__ == "__main__":
    # import pyperclip
    start_time = time.time() 
    try:
        atexit.register(cleanup_cache)
    except Exception as ex:
        print(f"461____{ex}")
    main() 
    # cleanup_cache()
    # pyperclip.copy('')
    # clipboard_text = pyperclip.paste()
    finish_time = time.time() - start_time
    print(f"Total time:  {math.ceil(finish_time)} сек")
    try:
        sys.exit()
    except Exception as ex:
        print(f"467____{ex}")





# u9FSEvF3:igzQ94p1@45.132.207.81:62036
# u9FSEvF3:igzQ94p1@154.7.205.72:64700
# u9FSEvF3:igzQ94p1@154.7.207.155:63732



# u9FSEvF3:igzQ94p1@185.97.76.249:62362
