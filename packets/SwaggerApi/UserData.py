from flask import request
from flask_restx import Namespace, Resource, fields,reqparse
from ..Database import models,engine

userDataNamespace = Namespace("UserInformation","Предоставляет информацию о пользователе")

userDataModel = userDataNamespace.model("Получить данные о пользователе",{
    'user_id':fields.Integer,
    'name_user': fields.String,
    'language_name': fields.String
})

userDataArgyments = reqparse.RequestParser()
userDataArgyments.add_argument('name_user', type=str, help='Имя пользователя')

@userDataNamespace.route('/userData')
class UserData(Resource):
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
        
    

userDataModel = userDataNamespace.model("Предоставляет информацию о выданных пользователю достижениях на выбранном пользователем языке",{
    'user_id':fields.Integer,
    'name_user': fields.String,
    'language_name': fields.String
})


AchievementsReceivedArgyments = reqparse.RequestParser()
AchievementsReceivedArgyments.add_argument('username', type=str, help='Имя пользователя')


@userDataNamespace.route('/AchievementsReceived')
class AchievementsReceived(Resource):
    @userDataNamespace.marshal_list_with(userDataModel)
    @userDataNamespace.response(500, 'Internal Server error')
    @userDataNamespace.expect(userDataArgyments)
    def get(self):
        '''Предоставляет информацию о выданных пользователю достижениях на выбранном пользователем языке'''
        try:
            print(request.args)
            for i in request.args:
                print(request.args.get(i))
        except:
            pass

        return {"name":{request.args.get('username')}}