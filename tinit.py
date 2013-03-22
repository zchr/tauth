#define db elements
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import requests, json, os

app = Flask(__name__)
#deployed on heroku using the addon https://addons.heroku.com/heroku-postgresql
#a terrific tutorial is: http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') #use
app.secret_key = #this is a secret key. there are many like it, but this one is mine.
db = SQLAlchemy(app)

class tweets(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tweetscreen = db.Column(db.String) #twitter handle
	tweettext = db.Column(db.String) #tweet body

	def __repr__(self):
		return '<tweet %r>' % (self.tweetscreen)

		