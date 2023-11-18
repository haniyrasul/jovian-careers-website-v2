from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

db_connection_string = "mysql+pymysql://{db_username}:{db_password}@localhost:5050/jovian_careers?charset=utf8mb4"

engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._asdict()))
        return jobs