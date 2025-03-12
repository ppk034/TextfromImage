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

   prompt = (
    "Analyze the engineering design of the system (either an engine, electronic system, or machine). "
    "If the system is an engine or mechanical system, describe the following: "
    "1. Full specifications, including engine type, size, and key parameters. "
    "2. Horsepower = (Torque × RPM) / 5252, explain how horsepower influences acceleration and performance. "
    "3. Compression ratio and its impact on power output and fuel efficiency. "
    "4. Volumetric efficiency and its role in engine performance. "
    "5. Fuel consumption rate and any significant modifications made to the engine. "
    "6. Explain thermal efficiency and how it affects the system's fuel usage."
    
    "If the system is an electronic system (e.g., circuit, PCB, sensor), provide the following: "
    "1. Full specifications, including voltage, current, resistance, power requirements, and circuit type. "
    "2. Power consumption calculation based on the system's components and usage (P = V * I). "
    "3. Signal processing: explain how the system handles data or signals, including any modulation or encoding techniques. "
    "4. Efficiency calculations, focusing on energy efficiency and how much power is converted to useful work. "
    "5. Analyze the system's components (transistors, resistors, capacitors) and explain their functionality in the system. "
    "6. Provide the system's overall power efficiency, including any energy-saving components."
    
    "In both cases, provide a detailed breakdown of how the system works, what components are used, and any significant modifications made."
)

try:
    # Generate content based on the customized prompt and image
    response = model.generate_content([prompt, image_part])

    # Display the generated description
    st.write("### Generated Description:")
    st.write(response.text)
except Exception as e:
    st.error(f"An error occurred: {e}")

