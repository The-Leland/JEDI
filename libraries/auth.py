

from datetime import timedelta

def generate_token(user):
    rank_expirations = {
        "Youngling": 15,
        "Padawan": 30,
        "Knight": 60,
        "Master": 120,
        "Council": 240,
        "Grand Master": 360
    }
    minutes = rank_expirations.get(user.force_rank, 15)
    expires = timedelta(minutes=minutes)
    return f"TOKEN_FOR_{user.user_id}_EXPIRES_IN_{expires}"
