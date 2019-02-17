from models.practice_datum import PracticeData
from db import DATABASES
from orator import DatabaseManager, Model


db = DatabaseManager(DATABASES)
Model.set_connection_resolver(db)
user_table_headers = PracticeData().find(1)._attributes
# print(user_table_headers)

def return_a_detail(grabbed_detail, value):
    row = PracticeData.find(value)
    if grabbed_detail.lower() != 'all':
        try: 
            detail = getattr(row, grabbed_detail.lower())
            print(f'The answer is {detail}')
        except AttributeError: 
            print(f'There is no "{grabbed_detail}" attribute.')
    else: 
        buffer = ""
        for column, detail in user_table_headers.items():
            buffer += f'{column.upper()}: {detail} \n'
        print(buffer)

# def return_a_detail(grabbed_detail, value):
#     user = PracticeData.find(value)
#     lower_ver = grabbed_detail.lower()
#     valid_options = user_table_headers
#     # valid_options = columns
#     if lower_ver not in valid_options and lower_ver != 'all': 
#         print('Invalid column name')
#     elif lower_ver == 'all': 
#         buffer = ""
#         for k in valid_options.keys(): buffer += f'{k.title()}: {valid_options[k]}\n'
#         print(buffer)
#     elif lower_ver: print(valid_options[lower_ver])

while True:
    column = input('What is being searched?: ')
    if column == '': break
    from_id = input('What record number?: ')
    if from_id == '': break
    if column and from_id: return_a_detail(column, from_id)