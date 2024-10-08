from flask import request
from flask_restx import Namespace, Resource, fields,reqparse
from sqlalchemy import exc
from ..Database import models,engine

achievementsNamespace = Namespace("AchievementsInformation","Предоставляет информацию о достижениях/Добавление достижений")

achievementsModel = achievementsNamespace.model("Предоставляет информацию о достижениях/Добавление достижений",{
    'username': fields.String(
        readonly=True,
        description='<h1>Информация о пользователе</h1>'
    )
})



@achievementsNamespace.route('/allAchievements')
class AllAchievements(Resource):
    @achievementsNamespace.marshal_list_with(achievementsModel)
    @achievementsNamespace.response(500, 'Internal Server error')
    def get(self):
        '''Возвращает информацию о всех доступных достижениях'''
        
        try:
            print(request.args)
            for i in request.args:
                print(request.args.get(i))
        except:
            pass

        return {"name":{request.args.get('username')}}
    
    def put(self):
        '''Добавить достижение'''
        try:
            print(request.args)
            for i in request.args:
                print(request.args.get(i))
        except:
            pass

        return {"name":{request.args.get('username')}}


addUserAchievementsModel = achievementsNamespace.model("Выдает достижения пользователю с сохранением времени выдачи",{
    'status':fields.Boolean
})


addUserAchievementsArguments = reqparse.RequestParser()
addUserAchievementsArguments.add_argument("user_id",type=int,help="id пользователя")
addUserAchievementsArguments.add_argument("achivment_id",type=int,help="id достижения")

@achievementsNamespace.route('/addUserAchievements')
class AddUserAchievements(Resource):
    @achievementsNamespace.marshal_list_with(addUserAchievementsModel)
    @achievementsNamespace.response(500, 'Internal Server error')
    @achievementsNamespace.expect(addUserAchievementsArguments)
    def put(self):
        '''Выдает достижения пользователю с сохранением времени выдачи'''

        user_id = request.args.get('user_id')
        achivment_id = request.args.get('achivment_id')

        if user_id != None or achivment_id != None:
            try:
                addAchivmentRequest = models.Achivment_recived(user_id = user_id,achivment_id=achivment_id)
                engine.session.add(addAchivmentRequest)
                engine.session.commit()
                return {'status':True}
            except exc.IntegrityError:
                engine.session.rollback()
                return {"status":False}
        else:
            return {'status':False}
    
    
    