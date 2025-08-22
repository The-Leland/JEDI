


from db import db
from models.temple import Temple
from reflection import serialize

def create_temple(data):
    temple = Temple(**data)
    db.session.add(temple)
    db.session.commit()
    return serialize(temple)

def get_temple(temple_id):
    temple = db.session.get(Temple, temple_id)
    return serialize(temple) if temple else None

def update_temple(temple_id, updates):
    temple = db.session.get(Temple, temple_id)
    if not temple:
        return None
    for key, value in updates.items():
        setattr(temple, key, value)
    db.session.commit()
    return serialize(temple)

def delete_temple(temple_id):
    temple = db.session.get(Temple, temple_id)
    if not temple:
        return False
    temple.is_active = False
    db.session.commit()
    return True
