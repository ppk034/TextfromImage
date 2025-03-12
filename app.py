import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from PIL import Image
import io

# Initialize Vertex AI
vertexai.init(project="mytextgeneratorapp", location="us-central1")

# Set up the model
model = GenerativeModel("gemini-pro-vision")

# Streamlit App
st.title("General description")
st.write("Upload an image of an engine or electronic system, and the app will generate its specifications, calculations, and descriptions.")

# Upload Image
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
    st.write("")

    # Prepare the image for the model
    image = uploaded_image.read()

    # Convert the image data to the correct format for model processing
    image_part = Part.from_data(data=image, mime_type="image/jpeg")

    prompt = ("Explain image in detailed description")


try:
    # Generate content based on the customized prompt and image
    response = model.generate_content([prompt, image_part])

    # Display the generated description
    st.write("### Generated Description:")
    st.write(response.text)
except Exception as e:
    st.error(f"An error occurred: {e}")

