from sqlalchemy import create_engine,text
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


if __name__ == "__main__":
    """TEST REQUESTS"""
    from models import *
    

    """выдавать достижения пользователю с сохранением времени выдачи (сохранять связь пользователя с достижением и датой выдачи);"""
    id_user = 1
    number_achivment = 228
    giveAchivmentRequest = Achivment_recived(user_id = id_user,achivment_id=number_achivment)
    session.add(giveAchivmentRequest)
    session.commit()
    '''Предоставляет информацию о выданных пользователю достижениях на выбранном пользователем языке'''