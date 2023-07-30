from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConnector:
    def __init__(self, username, password, host, port, database):
        self.engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

