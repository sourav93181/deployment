from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required, JWTManager
from sqlalchemy.orm import declarative_base, relationship
token=create_access_token
db = SQLAlchemy()
Base = declarative_base()
