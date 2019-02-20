from orator import Schema, DatabaseManager
from db import DATABASES

db = DatabaseManager(DATABASES)
schema = Schema(db)



# with schema.table('practice_data') as table:
    # table.rename_column('namef', 'first')
    # table.rename_column('namel', 'last')