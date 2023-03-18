from ..utils import db
from .users import User
from datetime import datetime


class Lecturer(User):
    __tablename__ = 'lecturers'
    id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)
    staff_no = db.Column(db.String(50), unique=True)
    courses = db.relationship('Course', backref='lecturer_course')

    __mapper_args__ = {
        'polymorphic_identity': 'lecturer'
    }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
