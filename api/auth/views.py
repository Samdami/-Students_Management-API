from flask import request
from flask_restx import Namespace, Resource, fields
from ..models.users import User, Student, Admin
from ..models.lecturer import Lecturer
from datetime import datetime
from ..utils import db, generate_random_string
from ..utils.blocklist import BLOCKLIST
from werkzeug.security import check_password_hash, generate_password_hash
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from .serializers_utils import password_reset_field, pasword_reset_request_field, lecturer_signup_field
from ..decorators import admin_required

auth_namespace = Namespace('auth', description='name space for authentication')



lecturer_signup_model = auth_namespace.model('Lecturer Signup Model', lecturer_signup_field)

password_reset_request_model = auth_namespace.model('PasswordResetRequest', pasword_reset_request_field)

password_reset_model = auth_namespace.model('PasswordReset', password_reset_field)

signup_model = auth_namespace.model(
    'Signup', {
        'first_name': fields.String(required=True, description="A name"),
        'last_name': fields.String(required=True, description="A name"),
        'email': fields.String(required=True, description="An email"),
        'user_type': fields.String(required=True, description='User type'),
        'password': fields.String(required=True, description="A password")
    }
)
login_model = auth_namespace.model(
    'Login', {
        'email': fields.String(required=True, description="User's Email"),
        'password': fields.String(required=True, description="User's Password")
    }
)


@auth_namespace.route('/signup')
class SignUp(Resource):

    @auth_namespace.expect(signup_model)
    # @auth_namespace.marshal_with(signup_model)
    @auth_namespace.doc(
        description="""
            User can register
        """
    )
    def post(self):
        """
            Register a User 
        """

        data = request.get_json()
        
                # check if lecturer already exists
        user = User.query.filter_by(email=data.get('email')).first()
        if user:
            return {
                'message': "Email already exists"
            }, HTTPStatus.CONFLICT
        

        current_year =  str(datetime.now().year)    
        if data.get('user_type') == 'student':
            admission = generate_random_string(5) + current_year
            new_user = Student(
                email = data.get('email'),
                first_name = data.get('first_name'),
                last_name = data.get('last_name'),
                password_hash = generate_password_hash(data.get('password')),
                matric_no = admission,
                user_type = 'student'
            )
        elif data.get('user_type') == 'admin':
            new_user = Admin(
                email = data.get('email'),
                first_name = data.get('first_name'),
                last_name = data.get('last_name'),
                password_hash = generate_password_hash(data.get('password')),
                user_type = 'admin'
            )
        else:
            return {
                'message': 'Invalid user type'
            }, HTTPStatus.BAD_REQUEST
            
        
        
        try:
            new_user.save()
               
            return {
                'message': 'Welcome'
            },HTTPStatus.CREATED

        except:
            db.session.rollback()
            return {
                'message': 'CAN ADD USER SOMETHING WENT WRORG'
            }, HTTPStatus.INTERNAL_SERVER_ERROR    
            
            
@auth_namespace.route('/signup/lecturer')
class SignUpLecturer(Resource):
    @auth_namespace.expect(lecturer_signup_model)
    @auth_namespace.doc(
        description="""
            This route is only accessible to admin allows an admin to regiser a lecturer
        """
    )
    @admin_required()
    def post(self):
        """
            Register a lecturer
        """
        data = request.get_json()

        # check if lecturer already exists
        user = User.query.filter_by(email=data.get('email')).first()
        if user:
            return {
                'message': "Email already exists"
            }, HTTPStatus.CONFLICT
        
        username = generate_random_string(10)
        current_year =  str(datetime.now().year)


        new_user = Lecturer(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            email = data.get('email'),
            user_type = 'lecturer',
            password_hash = generate_password_hash(data.get('password'))
        
            
            )

        try:
            new_user.save()
        except:
            db.session.rollback()
            return {
                'message': 'Something went wrong'
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        return {
            'message': f"Welcome You have successfully registered "
        }
            
        

@auth_namespace.route('/login')
class Login(Resource):
    @auth_namespace.expect(login_model)
    @auth_namespace.doc(
        description="""
            It allows a user to login
        """    
        )
    def post(self):
        """
            Generate JWT Token
        """
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if (user is not None) and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)

            response = {
                'access_token': access_token,
                'refresh_token': refresh_token
            }

            return response, HTTPStatus.CREATED


@auth_namespace.route('/refresh')
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """
            Refresh Access Token
        """
        user = get_jwt_identity()

        access_token = create_access_token(identity=user)

        return {'access_token': access_token}, HTTPStatus.OK



@auth_namespace.route('/logout')
class Logout(Resource):
    @auth_namespace.doc(
        description="""
            It allows the user to revoke their access token 
        """
    )
    @jwt_required()
    def post(self):
        """
            Log the User Out by revoking Access/refresh token
        """
        token = get_jwt()
        jti = token['jti']
        token_type = token['type']
        user_identity = get_jwt_identity()
        BLOCKLIST.add(jti)

        return {
            'message': 'Successfully logged out and token revoked successfully.'
        }, HTTPStatus.OK
        
