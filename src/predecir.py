import pickle

def estimacion(X):
    with open('mis_proyectos/cobify/modelos/modelo.pickle', 'r') as archivo:
        modelo = pickle.load(archivo)
    return modelo.predict(X)
