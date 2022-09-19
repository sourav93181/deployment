from flask_sqlalchemy import SQLAlchemy
from common import db
from flask import jsonify
from model.userAuthModel import AddUser
from common import Base
class getOrders(db.Model,Base):
    __tablename__ = "sql_orders"
    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    item_name = db.Column(db.String, nullable=False)
    item_price = db.Column(db.String, nullable=False)
    item_desc = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(AddUser.user_id), nullable = False)

    @classmethod
    def response(cls):
        return { "item_name": cls.item_name ,"item_desc": cls.item_desc}

    def add_order(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def getOrderDb(cls,user_id):
        result = cls.query.filter_by(user_id=user_id).all()
        return result
        

    @classmethod
    def getOrderById(cls, user_id):
        result = cls.query.filter_by(user_id=user_id).first()
        return result
