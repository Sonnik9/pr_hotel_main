def b_w_writerr(black_list):
    from . import b_filter_func
    from datetime import datetime
    import json
    print("hello black writer")
    # white_list_refactor = []
    try:
        new_resBlackList = eval(b_filter_func.black_filter(black_list))
    except Exception as ex:
        # print(f"339____{ex}")
        new_resBlackList = black_list

    now = datetime.now() 
    curentTimeForFile = now.strftime("%d_%m_%Y__%H_%M")

    try:
        if new_resBlackList != None and new_resBlackList != []:
            print(f"len_resBlackList___{len(new_resBlackList)}")
            try:
                with open(f'./result_hotels_upz/black_list__{curentTimeForFile}__{len(new_resBlackList)}.json', "w", encoding="utf-8") as file: 
                    json.dump(new_resBlackList, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str348__{ex}")
    except:
        pass
