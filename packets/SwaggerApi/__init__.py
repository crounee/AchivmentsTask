from flask import Blueprint
from flask_restx import Api
from .UserData import userDataNamespace
from .Achievements import achievementsNamespace
from .StatisticsData import statisticNamespace

blueprint = Blueprint('swagger', __name__, url_prefix='/swagger')

api_extension = Api(
    blueprint,
    title='API для работы с достижениями',
    version='1.0'
)

api_extension.add_namespace(userDataNamespace)
api_extension.add_namespace(achievementsNamespace)
api_extension.add_namespace(statisticNamespace)