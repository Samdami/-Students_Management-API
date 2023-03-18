from flask_restx import fields



lecturer_signup_field = {
    'first_name': fields.String(required=True, description="A name"),
    'last_name': fields.String(required=True, description="A name"),
    'email': fields.String(required=True, description='User email address'),
    'user_type': fields.String(required=True, description='User type'),
    'password': fields.String(required=True, description='Password of the User')
}


pasword_reset_request_field = {
    'email': fields.String(required=True, description='User email address')
}

password_reset_field = {
    'password': fields.String(required=True, description='User Password'),
    'confirm_password': fields.String(required=True, description='User Confirm Password')
}
