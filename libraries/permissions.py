

from functools import wraps
from flask import request, jsonify
from models.user import User

RANK_HIERARCHY = {
    "Youngling": 0,
    "Padawan": 1,
    "Knight": 2,
    "Master": 3,
    "Council": 4,
    "Grand Master": 5
}

def get_current_user():
    user_id = request.headers.get('X-User-Id')
    if not user_id:
        return None
    return User.query.get(user_id)

def rank_required(required_rank):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user = get_current_user()
            if not user:
                return jsonify({"message": "User not found"}), 404
            if RANK_HIERARCHY.get(user.force_rank, -1) < RANK_HIERARCHY.get(required_rank, 999):
                return jsonify({"message": f"{required_rank}+ required"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

def self_or_rank(required_rank):
    def decorator(fn):
        @wraps(fn)
        def wrapper(user_id, *args, **kwargs):
            user = get_current_user()
            if not user:
                return jsonify({"message": "User not found"}), 404
            if str(user.user_id) != str(user_id) and RANK_HIERARCHY.get(user.force_rank, 0) < RANK_HIERARCHY.get(required_rank, 0):
                return jsonify({"message": "Unauthorized"}), 403
            return fn(user_id, *args, **kwargs)
        return wrapper
    return decorator

def owner_only_or_rank(required_rank):
    def decorator(fn):
        @wraps(fn)
        def wrapper(saber_id, *args, **kwargs):
            from models.lightsaber import Lightsaber
            saber = Lightsaber.query.get(saber_id)
            if not saber:
                return jsonify({"message": "Saber not found"}), 404
            user = get_current_user()
            if not user:
                return jsonify({"message": "User not found"}), 404
            if saber.owner_id != user.user_id and RANK_HIERARCHY.get(user.force_rank, 0) < RANK_HIERARCHY.get(required_rank, 0):
                return jsonify({"message": "Permission denied"}), 403
            return fn(saber_id, *args, **kwargs)
        return wrapper
    return decorator
