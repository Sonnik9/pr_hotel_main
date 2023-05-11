from prettytable import PrettyTable
import json
import test_data_db


# from prettytable import PrettyTable

# def preaty_data_visualize(data):
#     table = PrettyTable()
#     table.field_names = ["ListPhoto", "ФотоАйди", "Срц", "Тайтл"]
#     table.align = "l"

#     for row in data:
#         table.add_row(["", row[0], row[1], row[2]])

#     print(table)

# result = [(1, "src1", "title1"), (2, "src2", "title2"), (3, "src3", "title3")]
# preaty_data_visualize(result)


from prettytable import PrettyTable
def preaty_data_visualize():
    table = PrettyTable()
    table.field_names = ["id", "hoid", "max", "square60", "list_photo", "src", "idF", "pTtl"]
    for item in test_data_db.data:
        hoid = item['hoid']
        max = item['max']
        square60 = item['square60']
        list_photos = item['list_photo']
        all_photos = item['all_photos']
    # Add a row for the main item data
        table.add_row([item['id'], item['hoid'], item['max'], item['square60']])
    # table.field_names = ["Л", "1", "2", "3"]
    # table.add_column("id", '')
    # table.add_column("hoid", [d[0] for d in data])
    # table.add_column("max", [d[1] for d in data])
    # table.add_column("Тайтл", [d[2] for d in data])
    # table.add_row(["1", "src1", "title1"])
    # table.add_row(["2", "src2", "title2"])
    # table.add_row(["3", "src3", "title3"])

    print(table)

# result = [(1, "src1", "title1"), (2, "src2", "title2"), (3, "src3", "title3")]
preaty_data_visualize()


data = [
    {
    "id": "",
    "hoid": "56",
    "max": "ht..",
    "square60": "htt",
    "list_photo": [

        {
            "src": "h",
            "idF": "2491",
            "pTtl": "a  ..."
        },
        {
            "src": "htt",
            "idF": "24",
            "pTtl": "a g ..."
        },
        
    ],
    "all_photos": [
        {
            "id_ph": "24",
            "p1": "htt",
            "p2": "htt",
            "p3": "ht"
        },
        {
            "id_ph": "249",
            "p1": "htt",
            "p2": "htt",
            "p3": "ht"
        },

    ]
},
{
    "id": "",
    "hoid": "56",
    "max": "ht..",
    "square60": "htt",
    "list_photo": [

        {
            "src": "h",
            "idF": "2491",
            "pTtl": "a  ..."
        },
        {
            "src": "htt",
            "idF": "24",
            "pTtl": "a g ..."
        },

        
    ],
    "all_photos": [
        {
            "id_ph": "24",
            "p1": "htt",
            "p2": "htt",
            "p3": "ht"
        },
        {
            "id_ph": "249",
            "p1": "htt",
            "p2": "htt",
            "p3": "ht"
        },
        {
            "id_ph": "49",
            "p1": "htt",
            "p2": "htt",
            "p3": "ht"
        },

    ]
},
] 



