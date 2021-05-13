import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# imports pandas library

# Google Credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\acer\Desktop\Divyesh\Projects\college_projects\cyber_bully_website\booming-coast-313509-bb494bed1251.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath(r'C:\Users\acer\Desktop\Divyesh\Projects\college_projects\cyber_bully_website\sampleImage.png')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations
texts = response.text_annotations

print('Labels:')
for label in labels:
    print(label.description)
    # df-pd.DataFrame(columns = ['Locale', description])
for text in texts:
    print(text)
# for text in texts: