#from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="OurSoleMate",
    page_icon="logoNike.ico",  # Asegúrate de que la ruta al archivo de imagen sea correcta
    layout="wide"
)

st.markdown(
        """
        <style>
        .css-1l02z1r {
            font-size: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            text-align: justify;
            padding: 20px;
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )


st.title('¿Ya tenes tu par?')
st.subheader('Hacé click en los modelos para encontrar tu SoleMate', divider='red')


# Definir una función para mostrar el contenido de cada contenedor

# Definir una función para mostrar el contenido con imagen y texto al costado
def mostrar_contenido(titulo, imagen_path, enlace, texto):
    # Dividir el contenedor en dos columnas
    col1, col2 = st.columns([1.5 , 2.5])  # La primera columna ocupa 1 unidad y la segunda 3 unidades

    # Mostrar la imagen en la primera columna
    with col1:
        st.image(imagen_path, width=200)

    # Mostrar el texto al costado de la imagen en la segunda columna
    with col2:
        st.header(titulo)
        st.markdown(texto)
        if st.button("Haz clic aquí para ir a la página", key=f"button_{titulo}", type="primary"):
            st.markdown(f'<a href="{enlace}" target="_blank">Enlace externo</a>', unsafe_allow_html=True)
     


# Crear los contenedores y mostrar el contenido con imagen y texto al costado
with st.container(border=True):
    mostrar_contenido(
        "Air Forces",
        "AirForces.jpeg",
        "https://www.nike.com.ar/air%201%20force?_q=air%201%20force&map=ft",
        "Las Nike Air Force 1 son un ícono de la moda urbana desde su lanzamiento en 1982. Originalmente diseñadas como zapatillas de baloncesto, han evolucionado para convertirse en una pieza esencial del streetwear."
    )
    

with st.container(border=True):
    mostrar_contenido(
        "Air Maxes",
        "AirMaxes.jpg",
        "https://www.nike.com.ar/air%20max?_q=air%20max&map=ft",
        "Las Nike Air Max son famosas por su unidad de aire visible en la suela, introducida por primera vez en 1987. Han evolucionado con diferentes modelos y tecnologías a lo largo de los años."
    )

with st.container(border=True):
    mostrar_contenido(
        "Jordans",
        "Jordans.jpg",
        "https://www.nike.com.ar/nike/air-jordan-1?map=category-1,icono",
        "Las Air Jordans son una línea de zapatillas creada en colaboración con el legendario jugador de baloncesto Michael Jordan. Cada modelo tiene un diseño único y una historia detrás."
    )

with st.container(border=True):
    mostrar_contenido(
        "Cleats",
        "Cleats2.jpg",
        "https://www.nike.com.ar/nike/hombre/calzado/botines?map=category-1,category-2,category-3,tipo-de-producto",
        "Las Nike Cleats están diseñadas para ofrecer el mejor rendimiento en deportes como el fútbol, béisbol y fútbol americano. Son conocidas por su tracción y durabilidad en terrenos específicos."
    )

with st.container(border=True):
    mostrar_contenido(
        "Dunks",
        "Dunks.jpg",
        "https://www.nike.com.ar/nike/hombre/calzado/dunk?map=category-1,category-2,category-3,icono",
        "Las Nike Dunks nacieron en los años 80 como zapatillas de baloncesto, pero rápidamente se convirtieron en un ícono del skateboard y la moda urbana."
    )

# Crear un contenedor dentro de la barra lateral
with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")


with st.sidebar:
    st.container(height=30, border=False)