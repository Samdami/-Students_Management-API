from flask_restx import fields


student_model = {
    'id': fields.String(),
    'first_name': fields.String(required=True, description="A name"),
    'last_name': fields.String(required=True, description="A name"),
    'email': fields.String(required=True, description='Students email address'),
    'matric_no': fields.String(required=True, description="Admission Number of the Student"),
}

update_student_model = {
    'first_name': fields.String(required=True, description="A name"),
    'last_name': fields.String(required=True, description="A name"),
    'email': fields.String(required=True, description="Email of the Student")
}

student_score_model = {
    'student_id': fields.Integer(required=False, description='ID of student'),
    'score': fields.Integer(required=True, description="Score value"),
}

course_model = {
    'student_id': fields.Integer(required=True),
}

course_retrieve_model =  {
    'id': fields.Integer(),
    'first_name': fields.String(required=True, description="A name"),
    'last_name': fields.String(required=True, description="A name"),
    'course_code': fields.String(description="A course code"),
    'lecturer_id': fields.Integer(), 
    'created_at': fields.DateTime( description="Course creation date"),
}

create_course_model = {
    'first_name': fields.String(required=True, description="A name"),
    'last_name': fields.String(required=True, description="A name"),
    'lecturer_id': fields.Integer(required=True, description="Course Lecturer ID")
}

student_register_for_course_model = {
    'student_id': fields.Integer(required=True, description='ID of student'),
}

course_lecturer_model = {
    'first_name': fields.String(required=True, description="A name"),
    'last_name': fields.String(required=True, description="A name"),
    'email': fields.String(required=True, description='Lecturer email address'),
    'created_at': fields.DateTime( description="Course creation date")
}

gpa_model = {
    'student_id': fields.String(required=True, description="Student Name"),
    'gpa': fields.Float(required=True, description="GPA"),
    'score': fields.String(required=True, description="Grade"),
    'percent': fields.String(required=True, description="Percentage")
}
