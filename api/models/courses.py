from ..utils import db
from datetime import datetime
from ..models.users import Student 

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer(), primary_key=True)
    lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturers.id'))
    

    def __repr__(self):
        return f"<Course {self.name}>"
        
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
    
class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer(), db.ForeignKey('courses.id'))
    score = db.Column(db.Float, nullable=False)
    percent = db.Column(db.String(10), nullable=True)
    gpa = db.Column(db.Float)
    created_at = db.Column(db.DateTime() , nullable=False , default=datetime.utcnow)

    def __init__(self, student_id, course_id, score, percent):
        self.student_id = student_id
        self.course_id = course_id
        self.score = score
        self.percent = percent
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
        