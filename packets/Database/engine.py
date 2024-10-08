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
    #session.add(addAchivment)
    #session.commit()
    
    """Описание достижения"""
    language_name = "rus"
    achivment_id = addAchivment.achivment_id
    description = "Достижение за покупку воды бим бам бим бим"

    addDescription = Description(language_name = language_name,achivment_id = achivment_id,description = description)
    #session.add(addDescription)
    #session.commit()


    '''Возвращает информацию о всех доступных достижениях'''
    achivments = session.query(Achivments).all()
    description = []
    for achiv in achivments:
        value = {"achivment_id":achiv.achivment_id,
                 "achivment_name":achiv.achivment_name,
                 "number_of_points":achiv.number_of_points}
        description.append(value)


    '''Предоставляет информацию о выданных пользователю достижениях на выбранном пользователем языке'''

    user_id = 1
    language_name = session.query(User).filter(User.user_id == user_id)
    language_name = language_name[0].language_name

    achivments_recived = session.query(Achivment_recived).filter(Achivment_recived.user_id == user_id)
    data = []
    for achivment in achivments_recived:
        description = session.query(Description).filter(Description.achivment_id == achivment.achivment_id,Description.language_name == language_name)
        
        if description.count() > 0:
            description = description[0].description
        else:
            description = "not found description"

        value = {"achivment_recived_id":achivment.achivment_recived_id,
                "user_id":achivment.user_id,
                "achivment_id": achivment.achivment_id,
                "date_of_recived":achivment.date_of_recived,
                "description":description
                }
        data.append(value)
        
    """Пользователь с максимальным количеством достижений (штук)"""
    value = session.execute(text("select user_id,count(achivment_id) as max_achivment from achivment_recived group by user_id order by max_achivment desc limit 1"))
    value = value.fetchone()


    """Пользователь с максимальным количеством достижений (штук)"""
    value = session.execute(text("select user_id, max(achivments.number_of_points) as max_points from achivment_recived inner join achivments on achivment_recived.achivment_id = achivments.achivment_id group by user_id order by max_points desc limit 1"))
    value = value.fetchone()
    #print(value)


    """s"""
    value = session.execute(text("""select user_id, (select sum(achivments.number_of_points) as max_points from achivment_recived 
                                                inner join achivments on achivment_recived.achivment_id = achivments.achivment_id
                                                group by user_id order by max_points desc limit 1) - sum(achivments.number_of_points) as value_difference 
                                                from achivment_recived inner join achivments on achivment_recived.achivment_id = achivments.achivment_id
                                                group by user_id order by value_difference desc limit 10"""))
    value = value.fetchall()
    print(value)