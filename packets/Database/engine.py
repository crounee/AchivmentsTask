from sqlalchemy import create_engine,text,desc
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password=9822,
    port=5432,
    host="localhost",
    database="user_achivement"
)

engine = create_engine(url)
conntection = engine.connect()
session = sessionmaker(bind=engine)()

