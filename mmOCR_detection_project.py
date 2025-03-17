from paddleocr import PaddleOCR, draw_ocr
import cv2
from PIL import Image

# Initialize the PaddleOCR model
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Path to your image
image_path = 'D:/CV_Projects/OCR_Apple_detection/apple_text_images/fffffffffffffffff.jpg'

# Run the OCR model on the image
result = ocr.ocr(image_path, cls=True)

# Extract recognized text and their bounding boxes
detected_texts = [line[1][0] for line in result[0]]
detected_boxes = [line[0] for line in result[0]]

# Filter results to find the word "apple"
detected_apples = [text for text in detected_texts if 'apple' in text.lower()]

print("Detected 'apple' variations:", detected_apples)

# Visualize the results
image = Image.open(image_path).convert('RGB')
boxes = [box for text, box in zip(detected_texts, detected_boxes) if 'apple' in text.lower()]
for box in boxes:
    draw_img = draw_ocr(image, boxes, detected_apples, font_path='path_to_font.ttf')

# Save the result image with detected words
result_image_path = 'result_image.png'
draw_img.save(result_image_path)
print(f"Result image saved to {result_image_path}")




