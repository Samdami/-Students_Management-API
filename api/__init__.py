from flask import Flask
from flask_restx import Api
from .auth.views import auth_namespace
from .courses.views import courses_namespace
from .student.views import student_namespace
from .config.config import config_dict 
from .utils import db
from .models.users import Admin, Student
from .models.courses import Course, Score
from .models.lecturer import Lecturer
from .models.student_course import StudentCourse
from .models.users import User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound, MethodNotAllowed

def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    
    app.config.from_object(config)
    
    db.init_app(app)
    
    jwt = JWTManager(app)
    
    migrate = Migrate(app, db)
    
    authorizations = {
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': "Authorization",
            "description": "Add a JWT token to the header with ** Bearer &lt;JWT&gt; ** token to authorize"
        }
    }
    
    api = Api(app,
        version='1.0', 
        title='Student Management API', 
        description='A REST Student Management API ',
        authorizations=authorizations,
        security='Bearer Auth'
        )
    
    api.add_namespace(auth_namespace, path='/auth')  
    api.add_namespace(student_namespace, path='/students')
    api.add_namespace(courses_namespace, path='/course')
    
    @app.errorhandler(NotFound)
    def handle_not_found(error):
        return {'message': 'Not Found'}, 404
    
    @app.errorhandler(MethodNotAllowed)
    def handle_method_not_allowed(error):
        return {'message': 'Method Not Allowed'}, 405
    
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User':User,
            'Course':Course,
            'Lecturer': Lecturer,
            'Score':Score,
            'Student':Student,
            'Admin':Admin,
            'StudentCourse': StudentCourse
        }
    
    return app