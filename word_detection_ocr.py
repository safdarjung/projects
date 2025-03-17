from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
from PIL import Image

def preprocess_image(image_path):
    # Open the image file
    image = Image.open(image_path).convert("RGB")
    return image

def detect_and_recognize_text(image_path):
    # Load the model and processor
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')

    # Preprocess the image
    image = preprocess_image(image_path)

    # Prepare the image for the model
    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    # Generate text from the image
    with torch.no_grad():
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_text

# Path to your image
image_path = 'D:/CV_Projects/OCR_Apple_detection/apple_text_images/WhatsApp Image 2024-06-01 at 10.30.51_20ca0319.jpg'

# Detect and recognize text
recognized_text = detect_and_recognize_text(image_path)

# Check if the recognized text contains the word "apple"
if "apple" in recognized_text.lower():
    print("Detected 'apple':", recognized_text)
else:
    print("The word 'apple' was not detected.")
