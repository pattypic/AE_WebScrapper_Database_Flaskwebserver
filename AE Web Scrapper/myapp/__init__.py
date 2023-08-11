from flask import Flask
from .models import db
from os import path

MY_DATABASE = "scraped_data.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abc123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{MY_DATABASE}'
    db.init_app(app)

    from .views import views

    create_database(app)

    app.register_blueprint(views, url_prefix='/')

    return app

def create_database(app):
    if not path.exists('myapp/' + MY_DATABASE):
        db.create_all(app=app)
        print('Created Database!')
    else:
        print('Database already exists!')
    
