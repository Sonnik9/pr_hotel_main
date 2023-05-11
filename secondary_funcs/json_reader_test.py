import json

def data_upz_hotels_func():
    data_upz_hotels_renevate = []
    n1 = 0
    n2 = 24
    with open('./source/hotels_copy1.json', 'r') as f:
        data_upz_hotels = json.load(f)[n1:n2]
        # for item in data_upz_hotels:
        #     data_upz_hotels_renevate.append(
        #         { 
        #         "id": item["id"],    
        #         "hotel_id": item["hotel_id"],
        #         "url": item["url"],
        #         "facility": item["facility"],
        #         "room": item["room"],
        #         "fotos": item["fotos"],
        #         "description": item["description"],
        #         "otziv": item["otziv"],
        #         }
        #     )

        # return data_upz_hotels_renevate
        return data_upz_hotels


# python json_reader_test.py
