from sqlalchemy import create_engine, Column, Integer, String, text, func
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import select

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

def test_connection(engine):
    try:
        connection = engine.connect()
        connection.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def list_tables(engine):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
        tables = [row[0] for row in result]
        return tables



def run():
    DATABASE_URL = "postgresql://postgres:12345@localhost:5432/red"

    engine = create_engine(DATABASE_URL)

    Session = sessionmaker(bind=engine)
    session = Session()

    connection_successful = test_connection(engine)
    print(connection_successful)

    if connection_successful:
        tables = list_tables(engine)
        print("Tables:", tables)

