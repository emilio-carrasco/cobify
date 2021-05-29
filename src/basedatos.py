
import pandas as pd
import config.config as conf
from config.config import engine


df_local=pd.read_csv('./data/data_clean.csv')

print("Cargando funciones de Bases de datos")
print("Motor: ", engine)

def carga_df_local():
    try:
        df=pd.read_csv('./data/mediciones.csv')
        df.to_sql(f'{conf.tabla}', con=engine, if_exists='append', index = False)
        return ({"mesanje":"Datos cargados en BD"},200)
    except: 
        return({"Mensaje":"Problema al cargar la base de datos"},500)
    

def eliminar():
    engine.execute(f"DROP TABLE {conf.dbName}.{conf.tabla};")
    return "DROPPED DB"  

def crea():
    engine.execute(f"""
    CREATE TABLE IF NOT EXISTS  cobify.rides (
    id_ride INT NOT NULL AUTO_INCREMENT,
    distance FLOAT NOT NULL,
    consume FLOAT NOT NULL,
    speed FLOAT NOT NULL,
    temp_inside FLOAT NULL,
    temp_outside FLOAT NULL,
    gas_type VARCHAR(10) NOT NULL,
    AC BINARY NULL DEFAULT false,
    rain BINARY NULL DEFAULT false,
    sun BINARY NULL DEFAULT false,
    snow BINARY NULL DEFAULT false,
    date_time DATETIME NULL DEFAULT NOW(),
    PRIMARY KEY (id_ride),
    UNIQUE INDEX id_ride_UNIQUE (id_ride ASC) VISIBLE)
    """)
    return ({"mensaje": "Tablas creadas"},200)

#    except: 
#        return({"mensaje":"problema al cargar la base de datos"},500)