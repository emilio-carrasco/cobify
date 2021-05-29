import pandas as pd
import config.config as conf
from config.config import engine


df_local=pd.read_csv('./data/data_clean.csv')

print("Cargando funciones de Bases de datos")


def carga_df_local():
    try:
        df=pd.read_csv('./data/mediciones.csv')
        return (df.to_sql(f'{conf.tabla1}', con=engine, if_exists='append', index = False),200)
    except: rerturn({"Mensaje":"Problema al cargar la base de datos"},500)
    

def eliminar():
    engine.execute("DROP DATABASE cobify;")
    return "DROPPED DB"  

def crea():
    print("Creando base de datos")
    try:
        engine.execute("CREATE DATABASE IF NOT EXISTS cobify;")
        return ({"mensaje": "BD y tablas creadas"},200)

    except: 
        return({"mensaje":"problema al cargar la base de datos"},500)