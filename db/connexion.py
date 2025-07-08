from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# HOST = "m2dsia-mlops.cfuik82swe2y.eu-central-1.rds.amazonaws.com"
# SECRET = "rootM2dsia"
# DB = "m2dsia_attoisse"

# DATABASE_URL = f"mysql+pymysql://root:{SECRET}@{HOST}:3306/{DB}"

HOST = "host.docker.internal"
USERNAME= "postgres"       
PASSWORD = "pgsql%4033"
DB = "API_FLASK"

DATABASE_URL = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:5432/{DB}"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
