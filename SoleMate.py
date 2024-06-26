import streamlit as st
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import pydeck as pdk


st.set_page_config(
    page_title="SoleMate",
    page_icon="logoNike.ico",
    layout="wide"
)

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
        background-color: #000000;
    }
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4, 
    [data-testid="stSidebar"] h5, 
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
    [data-testid="stFileUploadDropzone"] div div {
        color: black !important;
    }
    h1, h2, h3, h4, h5, h6, p, .stButton>button {
        color: white !important;
    }
    [data-testid="stFileUploadDropzone"] div div {
        color: black !important;
    }
    [data-testid="stCameraInput"] div div {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def classify_fruit(img):
    np.set_printoptions(suppress=True)
    model = load_model("keras_model.h5", compile=False)
    class_names = open("labels.txt", "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name.strip(), confidence_score

st.title('SoleMate')
st.subheader('Encontrá tu par perfecto', divider='red')

st.container(height=30, border=False)

col1, col2 = st.columns([1, 1])

with col1:
    container = st.container(border=False)
    with container:
        st.image('4KDr.gif', use_column_width=True)

with col2:
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
    st.header("Cómo funciona?")
    st.markdown("Paso 1: Hacé click 'Selecciona una opción' y elegí la metodología que te resulte más conveniente")
    st.markdown("Paso 2: Cargá o sacá una foto del modelo de zapatillas que estas buscando o uno similar")
    st.markdown("Paso 3: Una vez cargada la imagen hacé click en el botón 'Just do it!' y encontrá recomendaciones sobre lo que buscas!")
    st.markdown("Paso 4: Hacé click en el link y descubrí tu SoleMate")

option = st.selectbox("", ["Selecciona una opción", "Cargar imagen", "Tomar foto"])

input_img = None
camera_img = None

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

# Estilos CSS
st.markdown(
    """
    <style>
    .custom-button {
        background-color: #FF6347; /* Color de fondo */
        border: none;
        color: white; /* Color de texto */
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 3px 1px;
        cursor: pointer;
        border-radius: 8px; /* Borde redondeado */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Definir tus recomendaciones y funciones de clasificación aquí
recommendations = {
    "Compra este modelo!": ("Compra este modelo!", "https://www.nike.com.ar/air%20max?_q=air%20max&map=ft"),
    "Our SoleMates": ("Conoce más!", "https://solematearg.streamlit.app/Our_SoleMates"),
    # Agrega más según sea necesario
}

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

                label_description = label.split(maxsplit=1)[1]
                label2 = label_description

                st.success(label2)

                recommendation = recommendations.get(label.strip(), ("No hay recomendación disponible para esta clase.", ""))
                if recommendation[1]:
                    st.markdown(
                        f"""
                        <div style="display: flex; gap: 10px;">
                            <a href="{recommendation[1]}" target="_blank"><button class="custom-button">{recommendation[0]}</button></a>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                    

st.container(height=30, border=False)


video_file = open('NikeComercial.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes, start_time=0)                

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