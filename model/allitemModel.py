from flask_sqlalchemy import SQLAlchemy
from common import db
from flask import jsonify


class getItems(db.Model):
    __tablename__ = "sql_items"
    item_id = db.Column(db.Integer, primary_key=True, nullable=False)
    item_name = db.Column(db.String, nullable=False)
    item_price = db.Column(db.String, nullable=False)
    item_desc = db.Column(db.String, nullable=False)
    item_img = db.Column(db.BLOB, nullable=False)


    def response(cls):
        return {"item_id": cls.item_id, "item_name": cls.item_name, "item_price": cls.item_price, "item_desc": cls.item_desc, "item_img": cls.item_img}

    @classmethod
    def getItemDb(cls):
        result = cls.query.all()
        # return [i.response() for i in result]
        return result
        # return {"data":[i.response() for i in result]}
