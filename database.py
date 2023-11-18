from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://root:haniy9186@localhost:5050/jovian_careers?charset=utf8mb4"

engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._asdict()))
        return jobs