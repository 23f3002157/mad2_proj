from flask import Flask, request

app = Flask(__name__)

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
if __name__ == "__main__":
    app.run()