


from flask import Blueprint, request, jsonify
from controllers.auth_controller import authenticate_user
from schemas.user_schema import user_schema

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password required"}), 400

    token, user = authenticate_user(username, password)
    if not token:
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({
        "access_token": token,
        "user": user_schema.dump(user)
    }), 200
