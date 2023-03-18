import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from ..models.users import User, Admin
from flask_jwt_extended import create_access_token


class TestAuth(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config=config_dict['test'])

        self.client = self.app.test_client()

        self.appctx = self.app.app_context()

        self.appctx.push()

        db.create_all()

    def tearDown(self):
        db.drop_all()

        self.appctx.pop()

        self.app = None

        self.client = None


    def test_signup(self):
        # Register an admin
        admin_signup_data = {
            "first_name": "Sam",
            "last_name": "dami",
            "email": "testuser@gmail.com",
            "user_type": "admin",
            "password": "password"
        }
        admin_signup_response = self.client.post('/auth/signup', json=admin_signup_data)

        admin = User.query.filter_by(email=admin_signup_data['email']).first()

        # assert admin.first_name== "Test User"

        # assert admin.email == admin_signup_data['email']

        assert admin_signup_response.status_code == 201

        # Register a student
        student_signup_data = {
            "first_name": "Sam",
            "last_name": "dami",
            "email": "test@gmail.com",
            "user_type": "student",
            "password": "password"
        }

        student_signup_response = self.client.post('/auth/signup', json=student_signup_data)

        student = User.query.filter_by(email=student_signup_data['email']).first()

        # assert student.name == "Student"

        # assert student.email == student_signup_data['email']

        assert student_signup_response.status_code == 201


        # Sign an Admin in
        admin_login_data = {
            "email": "admin@aotem.com",
            "password": "password"
        }

        admin_login_response = self.client.post('/auth/login', json=admin_login_data)

        assert admin_login_response.status_code == 200

        token = create_access_token(identity=admin.id)

        headers = {
            'Authorization': f'Bearer {token}'
        }


        # Sign a student in
        student_login_data = {
            "email": 'student@aotem.com',
            "password": "password"
        }

        student_login_response = self.client.post('/auth/login', json=student_login_data)

        assert student_login_response.status_code == 200

