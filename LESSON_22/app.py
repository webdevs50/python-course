## Machine Learning - Computer Vision

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

endpoint = "https://<your-endpoint>.cognitiveservices.azure.com/"
key = "<your-key>"

client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

# Example: analyze an image and getting the image description
image_url = "https://example.com/yourimage.jpg"
description = client.describe_image(image_url)
print("Description:", description.captions[0].text)


## Machine Learning - Azure OpenAI 
## Configuration for each language varies slightly, but both require the same parameters to be set. The necessary parameters are endpoint, key, and deployment name.
## Add the library to your app, and set the required parameters for your client.

# Add OpenAI library
from openai import AzureOpenAI

deployment_name = '<YOUR_DEPLOYMENT_NAME>' 

# Initialize the Azure OpenAI client
client = AzureOpenAI(
        azure_endpoint = '<YOUR_ENDPOINT_NAME>', 
        api_key='<YOUR_API_KEY>',  
        api_version="20xx-xx-xx" #  Target version of the API, such as 2024-02-15-preview
        )

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"}
    ]
)
generated_text = response.choices[0].message.content

# Print the response
print("Response: " + generated_text + "\n")