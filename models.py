"""CREATING A DATABASE FOR APP.PY USAGE"""
from app import db
from sqlalchemy.dialects.mysql import BIGINT

class Person(db.Model):
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    favorites =  db.Column(db.ARRAY(db.String))
    applied =  db.Column(db.ARRAY(db.String))
    #Jobs = db.relationship('Address', backref='person', lazy=True)
    
    def __init__(self,id,email,favorites,applied):
        self.id=id
        self.email=email
        self.favorites=favorites
        self.applied=applied
    
class Jobs(db.Model):
    job_id = db.Column(db.String, primary_key=True)
    job_title=db.Column(db.String(120), nullable=False)
    job_location=db.Column(db.String(120), nullable=False)
    job_salary=db.Column(db.String(120), nullable=False)
   #person_id = db.Column(db.Integer, db.ForeignKey('person.id'),####to be deleted
    #    nullable=False)
    
    def __init__(self,job_id,job_title,job_location,job_salary):
        self.job_id=job_id
        self.job_title=job_title
        self.job_location=job_location
        self.job_salary=job_salary
        
def __repr__(self):
        return '<Person %r>' % self.email
        
        
        
