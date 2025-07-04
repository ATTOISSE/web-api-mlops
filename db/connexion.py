from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

HOST = "m2dsia-mlops.cfuik82swe2y.eu-central-1.rds.amazonaws.com"
SECRET = "rootM2dsia"
DB = "m2dsia_attoisse"

DATABASE_URL = f"mysql+pymysql://root:{SECRET}@{HOST}:3306/{DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()