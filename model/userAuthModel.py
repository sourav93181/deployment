from flask_sqlalchemy import SQLAlchemy
from common import db
from flask import jsonify
from common import Base


class AddUser(db.Model,Base):
    __tablename__ = "userauth"
    __table_args__ = (
        db.UniqueConstraint('username', 'contact',
                            name='unique_component_commit'),
    )
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    fullName = db.Column(db.String, nullable=False)
    username=db.Column(db.String,nullable=False)
    pass_word=db.Column(db.String,nullable=False)
    Address = db.Column(db.String, nullable=False)
    contact = db.Column(db.Integer,  nullable=False)
    # orderdetail = Base.relationship("getOrders")

    def __init__(self, fullName, username, pass_word, Address, contact) -> None:
        
        self.fullName = fullName
        self.username = username
        self.pass_word = pass_word
        self.Address = Address
        self.contact = contact

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def response(self):
        return {"user_id": self.user_id, "fullName": self.fullName, "username": self.username, "pass_word": self.pass_word, "Address": self.Address, "contact": self.contact}

    @classmethod
    def getUser(cls, username):
        result = cls.query.filter_by(username=username).first()
        return result.response()