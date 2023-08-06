from sqlalchemy import create_engine, Column, Integer, String, text, func
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import select

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class Database:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def test_connection(self):
        try:
            connection = self.engine.connect()
            connection.close()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
