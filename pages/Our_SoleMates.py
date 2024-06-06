#from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st


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
    col1, col2 = st.columns([1, 3])  # La primera columna ocupa 1 unidad y la segunda 3 unidades

    # Mostrar la imagen en la primera columna
    with col1:
        st.image(imagen_path, width=150)

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
        "airfORces.jpg",
        "https://www.nike.com.ar/air%201%20force?_q=air%201%20force&map=ft",
        "Las Air Forces son un modelo icónico de zapatillas Nike conocidas por su diseño versátil y durabilidad."
    )
    

with st.container(border=True):
    mostrar_contenido(
        "Air Maxes",
        "airMaxestest.jpg",
        "https://www.nike.com.ar/air%20max?_q=air%20max&map=ft",
        "Las Air Maxes son conocidas por su estilo y comodidad, ideales para el uso diario."
    )

with st.container(border=True):
    mostrar_contenido(
        "Jordans",
        "jordan1.jpg",
        "https://www.nike.com.ar/air%201%20force?_q=air%201%20force&map=ft",
        "Las Air Forces son un modelo icónico de zapatillas Nike conocidas por su diseño versátil y durabilidad."
    )

with st.container(border=True):
    mostrar_contenido(
        "Cleads",
        "cleads.jpeg",
        "https://www.nike.com.ar/air%201%20force?_q=air%201%20force&map=ft",
        "Las Air Forces son un modelo icónico de zapatillas Nike conocidas por su diseño versátil y durabilidad."
    )

with st.container(border=True):
    mostrar_contenido(
        "Dunks",
        "dunkstest.jpg",
        "https://www.nike.com.ar/air%201%20force?_q=air%201%20force&map=ft",
        "Las Air Forces son un modelo icónico de zapatillas Nike conocidas por su diseño versátil y durabilidad."
    )

# Crear un contenedor dentro de la barra lateral
with st.sidebar:
    container = st.container()
    with container:
        st.header("Formulario de Contacto")
        st.write("Dejanos tu consulta y un asesor se pondrá en contacto contigo.")
        
        # Campos del formulario
        nombre = st.text_input("Nombre")
        email = st.text_input("Correo Electrónico")
        mensaje = st.text_area("Mensaje")
        
        # Botón de envío
        if st.button("Enviar"):
            st.success("¡Gracias por tu mensaje! Un asesor se pondrá en contacto contigo pronto.")
   
#CODIGO DE JOSE

#col1, col2, col3, col4 = st.columns(4)

#with col1:
   #st.image("airfORces.jpg")
   #if st.button("Air Forces", type="primary"):
    #st.write('<a href="https://www.nike.com.ar/air%201%20force?_q=air%201%20force&map=ft" target="_blank">Haz clic aquí para ir a la página</a>', unsafe_allow_html=True)
   
#with col2:
   #st.image("airMaxestest.jpg")
   #if st.button("Air Maxes", type="primary"):
    #st.write('<a href="https://www.nike.com.ar/air%20max?_q=air%20max&map=ft" target="_blank">Haz clic aquí para ir a la página</a>', unsafe_allow_html=True)

#with col3:
   #st.image("jordan1.jpg")
   #if st.button("Jordans", type="primary"):
    #st.write('<a href="https://www.nike.com.ar/jordan?_q=jordan&map=ft&page=2" target="_blank">Haz clic aquí para ir a la página</a>', unsafe_allow_html=True)

#with col4:
   #st.image("dunkstest.jpg")
   #if st.button("Dunks", type="primary"):
    #st.write('<a href="https://www.nike.com.ar/dunks?_q=dunks&map=ft&page=2" target="_blank">Haz clic aquí para ir a la página</a>', unsafe_allow_html=True)