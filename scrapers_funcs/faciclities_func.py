# import main
from bs4 import BeautifulSoup
import re
from . import facilities_data


def page_scraper_facilities(resHtml, hotelid):
    # print('hello faci')
    result_facilities_upz = []
    result_facilities_upz_list = []
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")     
    except Exception as ex:
        # print(f"str102___{ex}") 
        return None

    try:     
        span_tag = soup1.find('span', attrs={'data-testid': 'facility-group-icon'})
        parent_div = span_tag.find_parent('div')
        parent_class = parent_div['class'][0]
        # print(parent_class)
        # facilities_block_pre = soup1.find_all('div', class_= parent_div)
        parent_div_main = parent_div.find_parent('div').find_parent('div').find_parent('div').get('class')[0]
        facilities_list = soup1.find_all('div', class_=parent_div_main)
        for item in facilities_list:

            try:
                name = ''                
                name = item.find('div', class_= parent_class).get_text().strip()
            except Exception as ex:
                name = 'not found' 
                # print(f"str129___{ex}")
            try:
                facilitytype_id = ''
                for key, value in facilities_data.hotelfacility_gen_en.items():
                    if re.search(f'{value}', name):
                        facilitytype_id = key
                        break
                if facilitytype_id == '':
                    for key, value in facilities_data.hotelfacility_gen_en.items():
                        if re.search(f'{name}', value):
                            facilitytype_id = key
                            break
            except Exception as ex:
                facilitytype_id = 'not found'         

            try:
                facilitytype_name_list = []
                facilitytype_name = ''
                uniq = ''               
                facilitytype_name_block = item.find_all('li')
                for i, li in enumerate(facilitytype_name_block):
                    uniq = f"{hotelid}_{i}"
                    facilitytype_name = li.get_text(strip=True, separator="\n")               
                    try:
                        hotelfacilitytype_id = ''
                        for key, value in facilities_data.hotelfacility_local_en.items():
                            if re.search(f'{value}', facilitytype_name):
                                hotelfacilitytype_id = key
                                break
                        
                        if  hotelfacilitytype_id == '':
                            for key, value in facilities_data.hotelfacility_local_en.items():
                                if re.search(f'{facilitytype_name}', value):
                                    hotelfacilitytype_id = key
                                    break
                        if  hotelfacilitytype_id == '':
                            for key, value in facilities_data.roomfacility.items():
                                if re.search(f'{value}', facilitytype_name):
                                    hotelfacilitytype_id = key
                                    break
                        if  hotelfacilitytype_id == '':
                            for key, value in facilities_data.roomfacility.items():
                                if re.search(f'{facilitytype_name}', value):
                                    hotelfacilitytype_id = key
                                    break
                    except:
                        hotelfacilitytype_id = 'not found'
                    
                    facilitytype_name_list.append({                        
                        'facilitytype_name': facilitytype_name,
                        'hotelfacilitytype_id': hotelfacilitytype_id,
                        "uniq": uniq, 
                    })
                # print(cons)
            except Exception as ex:
                facilitytype_name = 'not found' 
                # print(f"str129___{ex}") 

            result_facilities_upz_list.append({                
                "name": name, 
                "facilitytype_id": facilitytype_id, 
                'facilitytype_name_list': facilitytype_name_list,               
               
            })
            # print(len(result_review_upz_list))
    except Exception as ex:
        # print(f"str226___{ex}") 
        return None
        # pass
    try:
        result_facilities_upz.append({
            "id":"",
            "hotelid": hotelid,
            "result_review_upz_list": result_facilities_upz_list,            
        })
    except Exception as ex:
        # print(f"str226___{ex}") 
        return None
        # pass
    try:
        return result_facilities_upz[0]
    except:
        return None


