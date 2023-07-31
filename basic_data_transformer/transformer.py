import pandas as pd
from db.db_connector import DatabaseConnector
import glob

db = DatabaseConnector('root', 'root', 'localhost', '5432', 'postgres')
session = db.get_session()
session.close()

help(glob.glob)