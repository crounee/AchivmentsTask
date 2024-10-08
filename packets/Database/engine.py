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
    #session.add(giveAchivmentRequest)
    #session.commit()

    """Добавление достижения"""
    achivment_name = "Покупка воды"
    number_of_points = 100

    addAchivment = Achivments(achivment_name = achivment_name,number_of_points = number_of_points)
    session.add(addAchivment)
    session.commit()
    
    """Описание достижения"""
    language_name = "rus"
    achivment_id = addAchivment.achivment_id
    description = "Достижение за покупку воды бим бам бим бим"

    addDescription = Description(language_name = language_name,achivment_id = achivment_id,description = description)
    session.add(addDescription)
    session.commit()


