from flask_sqlalchemy import SQLAlchemy

import secrets
import string
import smtplib
from email.mime.text import MIMEText
from flask_sqlalchemy import SQLAlchemy
from email.mime.multipart import MIMEMultipart

db = SQLAlchemy()


def generate_reset_token(length):
    return secrets.token_hex(length)


def generate_random_string(length):
    """
    Generate a random string of alphanumeric characters of given length
    """
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string



def grade(score):
    if score >= 95:
        return 'A+'
    elif score >= 90:
        return 'A'
    elif score >= 85:
        return 'A-'
    elif score >= 80:
        return 'B+'
    elif score >= 75:
        return 'B'
    elif score >= 70:
        return 'B-'
    elif score >= 65:
        return 'C+'
    elif score >= 60:
        return 'C'
    elif score >= 55:
        return 'C-'
    elif score >= 50:
        return 'D+'
    elif score >= 45:
        return 'D'
    else:
        return 'F'


def letter_grade_to_gpa(letter_grade):
    """
    Converts a letter grade to a GPA value.
    """
    if letter_grade == "A+":
        return 4.0
    elif letter_grade == "A":
        return 4.0
    elif letter_grade == "A-":
        return 3.7
    elif letter_grade == "B+":
        return 3.3
    elif letter_grade == "B":
        return 3.0
    elif letter_grade == "B-":
        return 2.7
    elif letter_grade == "C+":
        return 2.3
    elif letter_grade == "C":
        return 2.0
    elif letter_grade == "C-":
        return 1.7
    elif letter_grade == "D+":
        return 1.3
    elif letter_grade == "D":
        return 1.0
    elif letter_grade == "F":
        return 0.0
    else:
        return None
