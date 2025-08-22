


from db import db
from models.course import Course
from models.padawan_course import PadawanCourse
from reflection import serialize

def create_course(data):
    course = Course(**data)
    db.session.add(course)
    db.session.commit()
    return serialize(course)

def get_courses_by_difficulty(difficulty):
    courses = Course.query.filter_by(difficulty=difficulty).all()
    return [serialize(course) for course in courses]

def update_course(course_id, updates):
    course = db.session.get(Course, course_id)
    if not course:
        return None
    for key, value in updates.items():
        setattr(course, key, value)
    db.session.commit()
    return serialize(course)

def delete_course(course_id):
    PadawanCourse.query.filter_by(course_id=course_id).delete()
    course = db.session.get(Course, course_id)
    if course:
        db.session.delete(course)
        db.session.commit()
        return True
    return False
