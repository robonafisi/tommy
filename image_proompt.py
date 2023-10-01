import openai
import os

# Load your API key from an environment variable or secret management service
openai.api_key = 'your_api_key_here'

# Get the path of the image
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'test.jpg')

# Make the request
response = openai.Image.create(
    image=open(image_path, 'rb'),
    prompt='Please tell me about this medication.'
)

# Output the response
print(response)
