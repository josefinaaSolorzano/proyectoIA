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
        **Comodidad**: Excelente amortiguación gracias a la unidad Air en el talón, proporcionando comodidad para uso diario.
        **Talles**: Disponibles en una amplia gama de talles para hombres, mujeres y niños.
        **Colores**: Variedad de colores y ediciones limitadas, desde el clásico blanco y negro hasta combinaciones de colores vibrantes y colaboraciones con artistas.
        **Uso**: Perfectas para el uso diario, moda urbana y casual.
        **Perfil del Usuario**: Ideal para jóvenes y adultos que buscan un estilo casual y moderno, amantes de la moda urbana y coleccionistas de zapatillas.
    """,
    "1 Air Jordans": """
        **Comodidad**: Diseñadas para ofrecer soporte y comodidad durante el juego de baloncesto, con tecnología de amortiguación avanzada.
        **Talles**: Disponibles en talles para hombres, mujeres y niños.
        **Colores**: Diversidad de colores y ediciones limitadas, con combinaciones que suelen contar con la participación del propio Michael Jordan.
        **Uso**: Originalmente para baloncesto, ahora también usadas como zapatillas de moda.
        **Perfil del Usuario**: Apreciadas por jugadores de baloncesto, coleccionistas y aficionados a la moda deportiva.
    """,
    "2 Air Maxes": """
        **Comodidad**: Excelente amortiguación y soporte gracias a la unidad Air Max, ideales para largas caminatas y uso diario.
        **Talles**: Disponibles en talles para toda la familia.
        **Colores**: Amplia gama de colores y estilos, desde tonos neutros hasta combinaciones audaces.
        **Uso**: Perfectas para el uso diario, running y actividades físicas ligeras.
        **Perfil del Usuario**: Adecuadas para personas activas que valoran la comodidad y el estilo deportivo, tanto jóvenes como adultos.
    """,
    "3 Cleats": """
        **Comodidad**: Sujeción firme y diseño anatómico para un ajuste perfecto, con tecnologías que proporcionan estabilidad y comodidad durante el juego.
        **Talles**: Disponibles en talles para hombres, mujeres y niños.
        **Colores**: Variedad de colores adaptados a los equipos y gustos personales.
        **Uso**: Específicas para deportes de campo como fútbol, béisbol y fútbol americano.
        **Perfil del Usuario**: Deportistas que practican deportes de campo y buscan rendimiento, durabilidad y soporte en su calzado.
    """,
    "4 Dunks": """
        **Comodidad**: Suela acolchada y estructura resistente, diseñada inicialmente para el baloncesto y adaptada para el skateboard.
        **Talles**: Disponibles en una amplia variedad de talles para hombres y mujeres.
        **Colores**: Gama extensa de colores y ediciones especiales, con colaboraciones frecuentes que añaden valor coleccionable.
        **Uso**: Popular en el skateboard, moda urbana y uso casual.
        **Perfil del Usuario**: Skaters, entusiastas de la moda urbana y coleccionistas de zapatillas exclusivas.
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
    st.write("Somos una app que te permite encontrar tu par ideal de la manera mas rapida y facil posible. Junto con Nike, diseñamos una app que te permite conocer sus modelos de una manera nunca antes vista. Que esperas para encontrar tu **SoleMate**")


st.container(height=30, border=False)

st.header("Cómo funciona?")

input_img = st.file_uploader("Ingresá la foto del modelo que buscas y conocé más con un solo click", type=['jpg', 'png', 'jpeg'])

if input_img is not None:
    if st.button('Clasificar'):
     st.toast('Just do it!', icon='👟')
        
    col1, col2 = st.columns([1 , 2])

    with col1:
            st.info("Imagen cargada")
            st.image(input_img, use_column_width=True)

    with col2:
            st.info("Tu par ideal es...")
            image_file = Image.open(input_img)

            with st.spinner('Analizando imagen...'):
                label, confidence_score = classify_fruit(image_file)

                # Extraer el nombre de la etiqueta sin el número
                label_description = label.split(maxsplit=1)[1]  # Divide la etiqueta por el primer espacio y toma el segundo elemento
                label2 = label_description  # Guarda la descripción en label2

                st.success(label2)  # Muestra la etiqueta sin el número

                # Mostrar recomendación basada en la clase
                recommendation = recommendations.get(label.strip(), "No hay recomendación disponible para esta clase.")
                st.write(recommendation)
                st.page_link("pages\Our_SoleMates.py", label="Page 1", icon="1️⃣")



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
    st.markdown(f"*{row['Nombre']}*")
    st.write(f"Dirección: {row['Dirección']}")
    st.write("---")  # Agregar una línea divisoria entre cada tienda


with st.sidebar:
    st.container(height=20, border=False)

st.sidebar.subheader('Regístrate para recibir ofertas exclusivas')
email = st.sidebar.text_input('Correo electrónico')
if st.sidebar.button('Registrarse'):
    # Guardar el correo electrónico en una base de datos o enviar a una lista de correo
    st.sidebar.success('¡Gracias por registrarte!')


