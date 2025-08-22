


from db import db
from models.crystal import Crystal
from reflection import serialize

def create_crystal(data):
    crystal = Crystal(**data)
    db.session.add(crystal)
    db.session.commit()
    return serialize(crystal)

def get_crystals_by_rarity(rarity_level):
    crystals = Crystal.query.filter_by(rarity_level=rarity_level).all()
    return [serialize(c) for c in crystals]
