







# # # python db_handler.py

# from prettytable import PrettyTable
# import mysql.connector

# # Connect to the database
# conn = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="yourdatabase"
# )

# # Create a cursor object
# cursor = conn.cursor()

# # Execute a SELECT statement to retrieve the data from the table
# select_query = "SELECT * FROM result_photos"
# cursor.execute(select_query)
# result = cursor.fetchall()

# # Create a PrettyTable object
# table = PrettyTable()
# table.field_names = ['hotelid', 'url_max', 'url_square60', 'preview_list_photo', 'photo_item_src', 'photo_item_id', 'photo_item_title', 'all_photos', 'id_photo', 'photo_max1280x900', 'photo_max1024x768', 'photo_max200']

# # Add the data to the table
# for row in result[0:40]:
#     table.add_row(row)

# # Print the table
# print(table)
    # cursor.execute("SET GLOBAL max_allowed_packet = 1073741824")
    # insert_query = "INSERT INTO result_photos (hotelid, url_max, url_square60, photo_item_src, photo_item_id, photo_item_title, id_photo, photo_max1280x900, photo_max1024x768, photo_max200) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # insert_query = "INSERT INTO result_photos (hoid, max, square60, src, idF, pTtl, id_ph, p1, p2, p3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # for item in data:
    #     for preview in item['list_photo']:
    #         values = (item['hoid'], item['max'], item['square60'], preview['src'], preview.get('idF', '----'), preview['pTtl'], '----', '----', '----', '----')
    #         cursor.execute(insert_query, values)

    #     for photo in item['all_photos']:
    #         values = (item['hoid'], item['max'], item['square60'], '----', '----', '----', photo['id_ph'], photo['p1'], photo['p2'], photo['p2'])
    #         cursor.execute(insert_query, values)
   


# Выполнение запроса на выборку данных
    # select_query = "SELECT * FROM result_photos"
    # cursor.execute(select_query)
    # result = cursor.fetchall()

    # # Create a PrettyTable object
    # table = PrettyTable()
    # # table.field_names = ['id', 'hotelid', 'url_max', 'url_square60', 'preview_list_photo', 'photo_item_src', 'photo_item_id', 'photo_item_title', 'all_photos', 'id_photo', 'photo_max1280x900', 'photo_max1024x768', 'photo_max200']
    # table.field_names = ['id', 'hoid', 'max', 'square60', 'list_photo', 'src', 'idF', 'pTtl', 'all_photos', 'id_ph', 'p1', 'p2', 'p3']

    # # Add the data to the table
    # for row in result:
    #     table.add_row(row)


    # select_query = "SELECT * FROM result_photos"
    # cursor.execute(select_query)

    # # Получение результатов запроса
    # results = cursor.fetchall()

    # # Вывод данных
    # for row in results[0:2]:
    #     print(row)

    # Закрытие соединения с базой данных

    # # Print the table
    # print(table)


    # select_query = "SELECT * FROM result_photos"
    # cursor.execute(select_query)

    # # Получение результатов запроса
    # results = cursor.fetchall()

    # # Вывод данных
    # for row in results[0:2]:
    #     print(row)

    # Закрытие соединения с базой данных





    # select_query = "SELECT * FROM result_photos"
    # cursor.execute(select_query)

    # # Получение результатов запроса
    # results = cursor.fetchall()

    # # Вывод данных
    # for row in results[0:2]:
    #     print(row)

    # Закрытие соединения с базой данных





# def preaty_data_visualize(result):
# # Create the table with the headers

#     table = PrettyTable(["id", "hoid", "max", "square60", "list_photo", "src", "idF", "pTtl", "all_photos", "id_ph", "p1", "p2", "p3"])

#     # Add rows to the table
#     for item in result:
#         # Add a row for the main item data
#         table.add_row([item['id'], item['hoid'], item['max'], item['square60'], "", "", "", "", "", "", "", "", ""])
        
#         # Add rows for the list_photo data
#         for preview in item['list_photo']:
#             table.add_row(["", "", "", "", "X", preview['src'], preview.get('idF', '----'), preview['pTtl'], "", "----", "----", "----", ""])
        
#         # Add rows for the all_photos data
#         for photo in item['all_photos']:
#             table.add_row(["", "", "", "", "", "", "", "", "X", photo['id_ph'], photo['p1'], photo['p2'], photo['p3']])

#     # Print the table
#     print(table)

#  try:    
#         for item in test_data_db.data:
#             hoid = item['hoid']
#             max = item['max']
#             square60 = item['square60']
#             list_photos = item['list_photo']
#             all_photos = item['all_photos']
#             # print(all_photos)

#             for photo in list_photos:
#                 src = photo['src']
#                 idF = photo['idF']
#                 pTtl = photo['pTtl']
#                 cursor.execute('INSERT INTO result_photos (hoid, max, square60, src, idF, pTtl) VALUES (%s, %s, %s, %s, %s, %s)', (hoid, max, square60, src, idF, pTtl))

#             for photo in all_photos:
#                 id_ph = photo['id_ph']
#                 p1 = photo['p1']
#                 p2 = photo['p2']
#                 p3 = photo['p3']
#                 cursor.execute('INSERT INTO result_photos (hoid, max, square60, id_ph, p1, p2, p3) VALUES (%s, %s, %s, %s, %s, %s, %s)', (hoid, max, square60, id_ph, p1, p2, p3))


    # conn = mysql.connector.connect(
    #     host='localhost',
    #     user='sonnik11',
    #     password='9283sono',
    #     database='upz_hotels_test2',       
    # )
    # print('connection ok')
    # # cursor = conn.cursor(buffered=True)
    # cursor = conn.cursor()
