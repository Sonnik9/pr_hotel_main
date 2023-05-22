from bs4 import BeautifulSoup
import re
from . import facilities_data

def page_scraper_room_block(resHtml, hotelid):
    meal_facilities_const = [1, 166, 167, 168, 169, 170, 171, 217, 218, 219, 220]
    result_room_block_upz = []
    # print('hello room block')

    try:   
        soup1 = BeautifulSoup(resHtml, "lxml")      
    except Exception as ex:
        # print(f"str102___{ex}") 
        return None 

    try:
        all_sripts_list = []
        scripts_fraction_list = []
        all_scripts_str = ''
        all_sripts_list = soup1.find_all('script')
        for fr in all_sripts_list:
            all_scripts_str += str(fr) + '\n'
        scripts_fraction_list = all_scripts_str.split('{}')           
        section = soup1.find('section', class_='roomstable')
        list_elements = section.find_all('div', recursive=False)
        for i, item in enumerate(list_elements):
            try:
                room_id = ''
                name_room = ''
                gross_price = 'api info'
                currency = 'api info'
                max_occupancy = 0
                nr_children = 0
                nr_adults = 0
                mealplan = ''
                all_inclusive = ''
                room_surface_in_m2 = '' 
                # all_facilities_of_room = ''            
                try:
                    room_id_pre = item.find('a').get('href')            
                    room_id = re.findall('\d+', room_id_pre)[0]                
                except:
                    room_id = ''
                    continue
    
                try:
                    name_room_pre = item.find('a')
                    name_room = name_room_pre.get_text(strip=True, separator="\n")
                except:
                    name_room = ''
                    continue
                try:
                    for element in item.find_all(True):
                        aria_label = element.get('aria-label')
                        if aria_label:
                            max_occupancy1 = aria_label.strip()                     
                            break
                except:
                    max_occupancy1 = ''
                try:            
                    pattern1 = f'"roomId":{room_id}.*__typename":"RTRoomCard".*"description".*"hasRoomInventory".*' 
                    # pattern_meal = r'(?:"mealPlans"::\[[^]]*?\]|"mealPlans":^\[\s*\]$)'
                    pattern_meal = f'"facilities":\[[^]]*?\]'
                    for fr in scripts_fraction_list:
                        match1 = re.search(pattern1, fr)                                   
                        if match1:
                            match_general_block = match1.group()

                            try:
                                match_allow_children = re.search(r'"maxChildren":\d', match_general_block)
                                nr_children = match_allow_children.group().split(':')[1].strip() 
                            except:
                                nr_children = 0
                            try:
                                match_nr_adults = re.search(r'"maxPersons":\d', match_general_block)
                                nr_adults = match_nr_adults.group().split(':')[1].strip() 
                            except:
                                nr_adults = 0
                            try:
                                match2 = re.findall(pattern_meal, str(match_general_block))
                                list_fs_meal = []
                                meal_facilities_set_list = []
                                if match2:
                                    for mf in match2:
                                        list_fs_meal += eval(mf.split(':')[1].strip())
                                meal_facilities_set_list = list(set(list_fs_meal))
                                common_facilities_items = [item for item in meal_facilities_const if item in meal_facilities_set_list]
                                if common_facilities_items:
                                    for fs in common_facilities_items:
                                        mealplan += facilities_data.roomfacility[str(fs)] +'\n' 
                                else:
                                    mealplan = ""
                            except:
                                mealplan = ""
                    try:
                        max_occupancy = nr_children + nr_adults
                    except:
                        max_occupancy = 0
            
                except:
                    try:       
                        nr_children = int(max_occupancy1.split(',')[1].strip())                  
                    except: 
                        nr_children = 0                
                    try:
                        nr_adults = int(max_occupancy1.split(',')[0].strip())
                    except:
                        nr_adults = 0     
                    try:
                        max_occupancy = nr_children + nr_adults
                    except:
                        max_occupancy = 0      
                try:
                    result_room_block_upz.append({
                        "hotelid": int(hotelid),
                        'room_id': int(room_id),                    
                        # 'gross_price': float(gross_price), 
                        # 'currency': currency,  
                        'room_name': name_room,                  
                        'nr_children': int(nr_children),
                        'max_occupancy': int(max_occupancy),
                        'mealplan': mealplan,
                        # 'room_surface_in_m2': float(room_surface_in_m2),
                        'nr_adults': int(nr_adults),
                        # 'all_inclusive': int(all_inclusive),

                    })
                except Exception as ex:
                    # print(f"150____{ex}") 
                    pass
                    # return None 
            except:
                continue
    except:
        # print(f"154____{ex}")
        # pass
        return None
    try:
        # print(result_room_block_upz)
        return result_room_block_upz
    except:
        return None

# python rooms_block_func.py






# try:
#     for fs in meal_facilities_set_list:
#         all_facilities_of_room += facilities_data.roomfacility[str(fs)] +'\n'
# except:
#     all_facilities_of_room = "not found"    
#                     # 'all_facilities_of_room': str(all_facilities_of_room),  