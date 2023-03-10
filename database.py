# import sqlalchemy
# print(sqlalchemy.__version__)
from sqlalchemy import create_engine, text

data_connection_string = "mysql+pymysql://znf6ei2yu3dvkncvwp8t:pscale_pw_pHrwTMmFufpycmApW0mIorj9w6R10CUWmspkbJZqFpq@ap-south.connect.psdb.cloud/careers?charset=utf8mb4"
engine = create_engine(data_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print("type(result):", type(result))

  result_all = result.all()
  print("type(result.all()):", type(result_all))
  # print("result.all():", result_all)

  first_result = result_all[0]
  print("type(first_result):", type(first_result))

  first_result_dict = result_all[0]._mapping
  print("type(first_result_dict):", type(first_result_dict))
  print(first_result_dict)
