from ..utils import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)
    user_type = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_on': user_type,
        'polymorphic_identity': 'user'
    }

    def __repr__(self):
        return f"<{self.email}>"

    def save(self):
        db.session.add(self)
        db.session.commit()        
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    
    
class Student(User):
    __tablename__ = 'students'
    id = db.Column(db.Integer(), db.ForeignKey('users_id'), primary_key=True)
    matric_no = db.Column(db.String(30), unique=True)
    course = db.relationship('Course', secondary='student_course')
    score = db.relationship('Score', backref="student_score", lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }

    def __repr__(self):
        return f"<Student {self.matric_no}>"
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)    
    
    
class Admin(User):
    __tablename__ = 'admin'
    id = db.Column(db.Integer(), db.ForeignKey('users_id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)    
    


    