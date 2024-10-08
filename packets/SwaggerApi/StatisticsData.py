from flask import request
from flask_restx import Namespace, Resource, fields,reqparse

statisticNamespace = Namespace("statisticNamespace","Пердоставляет статистические данные системы")

@statisticNamespace.route('/UserMaxAchievements')
class StatisticUserMaxAchievements(Resource):
    def get(self):
        '''Пользователь с максимальным количеством достижений (штук)'''
        try:
            print(request.args)
            for i in request.args:
                print(request.args.get(i))
        except:
            pass

        return {"name":{request.args.get('username')}}
    

@statisticNamespace.route('/UserMaxPoints')
class StatisticUserMaxPoints(Resource):
    def get(self):
        '''Пользователь с максимальным количеством очков достижений (баллов суммарно)'''
        try:
            print(request.args)
            for i in request.args:
                print(request.args.get(i))
        except:
            pass

        return {"name":{request.args.get('username')}}
    
@statisticNamespace.route('/UsersMaximumDifference')
class StatisticUsersMaximumDifference(Resource):
    def get(self):
        '''Пользователи с максимальной разностью очков достижений (разность баллов между пользователями)'''
        try:
            print(request.args)
            for i in request.args:
                print(request.args.get(i))
        except:
            pass

        return {"name":{request.args.get('username')}}
    

@statisticNamespace.route('/UsersMinDifference')
class StatisticUsersMinDifference(Resource):
    def get(self):
        '''Пользователи с минимальной разностью очков достижений(разность баллов между пользователями)'''
        try:
            print(request.args)
            for i in request.args:
                print(request.args.get(i))
        except:
            pass

        return {"name":{request.args.get('username')}}
    


@statisticNamespace.route('/UserSevenDaysStreak')
class StatisticUsersSevenDaysStreak(Resource):
    def get(self):
        '''Пользователи, которые получали достижения 7 дней подряд (по дате выдачи, хотя бы одно в каждый из 7 дней)'''
        try:
            print(request.args)
            for i in request.args:
                print(request.args.get(i))
        except:
            pass

        return {"name":{request.args.get('username')}}

    
