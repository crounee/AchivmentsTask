from flask import request
from flask_restx import Namespace, Resource, fields,reqparse
from ..Database import models,engine

userDataNamespace = Namespace("UserInformation","Предоставляет информацию о пользователе")


@userDataNamespace.route('/userData')
class UserData(Resource):
    userDataModel = userDataNamespace.model("Получить данные о пользователе",{
    'user_id':fields.Integer,
    'name_user': fields.String,
    'language_name': fields.String
})

    userDataArgyments = reqparse.RequestParser()
    userDataArgyments.add_argument('name_user', type=str, help='Имя пользователя')

    @userDataNamespace.marshal_list_with(userDataModel)
    @userDataNamespace.response(500, 'Internal Server error')
    @userDataNamespace.expect(userDataArgyments)
    def get(self):
        '''Возвращает информацию о пользователе'''
        user = engine.session.query(models.User).filter(models.User.name_user == request.args.get('username'))
        if user.count() > 0:
            return {"user_id":user[0].user_id,
                    "name_user":user[0].name_user,
                    "language_name":user[0].language_name
                    }
        else:
            return {}
        
    




@userDataNamespace.route('/AchievementsReceived')
class AchievementsReceived(Resource):

    userDataModel = userDataNamespace.model("Предоставляет информацию о выданных пользователю достижениях на выбранном пользователем языке",{
    'achivment_recived_id':fields.Integer,
    'user_id':fields.Integer,
    'achivment_id': fields.Integer,
    'date_of_recived': fields.DateTime,
    'description':fields.String
})
    AchievementsReceivedArgyments = reqparse.RequestParser()
    AchievementsReceivedArgyments.add_argument('user_id', type=str, help='id пользователя')

    @userDataNamespace.marshal_list_with(userDataModel)
    @userDataNamespace.response(500, 'Internal Server error')
    @userDataNamespace.expect(AchievementsReceivedArgyments)
    def get(self):
        '''Предоставляет информацию о выданных пользователю достижениях на выбранном пользователем языке'''
        user_id = request.args.get("user_id")
        try:
            language_name = engine.session.query(models.User).filter(models.User.user_id == user_id)
            language_name = language_name[0].language_name

            achivments_recived = engine.session.query(models.Achivment_recived).filter(models.Achivment_recived.user_id == user_id)
            data = []
            for achivment in achivments_recived:
                description = engine.session.query(models.Description).filter(models.Description.achivment_id == achivment.achivment_id,
                                                                              models.Description.language_name == language_name)

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
            return data
        except:
            return {"error"}
