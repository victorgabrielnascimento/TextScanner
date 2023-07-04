import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    cv2.imshow('Scanner', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    preprocessed_image = cv2.medianBlur(gray, 3)
    text = pytesseract.image_to_string(preprocessed_image)
    print("Texto detectado: ", text)

camera.release()
cv2.destroyAllWindows()
