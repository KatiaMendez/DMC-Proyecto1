import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Katia Mendez")

modulos = st.sidebar.selectbox("Selecione el módulo",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if modulos == "Home":
  st.write("Te encuentras en el módulo de listas")

elif modulos == "Ejercicio 1":
  st.write("Te encuentras en el módulo de arreglos")

elif modulos == "Ejercicio 2":
  st.write("Te encuentras en el módulo de Funciones")
  
elif modulos == "Ejercicio 3":
  st.write("Te encuentras en el módulo de Funciones")

else:
  st.write("Te encuentras en el Ejercicio 4")
