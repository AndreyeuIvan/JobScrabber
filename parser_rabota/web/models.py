from main import db


class Keyword(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	data = db.relationship('Data', backref='data')

	def __repr__(self):
		return f"Keyword is '{self.name}'"


class Data(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	company = db.Column(db.String(100))
	title = db.Column(db.String(50))
	link = db.Column(db.String(200)) 
	location = db.Column(db.String(100))
	keyword = db.Column(db.Integer, db.ForeignKey("keyword.id"))

	def __repr__(self):
		return f"Job in '{self.company}', as a '{self.title}'"
