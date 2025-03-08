from flask import Flask, request
from app_src.models import db
import os
base_directory = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(base_directory,"urbanServices.sqlite3")
db.init_app(app)
app.app_context().push()


@app.route('/')
def home():
    return {"hello":"me"}

class Home():
    def get(self):
        return {"api_stat":"from_class"}, 200
    def post(self):
        return {"post":"posts"},200
home_apis = Home()
@app.route('/api', methods=["GET", "POST"])
def new_route():
    if request.method=="GET":
        return home_apis.get()
    elif request.method == "POST":
        return home_apis.post()
class newHome():
    def get(self):
        return {"new":"home_api"}
newHome_api = newHome()
@app.route('/api/class')
def new_route_1():
    return newHome_api.get()



if __name__ == "__main__":
    db.create_all()
    app.run()