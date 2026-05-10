import time
from fastapi import APIRouter, WebSocket

from app.services.face_detector import FaceDetector
from app.services.image_processor import draw_roi
from app.utils.encoder import (
    decode_base64_image,
    encode_image_to_base64
)
from app.services.roi_service import save_roi

router = APIRouter()

face_detector = FaceDetector()

last_save_time = 0

@router.websocket("/ws/video")
async def video_stream(websocket: WebSocket):
    await websocket.accept()
    global last_save_time

    try:
        while True:
            data = await websocket.receive_text()
            image = decode_base64_image(data)

            # Skip invalid frames
            if image is None:
                continue

            roi = face_detector.detect_face(image)

            if roi:
                current_time = time.time()
                if current_time - last_save_time > 1:
                    save_roi(roi)
                    last_save_time = current_time
  

            processed_frame = encode_image_to_base64(image)

            await websocket.send_text(processed_frame)


    except Exception as e:
        print("WebSocket Error:", e)
        await websocket.close()