from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
from openai import OpenAI
import pandas as pd

import os
import streamlit as st

try:
    import openpyxl
except ImportError:
    st.error("Falta la dependencia 'openpyxl'. Ejecuta 'pip install openpyxl' para instalarla.")

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# List all files in the directory containing the script
directory_files = os.listdir(script_dir)
st.text("Files in directory: " + ", ".join(directory_files))

def classify_fruit(img):

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model_path = os.path.join(script_dir, "keras_model.h5")
    model = load_model(model_path, compile=False)

    # Load the labels
    labels_path = os.path.join(script_dir, "labels.txt")
    class_names = open(labels_path, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = img.convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
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

    # Print prediction and confidence score
    # print("Class:", class_name[2:], end="")
    # print("Confidence Score:", confidence_score)

    return class_name, confidence_score

#def generate_recipe(label):
    client = OpenAI(api_key="")

    response = client.Completion.create(
        model="gpt-3.5-turbo-instruct",
        temperature=0.5,
        prompt= f"Sos un asistente experto en modelos de zapatillas Nike Air Forces, Air Jordans, Air Maxes, Cleats y Dunks. A partir del modelo {label} necesito que generes una breve descripcion del producto y sus principales caracteristicas: comodidad, talles, colores, para que se utiliza y perfil del usuario que compraria este producto.",
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text


st.set_page_config(layout='wide')


st.title('SoleMate')
st.subheader('Encontrá tu par perfecto', divider='red')

video_file = open('NikeComercial.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes, start_time=0)

input_img = st.file_uploader("Ingresá la foto del modelo que buscas y conocé más con un solo click", type=['jpg', 'png', 'jpeg'])

#def classify_fruit(image_file):
    # Aquí deberías agregar la lógica para clasificar la imagen
    # Por ahora, simplemente devolvemos un valor de prueba
   # return "0 Air Forces", 0.85

#if input_img is not None:
   # if st.button("Classify"):
    #    col1, col2, col3 = st.columns([1, 1, 1])

     #   with col1:
      #      st.info("Your uploaded Image")
       #     st.image(input_img, use_column_width=True)

        #with col2:
         #   st.info("Your Result")
          #  image_file = Image.open(input_img)
           # label, confidence_score = classify_fruit(image_file)
           # if label == "0 Air Forces":
            #    st.success("Tu par perfecto es Air Forces.")
            #elif label == "1 Air Jordans":
             #   st.success("Tu par perfecto es Air Jordans.")
            #elif label == "2 Air Maxes":
             #   st.success("Tu par perfecto es Air Maxes.")
            #elif label == "3 Cleats":
             #   st.success("Tu par perfecto es Cleats.")
            #elif label == "4 Dunks":
             #   st.success("Tu par perfecto es Dunks.")
            #else:
             #   st.error("No encontramos ningún match para vos 😢 Cargá otra foto para que encontremos tu par ideal! .")

        #with col3:
         #   st.info("Recommendations")
          #  if label in ["0 Air Forces", "1 Air Jordans", "2 Air Maxes", "3 Cleats", "4 Dunks"]:
           #     st.write(f"Modelo identificado: {label}")
            #    st.write(f"Confianza: {confidence_score * 100:.2f}%")
             #   st.write("Recomendaciones de compra:")
              #  st.write("- Producto 1")
               # st.write("- Producto 2")
                #st.write("- Producto 3")

if input_img is not None:
    if st.button("Classify"):
        
        col1, col2, col3 = st.columns([1,1,1])

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

            
        