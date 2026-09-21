# ============================================================
# IMPORTAR LIBRERÍAS ESTÁNDAR
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
# INICIALIZACIÓN DEL ESTADO DE LA APLICACIÓN
# ============================================================
def inicializar_estado():
    """Crea las estructuras necesarias en st.session_state."""

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    if "productos" not in st.session_state:
        st.session_state.productos = {
            "nombre": np.array([], dtype=str),
            "categoria": np.array([], dtype=str),
            "precio": np.array([], dtype=float),
            "cantidad": np.array([], dtype=int),
            "total": np.array([], dtype=float),
        }

    if "historial_punto_equilibrio" not in st.session_state:
        st.session_state.historial_punto_equilibrio = []

    if "inventario_crud" not in st.session_state:
        st.session_state.inventario_crud = []


inicializar_estado()


# ============================================================
# FUNCIONES AUXILIARES DE LA APP
# ============================================================
def mostrar_error(mensaje):
    """Muestra un mensaje de error uniforme."""
    st.error(f"⚠️ {mensaje}")


def dataframe_movimientos():
    """Convierte la lista de movimientos en DataFrame."""
    if not st.session_state.movimientos:
        return pd.DataFrame(columns=["Concepto", "Tipo", "Valor"])

    return pd.DataFrame(st.session_state.movimientos)


def dataframe_productos():
    """Convierte los arrays de productos en DataFrame."""
    datos = st.session_state.productos

    return pd.DataFrame(
        {
            "Producto": datos["nombre"],
            "Categoría": datos["categoria"],
            "Precio": datos["precio"],
            "Cantidad": datos["cantidad"],
            "Total": datos["total"],
        }
    )


def dataframe_inventario():
    """Genera el DataFrame de los objetos InventarioProducto."""
    if not st.session_state.inventario_crud:
        return pd.DataFrame(
            columns=[
                "ID",
                "Producto",
                "Costo unitario",
                "Precio unitario",
                "Stock actual",
                "Stock mínimo",
                "Valor inventario",
                "Margen unitario",
                "Margen %",
                "Reposición",
            ]
        )

    registros = []

    for indice, producto in enumerate(
        st.session_state.inventario_crud, start=1
    ):
        resumen = producto.resumen()

        registros.append(
            {
                "ID": indice,
                "Producto": resumen["producto"],
                "Costo unitario": producto.costo_unitario,
                "Precio unitario": producto.precio_unitario,
                "Stock actual": resumen["stock_actual"],
                "Stock mínimo": producto.stock_minimo,
                "Valor inventario": resumen["valor_inventario"],
                "Margen unitario": resumen["margen_unitario"],
                "Margen %": resumen["margen_pct"],
                "Reposición": (
                    "Sí" if resumen["necesita_reposicion"] else "No"
                ),
            }
        )

    return pd.DataFrame(registros)

# ============================================================
# SIDEBAR / NAVEGACIÓN
# ============================================================
st.sidebar.title("Python Fundamentals")
st.sidebar.image("LogoKRMC-rectangular.png")
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
    st.title("Proyecto 1 – Especialización en Python for Analytics")
    st.subheader("Módulo 1: Python Fundamentals")
    st.image("Python_logo.png",width =120)
       
    st.markdown("---")

    st.markdown("### 👤 Datos del estudiante")
    st.write(f"**Nombre:** Katia Roxana Mendez Cortez")
    st.write("**Sobre mí:** Profesional Especialista en Control Interno, que disfruta aprender de tecnología")
    st.write(f"**Año:** 2026")

    st.markdown("---")


    st.markdown(
        """
        ### 🛠️ Descripción del proyecto

        Esta aplicación integra los principales conceptos trabajados
        durante el Módulo 1 de Python Fundamentals.
        
        """
    )

    st.markdown("##### Tecnologías utilizadas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("• Python")
        st.write("• Streamlit")

    with col2:
        st.write("• NumPy")
        st.write("• Pandas")
        
    with col3:
        st.write("• Programación funcional")
        st.write("• Programación orientada a objetos")


    st.markdown(
        """
        ##### Ejercicios incluidos

        **Ejercicio 1:** registro de movimientos financieros mediante
        una lista y cálculo del flujo de caja.

        **Ejercicio 2:** registro de productos utilizando arrays de
        NumPy y visualización mediante un DataFrame.

        **Ejercicio 3:** utilización de una función proveniente de una
        librería externa del proyecto.

        **Ejercicio 4:** utilización de una clase proveniente de una
        librería externa, implementando operaciones CRUD
        (Crear, Leer, Actualizar y Eliminar).

        """
    )

    st.markdown(
        """
        ##### 📌 Selecciona una opción en el menú lateral para comenzar.
        """
    )

# ============================================================
# EJERCICIO 1
# ============================================================

elif modulos == "Ejercicio 1":
    st.title("💰 Ejercicio 1 – Flujo de caja con listas")

    st.markdown(
        """
        En este ejercicio se registran movimientos financieros en una
        lista. Cada movimiento contiene un concepto, un tipo
        (Ingreso o Gasto) y un valor.
        """
    )
        
    st.subheader("Registrar movimiento")

    col1, col2, col3 = st.columns(3)

    with col1:
        concepto = st.text_input(
            "Concepto",
            placeholder="Ej. Venta de producto",
            key="e1_concepto",
        )

    with col2:
        tipo = st.selectbox(
            "Tipo de movimiento",
            ["Ingreso", "Gasto"],
            key="e1_tipo",
        )

    with col3:
        valor = st.number_input(
            "Valor",
            min_value=0.01,
            value=100.00,
            step=10.00,
            key="e1_valor",
        )

    if st.button(
        "➕ Agregar movimiento",
        type="primary",
        key="e1_agregar",
    ):
        if not concepto.strip():
            mostrar_error("Ingresa un concepto para el movimiento.")
        elif valor <= 0:
            mostrar_error("El valor debe ser mayor que cero.")
        else:
            st.session_state.movimientos.append(
                {
                    "Concepto": concepto.strip(),
                    "Tipo": tipo,
                    "Valor": float(valor),
                }
            )
            st.success("Movimiento agregado correctamente.")

    st.markdown("---")
    st.subheader("Movimientos registrados")

    df_movimientos = dataframe_movimientos()

    if df_movimientos.empty:
        st.info("Todavía no se han registrado movimientos.")
    else:
        st.dataframe(
            df_movimientos,
            use_container_width=True,
            hide_index=True,
        )

        ingresos = df_movimientos.loc[
            df_movimientos["Tipo"] == "Ingreso", "Valor"
        ].sum()

        gastos = df_movimientos.loc[
            df_movimientos["Tipo"] == "Gasto", "Valor"
        ].sum()

        saldo = ingresos - gastos

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total ingresos", f"S/ {ingresos:,.2f}")

        with col2:
            st.metric("Total gastos", f"S/ {gastos:,.2f}")

        with col3:
            st.metric("Saldo final", f"S/ {saldo:,.2f}")

        if saldo >= 0:
            st.success(
                f"El flujo de caja está **a favor**. "
                f"Saldo: S/ {saldo:,.2f}"
            )
        else:
            st.error(
                f"El flujo de caja está **en contra**. "
                f"Saldo: S/ {saldo:,.2f}"
            )

    st.markdown("---")

    if st.button("🗑️ Limpiar movimientos", key="e1_limpiar"):
        st.session_state.movimientos = []
        st.rerun()



# ============================================================
# EJERCICIO 2
# ============================================================

elif modulos == "Ejercicio 2":
  st.write("EJERCICIO 2")
  
elif modulos == "Ejercicio 3":
  st.write("EJERCICIO 3")

else:
  st.write("EJERCICIO 4")







