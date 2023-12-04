from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://portfolio_db_instance_user:oPGZLCRomD6lgn2pnYEMPJjkUra2Cezs@dpg-clkb0herem5c73ag1810-a.oregon-postgres.render.com/portfolio_db_instance", echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
