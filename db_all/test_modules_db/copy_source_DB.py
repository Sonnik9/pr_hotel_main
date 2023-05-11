import mysql.connector
from mysql.connector import connect, Error
from prettytable import PrettyTable
import json

import test_data_db, preaty_tabless, deliter_tableses, create_tables_db, source_DB_hotel

def db_rewriterr(source):
    conn = mysql.connector.connect(
        host='localhost',
        user='sonnik11',
        password='9283sono',
        database='upz_hotels_test2',       
    )
    print('connection ok')
    # cursor = conn.cursor(buffered=True)
    cursor = conn.cursor()

    # return
    # hotel_id, url, fotos, description, room, facility, otziv
    try:
   


        conn.commit()
            
    except Exception as ex:
        print(f"29____{ex}")

    select_query = "SELECT * FROM result_photos"
    cursor.execute(select_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print(result)

    return result




def main():
    # deliter_tableses.delete_tables()
    create_tables_db.create_tables()
    source_data = source_DB_hotel.db_opener()
    db_rewriterr(source_data)
    # result = test_data_db.data
    # return
    # preaty_tabless.preaty_data_visualize(result)

if __name__ == "__main__":
    main()
