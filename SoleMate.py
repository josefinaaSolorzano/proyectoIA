from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
#from openai import OpenAI
import pandas as pd
import requests
from bs4 import BeautifulSoup


def classify_fruit(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = img.convert("RGB")

    # Resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predict the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

    return class_name, confidence_score

def recommend_product(label):
    # Define a mapping from labels to search queries for the Nike website
    search_queries = {
        "Air Force 1": "air-force-1",
        "Air Jordan": "jordan",
        "Air Max": "air-max",
        "Cleats": "soccer-cleats",
        "Dunks": "dunk"
    }

    for key in search_queries:
        if key in label:
            query = search_queries[key]
            break
    else:
        query = "sneakers"

    url = f"https://www.nike.com/w?q={query}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first product
    product = soup.find('div', {'data-qa': 'product-card'})
    if product:
        product_name = product.find('div', {'data-qa': 'product-name'}).text
        product_price = product.find('div', {'data-qa': 'product-price'}).text
        product_link = product.find('a', {'data-qa': 'product-link'})['href']

        return {
            'name': product_name,
            'price': product_price,
            'link': f"https://www.nike.com{product_link}"
        }
    else:
        return None

st.set_page_config(layout='wide')

st.title('SoleMate')
st.subheader('Encontrá tu par perfecto', divider='red')

video_file = open('NikeComercial.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes, start_time=0)

input_img = st.file_uploader("Ingresá la foto del modelo que buscas y conocé más con un solo click", type=['jpg', 'png', 'jpeg'])

if input_img is not None:
    if st.button("Clasificar"):
        col1, col2, col3 = st.columns([1, 1, 1])

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

                # Recomendar un producto similar en Nike
                product = recommend_product(label2)
                if product:
                    st.markdown(f"**{product['name']}**")
                    st.markdown(f"Precio: {product['price']}")
                    st.markdown(f"[Visita el producto en Nike]({product['link']})")
                else:
                    st.warning("No se encontraron productos similares en Nike.")