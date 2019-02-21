from models.practice_datum import PracticeData
import helpers

helpers.connect_db()

# When creating a record, all non-nullable fields need to be filled
# pd = PracticeData()
# pd.namef = 'will'
# pd.namel = 'dove'
# pd.note = 'Things and stuff'
# pd.save()


user_table_headers = PracticeData().find(1)._attributes

def return_a_detail(grabbed_detail, value):
    row = PracticeData.find(value)
    if grabbed_detail.lower() != 'all':
        try: 
            detail = getattr(row, grabbed_detail.lower())
            print(f'The answer is {detail.title()}')
        except AttributeError: 
            print(f'There is no "{grabbed_detail}" attribute.')
    else: 
        buffer = ""
        for column, detail in user_table_headers.items():
            buffer += f'{column.upper()}: {detail} \n'
        print(buffer)

while True:
    column = input('What is being searched?: ')
    if column == '' or column.isspace() == '': break
    from_id = input('What record number?: ')
    if from_id == '' or from_id.isspace() == '': break
    if column and from_id: return_a_detail(column, from_id)
