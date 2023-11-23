# streamlit_app.py
import streamlit as st
import datetime
from PIL import Image
import pandas as pd

@st.cache
def run_fxn(n: int) -> list:
    return range(n)

def main():
    st.title("My Streamlit App")
    
    # Add a sidebar
    st.sidebar.header("Options")
    option = st.sidebar.selectbox("Select an option", ["Home", "About", "Contact"])

    # Display content based on the selected option
    if option == "Home":
        st.write("Hola mundo")
        st.markdown("# Este es un markdown h1 \n ## Este es un h2 \n ### Este es un h3")
        st.header("Colores de texto y mensajes de error")
        st.success("Successful")
        st.info("Información!")
        st.warning("Warning")
        st.error("Error")
        st.exception("NameError('no está definido')")
        st.header("Obtener información de ayuda de Python")
        st.help(range)
        st.header("Widgets:")
        st.subheader("Checkbox")
        
        # Checkbox
        if st.checkbox("Show/Hide"):
            st.text("Mostrar o esconder")
            st.subheader("Radio")

        status = st.radio('Cuál es tu estatus?', ('Activo','Inactivo'))

        if status == 'Activo':
            st.success('Estás activo')
        else:
            st.warning('Inactivo')
            st.subheader('Selectbox')

        occupation = st.selectbox('Tu ocupación', 
                                ['Programador', 'Científico de datos', 'BI', 'Ingeniero de datos'])
        st.write('Opción seleccionada:', occupation)
        st.subheader('MultiSelect')

        location = st.multiselect('Dónde trabajas?',
                                ('México', 'Nueva York', 'Guadalajara', 'Monterrey', 'Nepal', 'Buenos Aires', 'Caracas'))

        st.write('Selección:', len(location), 'locaciones')
        st.subheader('Slider')

        level = st.slider('Cuál es tu nivel?', 1, 5)
        st.write('Nivel:', level)
        st.subheader('Buttons')
        if st.button("Acerca"):
            st.text("Streamlit es genial!")
        else:
            st.text("")
        firstname = st.text_input("Ingresa tu nombre:")
        if st.button("Aceptar"):
            result = firstname.title()
            st.success(result)
        st.subheader("Area de Texto")
        # Text Area
        message = st.text_area("Escribe un mensaje:")
        if st.button("Aceptar "):
            result = message.title()
            st.success(result)
        st.subheader("Entrada de fecha")
        # Date Input
        today = st.date_input("Hoy es", datetime.datetime.now())
        st.text(f"La fecha es {today}")
        st.subheader("Entrada de tiempo")
        # Time
        the_time = st.time_input("La hora es", datetime.time())
        st.text(f"La hora es {the_time}")
        st.header("Trabajando con archivos de imágenes, audio y video")
        # Images
        st.subheader("Archivo de imagen")
        img = Image.open("C:/Users/Daniel Cruz/Pictures/Fondos/TopG.jfif")
        st.image(img, width=300, caption="Streamlit Images")

        st.header("Otras opciones que permite la función write")
        # Writing Text/Super Fxn
        st.subheader("Texto con write")
        st.write("Texto con write")
        st.write(range(10))
        st.header("Desplegando código puro y JSON")
        st.subheader("Código puro")
        st.code("import numpy as np")
        with st.echo():
            # This will also be shown
            df = pd.DataFrame()
            df
        st.subheader("JSON")
        st.text('Mostrando JSON')
        st.json({"nombre":"Daniel", "apellido":"Cruz", "genero":"Masculino"})
        st.header("Mostrando barra de progreso, spinner y balloons")
        st.subheader("Barra de progreso")
        my_bar = st.progress(0)
        for p in range(10):
            my_bar.progress(p + 1)


    elif option == "About":
        st.write("This is the About page. Streamlit is a great tool for creating web apps!")
    elif option == "Contact":
        st.write("Contact us at contact@example.com")

if _name_ == "_main_":
    main()