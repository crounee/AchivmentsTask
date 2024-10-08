from flask import request
from flask_restx import Namespace, Resource, fields,reqparse
from sqlalchemy import exc
from ..Database import models,engine

achievementsNamespace = Namespace("AchievementsInformation","Предоставляет информацию о достижениях/Добавление достижений")




@achievementsNamespace.route('/allAchievements')
class AllAchievements(Resource):

    achievementsModel = achievementsNamespace.model("Предоставляет информацию о достижениях",{
    "achivment_id":fields.Integer,
    "achivment_name":fields.String,
    "number_of_points":fields.Integer
})


    @achievementsNamespace.marshal_list_with(achievementsModel)
    @achievementsNamespace.response(500, 'Internal Server error')
    def get(self):
        '''Возвращает информацию о всех доступных достижениях'''
        
        
        try:
            achivments = engine.session.query(models.Achivments).all()
            description = []

            for achiv in achivments:
                value = {"achivment_id":achiv.achivment_id,
                    "achivment_name":achiv.achivment_name,
                    "number_of_points":achiv.number_of_points}
                description.append(value)

            return description
        except exc.IntegrityError:
            engine.session.rollback()
            return {"status":False}
        
    


    addAchievementsModel = achievementsNamespace.model("Создает достижение",{
    'status':fields.Boolean
})
    addUserAchievementsArguments = reqparse.RequestParser()
    addUserAchievementsArguments.add_argument("achivment_name",type=str,help="Название достижения")
    addUserAchievementsArguments.add_argument("number_of_points",type=int,help="Количество очков за получение достижения")

    @achievementsNamespace.marshal_list_with(addAchievementsModel)
    @achievementsNamespace.response(500, 'Internal Server error')
    @achievementsNamespace.expect(addUserAchievementsArguments)
    def put(self):
        '''Добавить достижение'''
        achivment_name = request.args.get('achivment_name')
        number_of_points = request.args.get('number_of_points')

        if achivment_name != None or number_of_points != None:
            try:
                addAchivment = models.Achivments(achivment_name = achivment_name,number_of_points = number_of_points)
                engine.session.add(addAchivment)
                engine.session.commit()
                return {'status':True}
            except exc.IntegrityError:
                engine.session.rollback()
                return {"status":False}
        else:
            return {'status':False}




@achievementsNamespace.route('/addUserAchievements')
class AddUserAchievements(Resource):

    addUserAchievementsModel = achievementsNamespace.model("Выдает достижения пользователю с сохранением времени выдачи",{
    'status':fields.Boolean
})

    addUserAchievementsArguments = reqparse.RequestParser()
    addUserAchievementsArguments.add_argument("user_id",type=int,help="id пользователя")
    addUserAchievementsArguments.add_argument("achivment_id",type=int,help="id достижения")

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
    
    
    
@achievementsNamespace.route('/addAchivmentsDescription')
class AddDescriptionAchievements(Resource):

    addDescriptionAchievementsModel = achievementsNamespace.model("Добавляет описание достижения",{
    'status':fields.Boolean
})

    addDescriptionAchievementsArguments = reqparse.RequestParser()
    addDescriptionAchievementsArguments.add_argument("achivment_id",type=int,help="id достижения")
    addDescriptionAchievementsArguments.add_argument("language_name",type=str,help="Язык описания достижения")
    addDescriptionAchievementsArguments.add_argument("description",type=str,help="Описание достижения")

    @achievementsNamespace.marshal_list_with(addDescriptionAchievementsModel)
    @achievementsNamespace.response(500, 'Internal Server error')
    @achievementsNamespace.expect(addDescriptionAchievementsArguments)
    def put(self):
        '''Добавляет описание достижения'''

        achivment_id = request.args.get('achivment_id')
        description = request.args.get('description')
        language_name = request.args.get('language_name')

        if achivment_id != None and description != None and language_name != None:
            try:
                addDescription = models.Description(language_name = language_name,achivment_id = achivment_id,description = description)
                engine.session.add(addDescription)
                engine.session.commit()
                return {'status':True}
            except exc.IntegrityError:
                engine.session.rollback()
                return {"status":False}
        else:
            return {'status':False}
    