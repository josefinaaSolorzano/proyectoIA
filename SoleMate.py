from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(
    page_title="SoleMate",
    page_icon="logoNike.ico",  # Asegúrate de que la ruta al archivo de imagen sea correcta
    layout="wide"
)

# Estilo CSS personalizado para el fondo negro y texto blanco
st.markdown(
    """
    <style>
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

def classify_fruit(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Convert the image to RGB
    image = img.convert("RGB")

    # Resize the image to 224x224 and crop from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Return class name and confidence score
    return class_name.strip(), confidence_score

st.title('SoleMate')
st.subheader('Encontrá tu par perfecto', divider='red')

st.container(height=30, border=False)

col1, col2 = st.columns([1,1])

with col1:
    container = st.container(border=False)
    with container:
        st.image('4KDr.gif', use_column_width=True)

with col2:
    # Contenedor para el texto centrado
    container = st.container(border=False)
    with container:
        st.markdown(
            """
            <div style="text-align: center;">
                <h2>¿Qué es SoleMate?</h2>
                <p>Somos una app que te permite encontrar tu par ideal de la manera más rápida y fácil posible.<p>
                <p>Junto con Nike, diseñamos una app que te permite conocer sus modelos de una manera nunca antes vista. ¿Qué esperas para encontrar tu <i>SoleMate</i>?</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.container(height=30, border=False)

container = st.container(border=True)
with container:
    st.header("¿Cómo funciona?")
    st.markdown("**Paso 1:** Hacé click en 'Selecciona una opción' y elegí la metodología que te resulte más conveniente")
    st.markdown("**Paso 2:** Cargá o sacá una foto del modelo de zapatillas que estas buscando o uno similar")
    st.markdown("**Paso 3:** Una vez cargada la imagen hacé click en el botón 'Just do it!' y dejanos encontrar tu par ideal")
    st.markdown("**Paso 4:** Para comprar hacé click en el botón de 'Compra este modelo'. Para conocer más hacé click en Our SoleMates en la barra izquierda de la página")

# Opción para elegir entre cargar una imagen o tomar una foto
option = st.selectbox("", ["Selecciona una opción", "Cargar imagen", "Tomar foto"])

# Variables para almacenar la imagen
input_img = None
camera_img = None

# Dependiendo de la elección del usuario, mostrar la opción correspondiente
if option == "Cargar imagen":
    input_img = st.file_uploader("Sube una imagen", type=['jpg', 'png', 'jpeg'])
elif option == "Tomar foto":
    camera_img = st.camera_input("Toma una foto")

recommendations = {
    "0 Air Forces": ('Comprar este modelo', 'https://www.nike.com.ar/air%201%20force?_q=air%201%20force&map=ft'),
    "1 Air Jordans": ('Comprar este modelo', 'https://www.nike.com.ar/nike/air-jordan-1?map=category-1,icono'),
    "2 Air Maxes": ('Comprar este modelo', 'https://www.nike.com.ar/air%20max?_q=air%20max&map=ft'),
    "3 Cleats": ('Comprar este modelo', 'https://www.nike.com.ar/nike/hombre/calzado/botines?map=category-1,category-2,category-3,tipo-de-producto'),
    "4 Dunks": ('Comprar este modelo', 'https://www.nike.com.ar/nike/hombre/calzado/dunk?map=category-1,category-2,category-3,icono')
}


# Determinar cuál imagen usar
img_to_process = input_img or camera_img

if img_to_process is not None:
    if st.button('Just do it!'):
        st.toast('Just do it!', icon='👟')
        
        col1, col2 = st.columns([1 , 2])

        with col1:
            st.info("Imagen cargada")
            st.image(img_to_process, use_column_width=True)

        with col2:
            st.info("Tu par ideal es...")
            image_file = Image.open(img_to_process)

            with st.spinner('Analizando imagen...'):
                label, confidence_score = classify_fruit(image_file)

                # Extraer el nombre de la etiqueta sin el número
                label_description = label.split(maxsplit=1)[1]  # Divide la etiqueta por el primer espacio y toma el segundo elemento
                label2 = label_description  # Guarda la descripción en label2

                st.success(label2)  # Muestra la etiqueta sin el número

                # Mostrar recomendación basada en la clase
                recommendation = recommendations.get(label.strip(), "No hay recomendación disponible para esta clase.")
                if recommendation:
                    st.markdown(f'<a href="{recommendation[1]}" target="_blank"><button class= "styled-button">{recommendation[0]}</button></a>  <p> Hacé click en Our SoleMates y conocé más sobre este modelo! <p>', unsafe_allow_html=True)

                    
# Estilos CSS
st.markdown(
    """
    <style>
    .styled-button {
        background-color: #FF6347; /* Color de fondo */
        border: none;
        color: white; /* Color de texto */
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px; /* Borde redondeado */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Botón HTML con clase CSS
#st.markdown('<button class="styled-button">Botón Estilizado</button>', unsafe_allow_html=True)
st.container(height=30, border=False)

video_file = open('NikeComercial.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)     

# Título de la aplicación
st.title('Mapa de Tiendas Nike en Argentina')

# Crear DataFrame de ejemplo (reemplazar con tus datos reales)
data = {
    'Nombre': ['NSO Abasto', 'NSO Alto Palermo', 'Factory Arcos', 'Factory Barracas', 'Factory Chacarita', 'Factory Rivadavia', 'Nike Avenida Santa Fe', 'NSO Unicenter', 'NSO Alto Avellaneda', 'Factory La Plata', 'Factory Soleil', 'Nike Alto Rosario', 'Nike Rosario', 'Nike Maxi Mendoza', 'Nike Tucumán', 'Nike Nuevocentro'],
    'Dirección': ['Avenida Corrientes 3247, CABA', 'Arenales 3360, CABA', 'Paraguay 4979, CABA', 'California 2098, CABA', 'Avenida Corrientes 6433, CABA', 'Avenida Rivadavia 8961, CABA', 'Avenida Santa Fe 1681, CABA', 'Paraná 3745, Martínez', 'Gral. Güemes 897, Crucecita', 'Camino Parque Centenario y Calle 507, La Plata', 'Bernardo de Irigoyen 2647, San Isidro', 'Junín 501, Rosario', 'Córdoba 1260, Rosario', 'Avenida San Martin 1468, Mendoza', 'Mendoza 562, San Miguel de Tucumán', 'Duarte Quiros 1400, Córdoba'],
    'Provincia': ['Buenos Aires', 'Buenos Aires', 'Buenos Aires', 'Buenos Aires', 'Buenos Aires', 'Buenos Aires', 'Buenos Aires', 'Buenos Aires', 'Buenos Aires', 'Buenos Aires', 'Buenos Aires', 'Santa Fe', 'Santa Fe', 'Mendoza', 'Tucumán', 'Córdoba'],
    'Latitud': [-34.6037, -34.5882, -34.5803, -34.6471, -34.5933, -34.6355, -34.5955, -34.5081, -34.6767, -34.8841, -34.4909, -32.9274, -32.9457, -32.8866, -26.8280, -31.4119],
    'Longitud': [-58.4103, -58.4098, -58.4272, -58.3773, -58.4496, -58.4903, -58.3914, -58.5266, -58.3665, -58.0039, -58.5903, -60.6694, -60.6402, -68.8390, -65.2050, -64.2053]
}
df = pd.DataFrame(data)

# Convertir latitud y longitud a flotantes
df['Latitud'] = df['Latitud'].astype(float)
df['Longitud'] = df['Longitud'].astype(float)

# Agregar un filtro de provincia
provincias = df['Provincia'].unique().tolist()
provincia_seleccionada = st.selectbox('Selecciona una provincia', provincias)

# Filtrar el DataFrame según la provincia seleccionada
df_filtrado = df[df['Provincia'] == provincia_seleccionada]


# Configuración del mapa
view_state = pdk.ViewState(latitude=df_filtrado['Latitud'].iloc[0], longitude=df_filtrado['Longitud'].iloc[0], zoom=10, bearing=0, pitch=0)

# Crear capa de marcadores
layer = pdk.Layer(
    'ScatterplotLayer',
    data=df_filtrado,
    get_position='[Longitud, Latitud]',
    get_radius=100,
    get_fill_color=[255, 0, 0],
    pickable=True,
    auto_highlight=True
)

# Renderizar el mapa
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "html": "<b>Nombre:</b> {Nombre} <br> <b>Dirección:</b> {Dirección} <br> <b>Provincia:</b> {Provincia}",
        "style": {
            "color": "white"
        }
    }
)

# Mostrar el mapa
st.pydeck_chart(r)

#Mostrar listado de tiendas a la izquierda del mapa
st.header('Tiendas de Nike en la provincia seleccionada:')

# Mostrar el listado de tiendas como contenedores
for index, row in df_filtrado.iterrows():
    st.markdown(f"{row['Nombre']}")
    st.write(f"Dirección: {row['Dirección']}")
    st.write("---")  # Agregar una línea divisoria entre cada tienda


with st.sidebar:
    st.container(height=20, border=False)

st.sidebar.subheader('Regístrate para recibir ofertas exclusivas')
email = st.sidebar.text_input('Correo electrónico')
if st.sidebar.button('Registrarse'):
    # Guardar el correo electrónico en una base de datos o enviar a una lista de correo
    st.sidebar.success('¡Gracias por registrarte!')