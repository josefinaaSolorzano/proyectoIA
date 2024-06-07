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
        "Dunks",
        "Dunks.jpg",
        "https://www.nike.com.ar/nike/hombre/calzado/dunk?map=category-1,category-2,category-3,icono",
        "Las Nike Dunks nacieron en los años 80 como zapatillas de baloncesto, pero rápidamente se convirtieron en un ícono del skateboard y la moda urbana."
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