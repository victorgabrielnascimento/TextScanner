import cv2
from PIL import Image
import pytesseract
from pyzbar import pyzbar

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

camera = cv2.VideoCapture(0)

while True:
    ret, image = camera.read()
    cv2.imshow('Scanner', image);

    serialNumber = pytesseract.image_to_string(image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break