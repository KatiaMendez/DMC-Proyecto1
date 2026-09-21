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

# ============================================================
# SIDEBAR / NAVEGACIÓN
# ============================================================
st.sidebar.title("🐍 Python Fundamentals")
st.sidebar.markdown("---")
modulos = st.sidebar.selectbox("Menú principal",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
st.sidebar.markdown("---")
st.sidebar.caption(
    "Proyecto Aplicado en Streamlit\n"
    "Módulo 1 – Python Fundamentals"
)

# ============================================================
# HOME
# ============================================================
if modulos == "Home":
    st.title("🐍 Proyecto 1 – Python Fundamentals")
    st.subheader("Especialización Python for Analytics")

    st.markdown(
        """
        ### Presentación

        Esta aplicación integra los principales conceptos trabajados
        durante el Módulo 1 de Python Fundamentals: variables,
        estructuras de datos, control de flujo, funciones,
        programación funcional y programación orientada a objetos.

        La aplicación está organizada en cuatro ejercicios prácticos
        desarrollados con Streamlit.
        """
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👤 Datos del estudiante")
        st.write(f"**Nombre:** Katia Roxana Mendez Cortez")
        st.write("**Módulo:** Python Fundamentals")
        st.write(f"**Año:** 2026")

    with col2:
        st.markdown("### 🛠️ Tecnologías utilizadas")
        st.write("• Python")
        st.write("• Streamlit")
        st.write("• NumPy")
        st.write("• Pandas")
        st.write("• Programación funcional")
        st.write("• Programación orientada a objetos")

    st.markdown("---")

    st.markdown(
        """
        ### 📌 Descripción del proyecto

        **Ejercicio 1:** registro de movimientos financieros mediante
        una lista y cálculo del flujo de caja.

        **Ejercicio 2:** registro de productos utilizando arrays de
        NumPy y visualización mediante un DataFrame.

        **Ejercicio 3:** utilización de una función proveniente de una
        librería externa del proyecto.

        **Ejercicio 4:** utilización de una clase proveniente de una
        librería externa, implementando operaciones CRUD
        (Crear, Leer, Actualizar y Eliminar).

        Selecciona una opción en el menú lateral para comenzar.
        """
    )

    st.info(
        "Antes de publicar en GitHub, reemplaza "
        "'TU NOMBRE COMPLETO' por tu nombre real."
    )


elif modulos == "Ejercicio 1":
  st.title("EJERCICIO 1")

elif modulos == "Ejercicio 2":
  st.write("EJERCICIO 2")
  
elif modulos == "Ejercicio 3":
  st.write("EJERCICIO 3")

else:
  st.write("EJERCICIO 4")
