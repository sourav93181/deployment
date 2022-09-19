from flask import Flask
from routes.index import addRoutes
from common import db
from flask_jwt_extended import  JWTManager
from flask_cors import CORS
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = 'sourav'
app = addRoutes(app)
jwt = JWTManager(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost/sql_hotspot"


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True, port=5000)
