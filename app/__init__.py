from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

from app import (	
					login,
					jadwal,
					absen, 
					models
				)

from app import login

if __name__ == "__main__":
    app.run(host='bsmkomputer.herokuapp.com', port=1337, workers=4)