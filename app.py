#Thank you LazyDeveloper for helping me in this journey !
#Must Subscribe On YouTube @LazyDeveloperr 

from flask import Flask
from application import db
from application.models import Person
app = Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():
    return '@LazyDeveloper'
manager= flast.ext.resless.APIManager(app,flask_sqlalchemy_db=db)
manager.create_api(Person, methods=['GET','POST','DELETE'])


if __name__ == "__main__":
    app.run()
