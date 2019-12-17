from flask import Flask, request, Response, render_template
import requests
import itertools
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField
from wtforms.validators import Regexp
from flask.json import jsonify
import re
import json
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "rock on bro"
csrf.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bandgeneratorLinusKelseycsci4131.db'
db = SQLAlchemy(app)

class BandData(db.Model):
    __tablename__ = 'thebands'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    primaryColor = db.Column(db.String(8), nullable=False)
    secondaryColor = db.Column(db.String(8), nullable=False)
    singer = db.Column(db.String(120), nullable=False)
    guitarist = db.Column(db.String(120), nullable=False)
    bassist = db.Column(db.String(120), nullable=False)
    drummer = db.Column(db.String(120), nullable=False)


db.create_all()
db.session.commit()

class Band:
    def __init__(self, name, color1, color2, singer, guitarist, bassist, drummer):
        self.name = name
        self.color1 = color1
        self.color2 = color2
        self.singer = singer
        self.guitarist = guitarist
        self.bassist = bassist
        self.drummer = drummer

class BandForm(FlaskForm):
    bandname = StringField("Band Name:")
    color1 = HiddenField("")
    color2 = HiddenField("")
    singer = SelectField("Singer:", choices = [('0','a'),('1','b'),('2','c')])
    guitarist = SelectField("Guitarist:", choices = [('3','d'),('4','e'),('5','f')])
    bassist = SelectField("Bassist:", choices = [('6','g'),('7','h'),('8','i')])
    drummer = SelectField("Drummer:", choices = [('9','j'),('10','k'),('11','l')])
    submit = SubmitField("Go")

class ItemTable(Table):
    id = Col('ident')
    name = Col('Generated Bands')
    primaryColor = Col('Primary Color')
    secondaryColor = Col('Secondary Color')
    singer = Col('Singer')
    guitarist = Col('Guitarist')
    bassist = Col('Bassist')
    drummer = Col('Drummer')


@app.route('/index')
def index():
    form = BandForm()
    return render_template("nameGenerator.html", form=form)


@app.route('/band', methods=['POST','GET'])
def band():
    form = BandForm()
    band = Band(form.bandname.data, form.color1.data, form.color2.data, form.singer.data, form.guitarist.data, form.bassist.data, form.drummer.data)
    b = BandData(name=band.name, primaryColor=band.color1, secondaryColor=band.color2, singer=band.singer, guitarist=band.guitarist, bassist=band.bassist, drummer=band.drummer)
    db.session.add(b)
    db.session.commit()

    items = BandData.query.all()
    table = ItemTable(items)

    return render_template("displayBand.html", table=table, band=band)
