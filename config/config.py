import os
import dotenv
import sqlalchemy as alch

dotenv.load_dotenv()


passw = os.getenv("pass_sql")
dbName= os.getenv("db")
api_id_here = os.getenv("api_id_here")
api_code_here= os.getenv("api_code_here")

#mE CONECTO CON LA BASE DE DATOS

connectionData=f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
