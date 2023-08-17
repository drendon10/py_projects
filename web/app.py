# Simple website to understand how to create websites using python along with other frameworks in this case flask
from flask import Flask
from views import views


app = Flask(__name__) #inits app
app.register_blueprint(views, url_prefix="/views")




if __name__ == '__main__':
    app.run(debug=True, port=8000)

