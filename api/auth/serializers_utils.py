from flask_restx import fields



lecturer_signup_field = {
    'first_name': fields.String(required=True, description="A name"),
    'last_name': fields.String(required=True, description="A name"),
    'email': fields.String(required=True, description='An email'),
    'user_type': fields.String(required=True, description='User type'),
    'password': fields.String(required=True, description='Password')
}
