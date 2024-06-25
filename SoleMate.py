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

# Dictionary of recommendations for each class
recommendations = {
    "0 Air Forces": """
        *Comodidad*: Excelente amortiguación gracias a la unidad Air en el talón, proporcionando comodidad para uso diario.\n
        *Talles*: Disponibles en una amplia gama de talles para hombres, mujeres y niños.\n
        *Colores*: Variedad de colores y ediciones limitadas, desde el clásico blanco y negro hasta combinaciones de colores vibrantes y colaboraciones con artistas.\n
        *Uso*: Perfectas para el uso diario, moda urbana y casual.\n
        *Perfil del Usuario*: Ideal para jóvenes y adultos que buscan un estilo casual y moderno, amantes de la moda urbana y coleccionistas de zapatillas.
    """,
    "1 Air Jordans": """
        *Comodidad*: Diseñadas para ofrecer soporte y comodidad durante el juego de baloncesto, con tecnología de amortiguación avanzada.\n
        *Talles*: Disponibles en talles para hombres, mujeres y niños.\n
        *Colores*: Diversidad de colores y ediciones limitadas, con combinaciones que suelen contar con la participación del propio Michael Jordan.\n
        *Uso*: Originalmente para baloncesto, ahora también usadas como zapatillas de moda.\n
        *Perfil del Usuario*: Apreciadas por jugadores de baloncesto, coleccionistas y aficionados a la moda deportiva.
    """,
    "2 Air Maxes": """
        *Comodidad*: Excelente amortiguación y soporte gracias a la unidad Air Max, ideales para largas caminatas y uso diario.\n
        *Talles*: Disponibles en talles para toda la familia.\n
        *Colores*: Amplia gama de colores y estilos, desde tonos neutros hasta combinaciones audaces.\n
        *Uso*: Perfectas para el uso diario, running y actividades físicas ligeras.\n
        *Perfil del Usuario*: Adecuadas para personas activas que valoran la comodidad y el estilo deportivo, tanto jóvenes como adultos.
    """,
    "3 Cleats": """
        *Comodidad*: Sujeción firme y diseño anatómico para un ajuste perfecto, con tecnologías que proporcionan estabilidad y comodidad durante el juego.\n
        *Talles*: Disponibles en talles para hombres, mujeres y niños.\n
        *Colores*: Variedad de colores adaptados a los equipos y gustos personales.\n
        *Uso*: Específicas para deportes de campo como fútbol, béisbol y fútbol americano.\n
        *Perfil del Usuario*: Deportistas que practican deportes de campo y buscan rendimiento, durabilidad y soporte en su calzado.
    """,
    "4 Dunks": """
        *Comodidad*: Suela acolchada y estructura resistente, diseñada inicialmente para el baloncesto y adaptada para el skateboard.\n
        *Talles*: Disponibles en una amplia variedad de talles para hombres y mujeres.\n
        *Colores*: Gama extensa de colores y ediciones especiales, con colaboraciones frecuentes que añaden valor coleccionable.\n
        *Uso*: Popular en el skateboard, moda urbana y uso casual.\n
        *Perfil del Usuario*: Skaters, entusiastas de la moda urbana y coleccionistas de zapatillas exclusivas.
    """,
}


st.title('SoleMate')
st.subheader('Encontrá tu par perfecto', divider='red')

st.container(height=30, border=False)

container = st.container(border=True)
col1, col2 = st.columns([1,1])
with col1:
    st.image('4KDr.gif', use_column_width=True)

with col2:
    st.header("¿Qué es SoleMate?")
    st.write("Somos una app que te permite encontrar tu par ideal de la manera más rápida y fácil posible. Junto con Nike, diseñamos una app que te permite conocer sus modelos de una manera nunca antes vista. ¿Qué esperas para encontrar tu *SoleMate*?")

st.container(height=30, border=False)

st.header("Cómo funciona?")

# Opción para cargar una imagen desde el dispositivo
input_img = st.file_uploader("Ingresá la foto del modelo que buscas y conocé más con un solo click", type=['jpg', 'png', 'jpeg'])

# Opción para tomar una foto con la cámara
camera_img = st.camera_input("O tomá una foto del modelo")

# Determinar cuál imagen usar
img_to_process = input_img or camera_img

if img_to_process is not None:
    if st.button('Clasificar'):
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
                st.markdown(recommendation)
                st.page_link('pages/Our_SoleMates.py', label = "Our SoleMates")

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
    'Latitud': [-34.603722, -34.588058, -34.583733, -34.636210, -34.583088, -34.630779, -34.595356, -34.501840, -34.670908, -34.904680, -34.498480, -32.956634, -32.942847, -32.889731, -26.824142, -31.417339],
    'Longitud': [-58.410904, -58.410526, -58.431961, -58.381592, -58.467369, -58.506790, -58.389870, -58.520485, -58.366353, -57.939468, -58.681000, -60.648104, -60.641346, -68.844390, -65.203178, -64.189274]
}

df = pd.DataFrame(data)

# Crear la visualización de mapa
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=-34.603722,
        longitude=-58.381592,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'ScatterplotLayer',
           data=df,
           get_position='[Longitud, Latitud]',
           get_color='[200, 30, 0, 160]',
           get_radius=200,
        ),
    ],
))

st.dataframe(df)