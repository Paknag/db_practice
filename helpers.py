from db import DATABASES
from orator import DatabaseManager, Model

def connect_db():
    db = DatabaseManager(DATABASES)
    Model.set_connection_resolver(db)