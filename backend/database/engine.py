from sqlalchemy import create_engine
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
DATABASE_URL = "mysql+mysqlconnector://tuna:backend_guy@localhost:3306/mydb"
engine = create_engine(DATABASE_URL, echo=True)
