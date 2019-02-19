from models.practice_datum import PracticeData
import helpers

helpers.connect_db()

user_table_headers = PracticeData().find(1)._attributes

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

while True:
    column = input('What is being searched?: ')
    if column.isspace() or column == '': break
    from_id = input('What record number?: ')
    if from_id.isspace() or from_id == '': break
    if column and from_id: return_a_detail(column, from_id)
