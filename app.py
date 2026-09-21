# ============================================================
# Importar librerías estándar
# ============================================================
import streamlit as st
import pandas as pd
import numpy as np

# ============================================================
# LIBRERÍAS EXTERNAS DEL PROYECTO
# ============================================================
from libreria_funciones_proyecto1 import calcular_punto_equilibrio
from librería_clases_proyecto1 import InventarioProducto

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================
st.set_page_config(
    page_title="Proyecto 1 - Python Fundamentals",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)


modulos = st.sidebar.selectbox("Selecione el módulo",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

# ============================================================
# HOME
# ============================================================
if modulos == "Home":
  st.title("HOME")

elif modulos == "Ejercicio 1":
  st.title("EJERCICIO 1")

elif modulos == "Ejercicio 2":
  st.write("Te encuentras en el módulo de Funciones")
  
elif modulos == "Ejercicio 3":
  st.write("Te encuentras en el módulo de Funciones")

else:
  st.write("Te encuentras en el Ejercicio 4")
