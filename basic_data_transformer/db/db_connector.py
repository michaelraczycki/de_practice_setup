from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConnector:
    def __init__(self, username, password, host, port, database):
        self.engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def select_data(self, table_name, condition=None):
            session = self.get_session()
            query = f"SELECT * FROM {table_name}"
            if condition:
                query += f" WHERE {condition}"
            result = session.execute(query)
            data = result.fetchall()
            session.close()
            return data
    
    def insert_data(self, table_name, data):
        session = self.get_session()
        query = f"INSERT INTO {table_name} VALUES {data}"
        session.execute(query)
        session.commit()
        session.close()

    def update_data(self, table_name, data, condition):
        session = self.get_session()
        query = f"UPDATE {table_name} SET {data} WHERE {condition}"
        session.execute(query)
        session.commit()
        session.close()
