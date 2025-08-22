


from db import db
from models.padawan import Padawan
from models.padawan_course import PadawanCourse
from datetime import datetime
from reflection import serialize

def create_padawan(data):
    padawan = Padawan(**data)
    db.session.add(padawan)
    db.session.commit()
    return serialize(padawan)

def get_padawans():
    return [serialize(p) for p in Padawan.query.all()]

def update_padawan(padawan_id, updates):
    padawan = db.session.get(Padawan, padawan_id)
    if not padawan:
        return None
    for key, value in updates.items():
        setattr(padawan, key, value)
    db.session.commit()
    return serialize(padawan)

def promote_padawan(padawan_id):
    padawan = db.session.get(Padawan, padawan_id)
    if not padawan:
        return None
    padawan.training_level += 1
    padawan.graduation_date = datetime.utcnow()
    db.session.commit()
    return serialize(padawan)

def delete_padawan(padawan_id):
    PadawanCourse.query.filter_by(padawan_id=padawan_id).delete()
    padawan = db.session.get(Padawan, padawan_id)
    if padawan:
        db.session.delete(padawan)
        db.session.commit()
        return True
    return False
