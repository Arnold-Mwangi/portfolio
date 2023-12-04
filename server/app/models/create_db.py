from database import Base, engine
from model import *

print("Creating cloud db....")
Base.metadata.create_all(engine)
