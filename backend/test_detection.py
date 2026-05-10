from PIL import Image

from app.services.face_detector import FaceDetector
from app.services.image_processor import draw_roi

detector = FaceDetector()

image = Image.open("test.jpg")

roi = detector.detect_face(image)

print("ROI:", roi)

if roi:
    image = draw_roi(image, roi)
    image.save("output.jpg")