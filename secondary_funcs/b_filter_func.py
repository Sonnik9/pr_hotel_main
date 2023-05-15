def black_filter(finRes):
    print('helo secondary_funcs____black_filter')
    d_lackList = []
    sorted_blackList = []
    refactor_blackList = []

    for t in finRes:
        try:
           d_lackList.append(t[1])
        except Exception as ex:
            print(f"secondary_funcs____black_filter__11____{ex}")
            continue
    try:
        d_lackList = list(filter(None, d_lackList))                
        d_lackList = list(filter([], d_lackList))
    except Exception as ex:
        print(f"secondary_funcs____black_filter__17____{ex}")
    try:
        for lst in d_lackList:
            merged_dict = {}
            for dct in lst:
                try:
                    hotel_id = dct["hotel_id"]
                    url = dct["url"]
                except Exception as ex:
                    print(f"b_filter_func___24{ex}")
                if hotel_id not in merged_dict:
                    merged_dict[hotel_id] = {"hotel_id": hotel_id, "url": url}
                merged_dict[hotel_id][list(dct.keys())[2]] = dct[list(dct.keys())[2]]
            sorted_blackList.append(list(merged_dict.values()))
        for item in sorted_blackList:
            refactor_blackList += item

        for rfi in refactor_blackList:            
            if "fotos" not in rfi:
                rfi.setdefault("fotos", 1)
            if "description" not in rfi:
                rfi.setdefault("description", 1)
            if "facility" not in rfi:
                rfi.setdefault("facility", 1)
            if "otziv" not in rfi:
                rfi.setdefault("otziv", '?')
            if "room" not in rfi:
                rfi.setdefault("room", 1)
            if "room_block" not in rfi:
                rfi.setdefault("room_block", 1)

    except Exception as ex:
        # print(f"327____{ex}")
        pass
    try:
        return refactor_blackList
    except Exception as ex:
        # print(f"331____{ex}")
        return None

