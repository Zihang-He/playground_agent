from dotenv import load_dotenv
import base64
import os
from openai import OpenAI
load_dotenv()
client = OpenAI()
# Load environment variables from a .env file

# Ensure OPENAI_API_KEY is set
client.api_key = os.getenv("OPENAI_API_KEY")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_local = './input_files/math_equations.jpeg'
image_data = encode_image(image_local)
# gpt4-turbo
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are an OCR assistant."},
        {"role": "user", "content": [
            {"type": "text", "text": "Extract the text from this image."},
            {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
            },
        ]}
    ]
)

print(response.choices[0])