from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import datetime

db = SQLAlchemy()

# defines a AE_data model for a database table using the SQLAlchemy ORM (Object-Relational Mapping) library.
# defined as a subclass of db.Model, indicating that it is a SQLAlchemy model that will be mapped to a database table
# id, name, url attributes are defined as columns of the table, with id being the primary key column

class AmericanEagleProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    product_type = db.Column(db.String(25))
    price = db.Column(db.String(8))
    on_sale = db.Column(db.Boolean, default=False)
    discount_price = db.Column(db.String(8))
    has_promo = db.Column(db.Boolean, default=False)
    promo = db.Column(db.String(100))

class URLForm(FlaskForm):
    AEWeb_url = StringField('AEWeb_url', validators=[DataRequired()])

    

