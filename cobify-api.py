from flask import Flask, request 
import markdown.extensions.fenced_code
from src.ruta import estimador_ruta as ruta
import basedatos as db
import pandas as pd
import config.config as conf
from src.predecir import estimacion

print(" - - - Iniziando API")
app = Flask(__name__)
print(" - - - Carga Flask", app)

#////////////////////////////////    GET    /////////////////////////////////////////////////////
@app.route("/")
@app.route("/index")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

@app.route("/test", methods=["GET"])
def testo():
    return ({"mensaje": "Esto es un test"},200)

@app.route("/calculator", methods=["GET"])
def calculator():
    try:
        origen=request.args.get("origen",None)
        destino = request.args.get("destino", None)
        ciudad_origen = request.args.get("ciudad_origen", None)
        ciudad_destino = request.args.get("ciudad_destino", None)
        nieve = request.args.get("nieve", None)
        sol = request.args.get("sol", None)
        lluvia = request.args.get("lluvia", None)
        ac = request.args.get("ac", None)
        combus = request.args.get("combustible", None)

        combus_dummy=conf.dict_fuel[combus]

        (distancia, tiempo, velocidad) = ruta(origen, destino, ciudad_origen , ciudad_destino)
        x = pd.Series([distancia, velocidad, combus_dummy,ac,lluvia,sol,nieve])
        consumo = estimacion(x)
        coste = conf.precio['combus']*consumo
        return ({"consumo":consumo,"coste":coste},200)
    except:
        return "error"

#////////////////////////////////    POST    /////////////////////////////////////////////////////
@app.route("/drop", methods=["POST"])
def eliminar():
    """Drops all the schems and tables in db

    Returns:
        str: Load done or error
    """
 
    return db.eliminar()


@app.route("/carga", methods=["POST"])
def carga():
    return db.carga_df_local()

@app.route("/creadb", methods=["POST"])
def creabase():
    return db.crea()

app.run("localhost", 5001, debug=True)
