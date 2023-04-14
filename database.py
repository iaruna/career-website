from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://znf6ei2yu3dvkncvwp8t:pscale_pw_pHrwTMmFufpycmApW0mIorj9w6R10CUWmspkbJZqFpq@ap-south.connect.psdb.cloud/careers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs
 