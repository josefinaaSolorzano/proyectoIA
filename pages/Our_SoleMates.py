#from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st

st.markdown(
    """
    <style>
    .css-1l02z1r {
        font-size: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        text-align: justify;
        padding: 20px;
    }
    .stTabs [role="tablist"] {
        display: flex;
        justify-content: space-between;
        width: 100%;
    }
    .stTabs [role="tab"] {
        flex-grow: 1;
        text-align: center;
    }
    .centered-header {
        text-align: center;
    }
    .align-center {
        display: flex;
        align-items: center;
        height: 100%;
    }
    .full-height {
        height: 100vh;
    }
    body, .stApp {
        background-color: black;
        color: white;
    }
    .stSidebar, .stSidebar > div {
        background-color: black !important;
    }
    [data-testid="stSidebar"] {
        background-color: #000000; /* Color negro */
    }
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4, 
    [data-testid="stSidebar"] h5, 
    [data-testid="stSidebar"] h6, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] .stButton>button {
        color: white !important;
    }
    .stSelectbox>div>div {
        background-color: black !important;
        color: white !important;
    }
    .stButton>button {
        background-color: black !important;
        color: white !important;
        border: 1px solid white !important;
    }
    .stButton>button:hover {
        background-color: #555555 !important;
        color: white !important;
    }
    .stToast {
        background-color: #555555 !important;
        color: black !important;
    }
    /* Estilo específico para la sección de carga de imágenes */
    [data-testid="stFileUploadDropzone"] div div {
        color: black !important;
    }
    h1, h2, h3, h4, h5, h6, p, .stButton>button {
        color: white !important;
    }
    /* Estilo específico para la sección de carga de imágenes */
    [data-testid="stFileUploadDropzone"] div div {
        color: black !important;
    }
    /* Estilo específico para la sección de cámara */
    [data-testid="stCameraInput"] div div {
        color: black !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.title('¿Ya tenes tu par?')
st.subheader('Hacé click en los modelos para encontrar tu SoleMate')

# Crear pestañas para mostrar el contenido
tabs = st.tabs(["Air Forces", "Air Maxes", "Jordans", "Cleats", "Dunks"])


#TAB AIRFORCES
with tabs[0]:
    st.markdown('<h2 class="centered-header">Air Forces</h2', unsafe_allow_html=True)
    st.markdown('<p class="centered-header">El modelo icónico de zapatillas Nike, conocidas por su diseño y versatilidad</p>', unsafe_allow_html=True)
   
    col1, col2, col3= st.columns([1.4,1,1.4])
    with col1:
        st.container(border = False)
    with col2: 
        st.link_button('Comprar este modelo', 'https://www.nike.com.ar/air%201%20force?_q=air%201%20force&map=ft', type='primary')
    with col3: 
        st.container(border = False)
    
    st.container(height=20, border=False)
    
    video_file = open('AirForces.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.container(border=False, height=20)

    col1, col2 = st.columns([1.5,2])
    with col1:
        st.image("AirForcesT1.jpg")

    with col2:
        st.subheader('Características', divider="red")
        st.markdown('*Comodidad*: Excelente amortiguación gracias a la unidad Air en el talón, proporcionando comodidad para uso diario')
        st.markdown("*Talles*: Disponibles en una amplia gama de talles para hombres, mujeres y niños")
        st.markdown('*Colores*: Variedad de :rainbow[colores] y ediciones limitadas, desde el clásico blanco y negro hasta combinaciones de colores vibrantes y colaboraciones con artistas')
        st.markdown('*Uso*: Perfectas para el uso diario, moda urbana y casual')
        st.markdown('*Perfil del Usuario*: Ideal para jóvenes y adultos que buscan un estilo casual y moderno, amantes de la moda urbana y coleccionistas de zapatillas')
    
    st.container(border=False, height=20)


    col1, col2 = st.columns(2)
    with col1:
        st.image("AirForcesT4.jpeg")
    with col2:
        st.image("AirForcesT5.jpeg")

#TABS AIRMAXES
with tabs[1]:
    st.markdown('<h2 class="centered-header">Air Maxes</h2', unsafe_allow_html=True)
    st.markdown('<p class="centered-header">Conocidas por su estilo y comodidad, ideales para el uso diario</p>', unsafe_allow_html=True)
   
    col1, col2, col3= st.columns([1.4,1,1.4])
    with col1:
        st.container(border = False)
    with col2: 
        st.link_button('Comprar este modelo', 'https://www.nike.com.ar/air%20max?_q=air%20max&map=ft', type='primary')
    with col3: 
        st.container(border = False)
    
    st.container(height=20, border=False)
    
    video_file = open('AirMaxes.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.container(border=False, height=20)

    col1, col2 = st.columns([1.5,2])
    with col1:
        st.image("AirMaxesT1.jpg")

    with col2:
        st.subheader('Características', divider="red")
        st.markdown('*Comodidad*: Excelente amortiguación y soporte gracias a la unidad Air Max, ideales para largas caminatas y uso diario')
        st.markdown("*Talles*: Disponibles en talles para toda la familia")
        st.markdown('*Colores*: mplia gama de colores y estilos, desde tonos neutros hasta combinaciones audaces')
        st.markdown('*Uso*: Perfectas para el uso diario, running y actividades físicas ligeras')
        st.markdown('*Perfil del Usuario*: Adecuadas para personas activas que valoran la comodidad y el estilo deportivo, tanto jóvenes como adultos')
    
    st.container(border=False, height=20)

    col1, col2 = st.columns(2)
    with col1:
        st.image("AirMaxesT2.jpeg")
    with col2:
        st.image("AirMaxesT3.png")

#TABS JORDANS
with tabs[2]:
    st.markdown('<h2 class="centered-header">Air Jordans</h2', unsafe_allow_html=True)
    st.markdown('<p class="centered-header">Ícono de estilo y rendimiento, elevando cada paso</p>', unsafe_allow_html=True)
   
    col1, col2, col3= st.columns([1.4,1,1.4])
    with col1:
        st.container(border = False)
    with col2: 
        st.link_button('Comprar este modelo', 'https://www.nike.com.ar/nike/air-jordan-1?map=category-1,icono', type='primary')
    with col3: 
        st.container(border = False)
    
    st.container(height=20, border=False)
    
    video_file = open('Jordans.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.container(border=False, height=20)

    col1, col2 = st.columns([1.5,2])
    with col1:
        st.image("JordansT1.jpg")

    with col2:
        st.subheader('Características', divider="red")
        st.markdown('*Comodidad*: Diseñadas para ofrecer soporte y comodidad durante el juego de baloncesto, con tecnología de amortiguación avanzada')
        st.markdown("*Talles*: Disponibles en talles para hombres, mujeres y niños")
        st.markdown('*Colores*: Diversidad de colores y ediciones limitadas, con combinaciones que suelen contar con la participación del propio Michael Jordan')
        st.markdown('*Uso*: Originalmente para baloncesto, ahora también usadas como zapatillas de moda')
        st.markdown('*Perfil del Usuario*: Apreciadas por jugadores de baloncesto, coleccionistas y aficionados a la moda deportiva')
    
    st.container(border=False, height=20)

    col1, col2 = st.columns(2)
    with col1:
        st.image("JordansT2.jpg")
    with col2:
        st.image("JordansT3.jpg")

#TABS CLEATS
with tabs[3]:
    st.markdown('<h2 class="centered-header">Cleats</h2', unsafe_allow_html=True)
    st.markdown('<p class="centered-header">Diseñados para dominar el campo, combina velocidad y control</p>', unsafe_allow_html=True)
   
    col1, col2, col3= st.columns([1.4,1,1.4])
    with col1:
        st.container(border = False)
    with col2: 
        st.link_button('Comprar este modelo', 'https://www.nike.com.ar/nike/hombre/calzado/botines?map=category-1,category-2,category-3,tipo-de-producto', type='primary')
    with col3: 
        st.container(border = False)
    
    st.container(height=20, border=False)
    
    video_file = open('Cleats.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.container(border=False, height=20)

    col1, col2 = st.columns([1.5,2])
    with col1:
        st.image("CleatsT1.jpg")

    with col2:
        st.subheader('Características', divider="red")
        st.markdown('*Comodidad*: Sujeción firme y diseño anatómico para un ajuste perfecto, con tecnologías que proporcionan estabilidad y comodidad durante el juego')
        st.markdown("*Talles*: Disponibles en talles para hombres, mujeres y niños")
        st.markdown('*Colores*: Variedad de colores adaptados a los equipos y gustos personales')
        st.markdown('*Uso*: Específicas para deportes de campo como fútbol, béisbol y fútbol americano')
        st.markdown('*Perfil del Usuario*: Deportistas que practican deportes de campo y buscan rendimiento, durabilidad y soporte en su calzado')
    
    st.container(border=False, height=20)

    col1, col2 = st.columns(2)
    with col1:
        st.image("CleatsT2.jpg")
    with col2:
        st.image("CleatsT3.jpg")


#TABS DUNKS
with tabs[4]:
    st.markdown('<h2 class="centered-header">Dunks</h2', unsafe_allow_html=True)
    st.markdown('<p class="centered-header">Versatilidad y estilo urbano, redefiniendo cada paso</p>', unsafe_allow_html=True)
   
    col1, col2, col3= st.columns([1.4,1,1.4])
    with col1:
        st.container(border = False)
    with col2: 
        st.link_button('Comprar este modelo', 'https://www.nike.com.ar/nike/hombre/calzado/dunk?map=category-1,category-2,category-3,icono', type='primary')
    with col3: 
        st.container(border = False)
    
    st.container(height=20, border=False)
    
    video_file = open('Dunks.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.container(border=False, height=20)

    col1, col2 = st.columns([1.5,2])
    with col1:
        st.image("DunksT1.jpg")

    with col2:
        st.subheader('Características', divider="red")
        st.markdown('*Comodidad*: Suela acolchada y estructura resistente, diseñada inicialmente para el baloncesto y adaptada para el skateboard')
        st.markdown("*Talles*: Disponibles en una amplia variedad de talles para hombres y mujeres")
        st.markdown('*Colores*: Gama extensa de colores y ediciones especiales, con colaboraciones frecuentes que añaden valor coleccionable')
        st.markdown('*Uso*: Popular en el skateboard, moda urbana y uso casual')
        st.markdown('*Perfil del Usuario*: Skaters, entusiastas de la moda urbana y coleccionistas de zapatillas exclusivas')
    
    st.container(border=False, height=20)

    col1, col2 = st.columns(2)
    with col1:
        st.image("DunksT2.jpeg")
    with col2:
        st.image("DunksT3.jpeg")

