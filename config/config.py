import os
import dotenv
import sqlalchemy as alch
from  json import load

def lee_archivo_json(ruta):
    
    try:
        with open(ruta) as archivo:
            opcionesjson = load(archivo)
            return opcionesjson
            
    except Exception as ex :
        plantilla = "Ocurrió una excepción de tipo {0}. Argumentos:\n{1!r}"
        mensaje = plantilla.format(type(ex).__name__, ex.args)
        print(mensaje)
        print("Ruta: ",ruta)
        print("Error en: lee_archivo_json")

opciones = lee_archivo_json('./config/opciones.json')



dotenv.load_dotenv()

passw = os.getenv("pass_sql")
dbName= os.getenv("db")

tabla1 = os.getenv("tabla")
api_id_here = os.getenv("api_id_here")
api_code_here= os.getenv("api_code_here")

#CONECTO CON LA BASE DE DATOS
os.system("sudo /etc/init.d/mysql start")
conexion=f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(conexion)

dict_fuel = opciones['combustible']
precio = opciones['precio_litro']