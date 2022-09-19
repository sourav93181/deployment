
from ast import Or
from flask_restful import Api
from resources.userAuthrRes import user,getAll,Orders,FeedBack
from flask import request
from common import db


def addRoutes(app):
    api = Api(app)
    api.add_resource(user, '/newuser')
    api.add_resource(getAll, '/allitems')
    api.add_resource(Orders, '/orders',"/orders/<int:user_id>")
    api.add_resource(FeedBack,'/feedback')
    return app

