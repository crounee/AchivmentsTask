from flask import request
from flask_restx import Namespace, Resource, fields,reqparse
from sqlalchemy import exc,text,desc
from ..Database import models,engine
statisticNamespace = Namespace("statisticNamespace","Пердоставляет статистические данные системы")




@statisticNamespace.route('/UserMaxAchievements')
class StatisticUserMaxAchievements(Resource):
    statisticUserMaxAchievementsModel = statisticNamespace.model("Пользователь с максимальным количеством достижений (штук)",{
    "user_id":fields.Integer,
    "achivments_count":fields.Integer
})

    @statisticNamespace.marshal_list_with(statisticUserMaxAchievementsModel)
    @statisticNamespace.response(500, 'Internal Server error')
    def get(self):
        '''Пользователь с максимальным количеством достижений (штук)'''
        try:
            value = engine.session.execute(text("select user_id,count(achivment_id) as max_achivment from achivment_recived group by user_id order by max_achivment desc limit 1"))
            value = value.fetchone()
            return {"user_id":value[0],"achivments_count":value[1]}
        except:
            return {"error"}

    

@statisticNamespace.route('/UserSumPoints')
class StatisticUserSumPoints(Resource):
    statisticUserSumPointsModel = statisticNamespace.model("Пользователь с максимальным количеством очков достижений (баллов суммарно)",{
    "user_id":fields.Integer,
    "total_points":fields.Integer
})

    @statisticNamespace.marshal_list_with(statisticUserSumPointsModel)
    @statisticNamespace.response(500, 'Internal Server error')
    def get(self):
        '''Пользователь с максимальным количеством очков достижений (баллов суммарно)'''
        try:
            value = engine.session.execute(text("select user_id, sum(achivments.number_of_points) as max_points from achivment_recived inner join achivments on achivment_recived.achivment_id = achivments.achivment_id group by user_id order by max_points desc limit 1"))
            value = value.fetchone()
            return {"user_id":value[0],"total_points":value[1]}
        except:
            return {"error"}

    
@statisticNamespace.route('/UsersMaximumDifference')
class StatisticUsersMaximumDifference(Resource):
    statisticUsersMaximumDifferenceModel = statisticNamespace.model("Пользователи с максимальной разностью очков достижений (разность баллов между пользователями)",{
    "user_id":fields.Integer,
    "points_difference":fields.Integer
})

    @statisticNamespace.marshal_list_with(statisticUsersMaximumDifferenceModel)
    @statisticNamespace.response(500, 'Internal Server error')
    def get(self):
        '''Пользователи с максимальной разностью очков достижений (разность баллов между пользователями)'''
        try:
            
            value = engine.session.execute(text("""select user_id, (select sum(achivments.number_of_points) as max_points from achivment_recived 
                                                inner join achivments on achivment_recived.achivment_id = achivments.achivment_id
                                                group by user_id order by max_points desc limit 1) - sum(achivments.number_of_points) as value_difference 
                                                from achivment_recived inner join achivments on achivment_recived.achivment_id = achivments.achivment_id
                                                group by user_id order by value_difference desc limit 10"""))
            value = value.fetchall()
            print(value)
            data = []
            for val in value:
                data.append({"user_id":val[0],
                             "points_difference":val[1]})

            return data
        except:
            return {"error"}
    

@statisticNamespace.route('/UsersMinDifference')
class StatisticUsersMinDifference(Resource):
    statisticUsersMinDifferenceModel = statisticNamespace.model("Пользователи с минимальной разностью очков достижений(разность баллов между пользователями)",{
    "user_id":fields.Integer,
    "points_difference":fields.Integer
})

    @statisticNamespace.marshal_list_with(statisticUsersMinDifferenceModel)
    @statisticNamespace.response(500, 'Internal Server error')
    def get(self):
        '''Пользователи с минимальной разностью очков достижений(разность баллов между пользователями)'''
        try:
            
            value = engine.session.execute(text("""select user_id, (select sum(achivments.number_of_points) as max_points from achivment_recived 
                                                inner join achivments on achivment_recived.achivment_id = achivments.achivment_id
                                                group by user_id order by max_points desc limit 1) - sum(achivments.number_of_points) as value_difference 
                                                from achivment_recived inner join achivments on achivment_recived.achivment_id = achivments.achivment_id
                                                group by user_id order by value_difference asc limit 10"""))
            value = value.fetchall()
            print(value)
            data = []
            for val in value:
                data.append({"user_id":val[0],
                             "points_difference":val[1]})

            return data
        except:
            return {"error"}
    


@statisticNamespace.route('/UserSevenDaysStreak')
class StatisticUsersSevenDaysStreak(Resource):
    statisticUsersSevenDaysStreakModel = statisticNamespace.model("Пользователи, которые получали достижения 7 дней подряд (по дате выдачи, хотя бы одно в каждый из 7 дней)",{
    "user_id":fields.Integer
})
    def get(self):
        '''Пользователи, которые получали достижения 7 дней подряд (по дате выдачи, хотя бы одно в каждый из 7 дней)'''
        try:
            
            value = engine.session.execute(text("""
    SELECT ua1.user_id FROM (select DISTINCT user_id from achivment_recived where DATE(date_of_recived) = CURRENT_DATE - 1) ua1
    INNER JOIN (select DISTINCT user_id from achivment_recived where DATE(date_of_recived) = CURRENT_DATE - 2) ua2 on ua1.user_id = ua2.user_id
    INNER JOIN (select DISTINCT user_id from achivment_recived where DATE(date_of_recived) = CURRENT_DATE - 3) ua3 on ua1.user_id = ua3.user_id
    INNER JOIN (select DISTINCT user_id from achivment_recived where DATE(date_of_recived) = CURRENT_DATE - 4) ua4 on ua1.user_id = ua4.user_id
    INNER JOIN (select DISTINCT user_id from achivment_recived where DATE(date_of_recived) = CURRENT_DATE - 5) ua5 on ua1.user_id = ua5.user_id
    INNER JOIN (select DISTINCT user_id from achivment_recived where DATE(date_of_recived) = CURRENT_DATE - 6) ua6 on ua1.user_id = ua6.user_id
    INNER JOIN (select DISTINCT user_id from achivment_recived where DATE(date_of_recived) = CURRENT_DATE - 7) ua7 on ua1.user_id = ua7.user_id"""))
            value = value.fetchall()
            print(value)
            data = []
            for val in value:
                data.append({"user_id":val[0]})

            return data
        except:
            return {"error"}

    
