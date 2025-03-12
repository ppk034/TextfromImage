from google.cloud import aiplatform

# Initialize Vertex AI with project details
aiplatform.init()

# Get and print the active project
project_id = aiplatform.initializer.global_config.project
print(f"Authenticated successfully with project: {project_id}")
