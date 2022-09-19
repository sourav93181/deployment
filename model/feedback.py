from flask_sqlalchemy import SQLAlchemy
from common import db
from flask import jsonify
from model.userAuthModel import AddUser
class UserFeedback(db.Model):
    __tablename__ = "sql_feedback"
    feedback_id = db.Column(db.Integer, primary_key=True, nullable=False)
    item_name = db.Column(db.String, nullable=False)
    item_quality = db.Column(db.String, nullable=False)
    item_taste = db.Column(db.String, nullable=False)
    item_rating = db.Column(db.Integer, nullable=False)
    item_suggestion = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(
        AddUser.user_id), nullable=False)

    def add_feedback(self):
        db.session.add(self)
        db.session.commit()
