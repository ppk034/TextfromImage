import vertexai
from vertexai.generative_models import GenerativeModel, Part

vertexai.init(project="mytextgeneratorapp", location="us-central1")

model = GenerativeModel("gemini-pro-vision")

image_path = "C:\\Users\\Prave\\OneDrive\\Documents\\MLOps\\Vertex_AI_Image_generator\\2004-ford-mustang-8.jpg" #Updated Image path

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



with open(image_path, "rb") as f:
    image_data = f.read()

image = Part.from_data(data=image_data, mime_type="image/jpeg") #ensure correct mime type.

response = model.generate_content([prompt, image])

print(response.text)