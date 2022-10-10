from sqlalchemy import create_engine
from conf import POSTGRES


engine = create_engine(POSTGRES)

engine.connect()

print(engine)
