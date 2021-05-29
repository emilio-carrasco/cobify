import streamlit as st
import config.config as conf
#from trafico import estimador_ruta
combustible = st.selectbox("COMBUSTIBLE",conf.opciones["combustible"])

if combustible:
    ciudad_origen= st.text_input("Ciudad origen:", "")
    origen = st.text_input("Origen:", "")
if origen:
    ciudad_destino= st.text_input("Ciudad destino:", "")
    destino= st.text_input("Destino:", "")

if origen and destino and combustible:
    pass
    #estimador_ruta(origen,destino,ciudad_origen, ciudad_destino)