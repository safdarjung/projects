
import cv2
import pytesseract
import pandas as pd

def table_to_csv(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Dilate the thresholded image to combine adjacent table cells
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    dilated = cv2.dilate(thresh, kernel, iterations=2)

    # Find contours
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each contour and crop the table
    tables = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        table = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Perform OCR on the table
        table_data = pytesseract.image_to_string(table, config='--psm 6')
        tables.append(table_data.split('\n'))

    # Convert tables to a DataFrame and save as CSV file
    df = pd.DataFrame(tables)
    df.to_csv('table_data.csv', index=False)

    # Display the image with bounding boxes
    cv2.imshow('Table Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

table_to_csv('D:\CV_Projects\Image OCR Dataset - Business Quant\image00013.jpg')