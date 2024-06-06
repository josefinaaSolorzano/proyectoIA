from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
#from openai import OpenAI
import pandas as pd

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



st.set_page_config(layout='wide')

st.title('SoleMate')
st.subheader('Encontrá tu par perfecto', divider='red')

video_file = open('NikeComercial.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes, start_time=0)

input_img = st.file_uploader("Ingresá la foto del modelo que buscas y conocé más con un solo click", type=['jpg', 'png', 'jpeg'])

if input_img is not None:
    if st.button("Clasificar"):
        
        col1, col2 = st.columns([1 , 2])

        with col1:
            st.info("Imagen cargada")
            st.image(input_img, use_column_width=True)

        with col2:
            st.info("Resultado")
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

