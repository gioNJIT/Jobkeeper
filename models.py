"""CREATING A DATABASE FOR APP.PY USAGE"""
from app import DB

class Person(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(50), nullable=False)
    favorites =  DB.Column(DB.ARRAY(DB.Integer))
    applied =  DB.Column(DB.ARRAY(DB.Integer))
    #Jobs = db.relationship('Address', backref='person', lazy=True)
    
    def __init__(self,id,email,favorites,applied):
        self.id=id
        self.email=email
        self.favorites=favorites
        self.applied=applied
    
class Jobs(DB.Model):
    job_id = DB.Column(DB.Integer, primary_key=True)
    job_title=DB.Column(DB.String(120), nullable=False)
    job_location=DB.Column(DB.String(120), nullable=False)
    job_salary=DB.Column(DB.String(120), nullable=False)
   #person_id = db.Column(db.Integer, db.ForeignKey('person.id'),####to be deleted
    #    nullable=False)
    
    def __init__(self,job_id,job_title,job_location,job_salary):
        self.job_id=job_id
        self.job_title=job_title
        self.job_location=job_location
        self.job_salary=job_salary
        
def __repr__(self):
        return '<Person %r>' % self.email
        
        
        
