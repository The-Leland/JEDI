

from db import db
from models.species import Species
from reflection import serialize

def create_species(data):
    species = Species(**data)
    db.session.add(species)
    db.session.commit()
    return serialize(species)
