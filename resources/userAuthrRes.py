from tkinter.messagebox import RETRY
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required, JWTManager
from ast import Add
from unittest import result
from urllib.request import Request
from flask import request
from flask_restful import Resource
from model.userAuthModel import AddUser
from model.allitemModel import getItems
from model.orderByUser import getOrders
from model.feedback import UserFeedback
from common import db,token
from flask import jsonify
import json
class user(Resource):
    def post(self):
        print("request reach")
        requestBody = request.json
        verifyuser = AddUser.getUser(username=requestBody.get('username', None))
        print(verifyuser)
        if(verifyuser.get('pass_word') == requestBody.get('pass_word')):
            print("found")
            return {'data': create_access_token(identity={'user_id':verifyuser.get('user_id') , 'username': verifyuser.get('username'), "password": verifyuser.get('pass_word'), "Address": verifyuser.get('Address'), "contact": verifyuser.get('contact')})}
        return {'message':'not a user'}
    def put(self):
       print("request reach")
       requestBody = request.json
       newUser = AddUser(fullName=requestBody.get('fullName', None),  username=requestBody.get(
           'username', None), pass_word=requestBody.get('pass_word', None),  Address=requestBody.get('Address', None), contact=requestBody.get('contact',None))
       newUser.add_user()
       return {"message": "Added new User"}, 200

class getAll(Resource):
    
    def get(self):
        result=getItems.getItemDb()
        return jsonify({'data':[{"item_id":i.item_id,"item_name":i.item_name,"item_img":str(i.item_img)} for i in result]})
        
class Orders(Resource):
    def post(self):
        requestBody = request.json
        allOrders = getOrders.getOrderDb(
            user_id=requestBody.get('user_id', None))
        print(allOrders)
        res = [{'item_name': i.item_name, "item_desc": i.item_desc} for i in allOrders]
        return res
        # return jsonify({'data': create_access_token(identity=res)})
        
    def put(self):
       requestBody = request.json
       newOrder = getOrders(item_name=requestBody.get('item_name', None),  item_price=requestBody.get(
           'item_price', None), item_desc=requestBody.get('item_desc', None),  user_id=requestBody.get('user_id', None))
       newOrder.add_order()
       return {"message": "Added new order"}, 200
    
    def delete(self,user_id):
        # requestBody = request.json
        delOrders = getOrders.getOrderById(user_id)
        print(delOrders)
        db.session.delete(delOrders)
        db.session.commit()
        return {"message":"Order Cancel"}, 200

class FeedBack(Resource):

    def put(self):
        requestBody = request.json
        newFeedback = UserFeedback(
            item_name=requestBody.get('item_name', None), item_quality=requestBody.get('item_quality', None), item_taste=requestBody.get('item_taste', None), item_rating=requestBody.get('item_rating', None), item_suggestion=requestBody.get('item_suggestion', None), user_id=requestBody.get('user_id', None))
        newFeedback.add_feedback()
        return {"message":"Feedback Added"}