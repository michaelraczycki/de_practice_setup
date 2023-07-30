import pandas as pd
from .db.db_connector import DatabaseConnector

db = DatabaseConnector('root', 'root', 'localhost', '5432', 'postgres')
