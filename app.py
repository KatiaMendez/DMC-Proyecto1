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
    st.title("📊 Ejercicio 2 – Registro con NumPy, arrays y DataFrame")

    st.markdown(
        """
        Este ejercicio utiliza **arrays de NumPy** para almacenar
        los registros y posteriormente convierte dichos arrays en
        un **DataFrame de Pandas** para su visualización.
        """
    )

    st.subheader("Registrar producto")

    col1, col2 = st.columns(2)

    with col1:
        nombre_producto = st.text_input(
            "Nombre del producto",
            placeholder="Ej. Laptop",
            key="e2_nombre",
        )

        categoria = st.selectbox(
            "Categoría",
            [
                "Tecnología",
                "Oficina",
                "Hogar",
                "Servicios",
                "Otros",
            ],
            key="e2_categoria",
        )

    with col2:
        precio = st.number_input(
            "Precio unitario",
            min_value=0.01,
            value=100.00,
            step=10.00,
            key="e2_precio",
        )

        cantidad = st.number_input(
            "Cantidad",
            min_value=1,
            value=1,
            step=1,
            key="e2_cantidad",
        )

    total = precio * cantidad
    st.info(f"Total calculado: **S/ {total:,.2f}**")

    if st.button(
        "➕ Agregar producto",
        type="primary",
        key="e2_agregar",
    ):
        if not nombre_producto.strip():
            mostrar_error("Ingresa el nombre del producto.")
        else:
            datos = st.session_state.productos

            datos["nombre"] = np.append(
                datos["nombre"], nombre_producto.strip()
            )
            datos["categoria"] = np.append(
                datos["categoria"], categoria
            )
            datos["precio"] = np.append(
                datos["precio"], float(precio)
            )
            datos["cantidad"] = np.append(
                datos["cantidad"], int(cantidad)
            )
            datos["total"] = np.append(
                datos["total"], float(total)
            )

            st.success("Producto agregado correctamente.")

    st.markdown("---")
    st.subheader("DataFrame actualizado")

    df_productos = dataframe_productos()

    if df_productos.empty:
        st.info("Todavía no existen productos registrados.")
    else:
        st.dataframe(
            df_productos,
            use_container_width=True,
            hide_index=True,
        )

        st.metric(
            "Valor total registrado",
            f"S/ {df_productos['Total'].sum():,.2f}",
        )

    st.markdown("---")

    if st.button("🗑️ Limpiar productos", key="e2_limpiar"):
        st.session_state.productos = {
            "nombre": np.array([], dtype=str),
            "categoria": np.array([], dtype=str),
            "precio": np.array([], dtype=float),
            "cantidad": np.array([], dtype=int),
            "total": np.array([], dtype=float),
        }
        st.rerun()



# ============================================================
# EJERCICIO 3
# ============================================================

elif modulos == "Ejercicio 3":
    st.title("📈 Ejercicio 3 – Función desde una librería externa")

    st.markdown(
        """
        Para este ejercicio se utiliza una función importada desde
        **libreria_funciones_proyecto1.py**.

        La función seleccionada corresponde al cálculo del
        **punto de equilibrio**, una métrica utilizada en análisis
        de negocios.
        """
    )

    st.subheader("Selección de función")

    funcion_seleccionada = st.selectbox(
        "Selecciona la función",
        ["Calcular punto de equilibrio"],
        key="e3_funcion",
    )

    if funcion_seleccionada == "Calcular punto de equilibrio":
        st.markdown(
            """
            **Fórmulas utilizadas por la librería:**

            - Margen de contribución = Precio unitario − Costo variable unitario
            - Punto de equilibrio (unidades) =
              Costos fijos / Margen de contribución
            - Punto de equilibrio (ventas) =
              Unidades de equilibrio × Precio unitario
            """
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            costos_fijos = st.number_input(
                "Costos fijos",
                min_value=0.01,
                value=10000.00,
                step=500.00,
                key="e3_costos_fijos",
            )

        with col2:
            precio_unitario = st.number_input(
                "Precio unitario",
                min_value=0.01,
                value=100.00,
                step=5.00,
                key="e3_precio",
            )

        with col3:
            costo_variable_unitario = st.number_input(
                "Costo variable unitario",
                min_value=0.00,
                value=40.00,
                step=5.00,
                key="e3_costo_variable",
            )

        if st.button(
            "▶️ Ejecutar función",
            type="primary",
            key="e3_ejecutar",
        ):
            try:
                resultado = calcular_punto_equilibrio(
                    costos_fijos=costos_fijos,
                    precio_unitario=precio_unitario,
                    costo_variable_unitario=costo_variable_unitario,
                )

                registro = {
                    "Función": funcion_seleccionada,
                    "Costos fijos": costos_fijos,
                    "Precio unitario": precio_unitario,
                    "Costo variable unitario": costo_variable_unitario,
                    "Margen contribución": resultado[
                        "margen_contribucion_unitario"
                    ],
                    "Punto equilibrio unidades": resultado[
                        "punto_equilibrio_unidades"
                    ],
                    "Punto equilibrio ventas": resultado[
                        "punto_equilibrio_ventas"
                    ],
                }

                st.session_state.historial_punto_equilibrio.append(
                    registro
                )

                st.success("Función ejecutada correctamente.")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Margen de contribución",
                        f"S/ {resultado['margen_contribucion_unitario']:,.2f}",
                    )

                with col2:
                    st.metric(
                        "Punto de equilibrio",
                        f"{resultado['punto_equilibrio_unidades']:,.2f} unidades",
                    )

                with col3:
                    st.metric(
                        "Ventas de equilibrio",
                        f"S/ {resultado['punto_equilibrio_ventas']:,.2f}",
                    )

            except ValueError as error:
                mostrar_error(str(error))

    st.markdown("---")
    st.subheader("📋 Histórico de resultados")

    if st.session_state.historial_punto_equilibrio:
        df_historial = pd.DataFrame(
            st.session_state.historial_punto_equilibrio
        )

        st.dataframe(
            df_historial,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Todavía no se ha ejecutado la función.")

    if st.button("🗑️ Limpiar histórico", key="e3_limpiar"):
        st.session_state.historial_punto_equilibrio = []
        st.rerun()


# ============================================================
# EJERCICIO 4
# ============================================================

else:
    st.title("📦 Ejercicio 4 – Clase externa con CRUD")

    st.markdown(
        """
        Para este ejercicio se utiliza la clase
        **InventarioProducto** de la librería
        **librería_clases_proyecto1.py**.

        Se implementan las cuatro operaciones básicas de un CRUD:

        - **Crear:** registrar un producto.
        - **Leer:** visualizar los productos registrados.
        - **Actualizar:** modificar un producto.
        - **Eliminar:** eliminar un producto.
        """
    )

    st.subheader("Selección de clase")

    clase_seleccionada = st.selectbox(
        "Selecciona la clase",
        ["InventarioProducto"],
        key="e4_clase",
    )

    st.caption(
        "Clase seleccionada: "
        f"**{clase_seleccionada}**. Permite calcular valor de "
        "inventario, margen unitario, margen porcentual y necesidad "
        "de reposición."
    )

    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(
        ["➕ Crear", "📖 Leer", "✏️ Actualizar", "🗑️ Eliminar"]
    )

    # --------------------------------------------------------
    # CREATE
    # --------------------------------------------------------
    with tab_crear:
        st.subheader("Crear nuevo producto")

        col1, col2 = st.columns(2)

        with col1:
            nombre = st.text_input(
                "Nombre del producto",
                placeholder="Ej. Monitor",
                key="e4_crear_nombre",
            )

            costo_unitario = st.number_input(
                "Costo unitario",
                min_value=0.01,
                value=100.00,
                step=10.00,
                key="e4_crear_costo",
            )

            precio_unitario = st.number_input(
                "Precio unitario",
                min_value=0.01,
                value=150.00,
                step=10.00,
                key="e4_crear_precio",
            )

        with col2:
            stock_actual = st.number_input(
                "Stock actual",
                min_value=0,
                value=10,
                step=1,
                key="e4_crear_stock",
            )

            stock_minimo = st.number_input(
                "Stock mínimo",
                min_value=0,
                value=5,
                step=1,
                key="e4_crear_minimo",
            )

        if st.button(
            "💾 Crear registro",
            type="primary",
            key="e4_crear",
        ):
            try:
                if not nombre.strip():
                    raise ValueError(
                        "El nombre del producto es obligatorio."
                    )

                nuevo_producto = InventarioProducto(
                    nombre=nombre.strip(),
                    costo_unitario=float(costo_unitario),
                    precio_unitario=float(precio_unitario),
                    stock_actual=int(stock_actual),
                    stock_minimo=int(stock_minimo),
                )

                st.session_state.inventario_crud.append(
                    nuevo_producto
                )

                st.success("Registro creado correctamente.")

            except ValueError as error:
                mostrar_error(str(error))







