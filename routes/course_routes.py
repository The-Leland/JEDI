


from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.course_controller import *
from schemas.course_schema import course_schema, courses_schema
from util.permissions import rank_required

course_bp = Blueprint("course_bp", __name__, url_prefix="/course")

@course_bp.route("", methods=["POST"])
@jwt_required()
@rank_required("Master")
def create():
    course = create_course(request.get_json())
    return course_schema.dump(course), 201

@course_bp.route("/<course_id>", methods=["PUT"])
@jwt_required()
@rank_required("Council")
def update(course_id):
    updated = update_course(course_id, request.get_json())
    if not updated:
        return {"message": "Not found"}, 404
    return course_schema.dump(updated), 200

@course_bp.route("/<course_id>", methods=["DELETE"])
@jwt_required()
@rank_required("Council")
def delete(course_id):
    if not delete_course(course_id):
        return {"message": "Not found"}, 404
    return {"message": "Deleted"}, 200

@course_bp.route("/difficulty/<difficulty>", methods=["GET"])
@jwt_required()
def list_by_difficulty(difficulty):
    return courses_schema.dump(get_courses_by_difficulty(difficulty)), 200
