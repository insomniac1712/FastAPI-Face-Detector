from PIL import Image
import mediapipe as mp
import numpy as np


class FaceDetector:

    def __init__(self):

        self.face_detection = mp.tasks.vision.FaceDetector.create_from_options(
            mp.tasks.vision.FaceDetectorOptions(
                base_options=mp.tasks.BaseOptions(
                    model_asset_path="models/blaze_face_short_range.tflite"
                ),
                running_mode=mp.tasks.vision.RunningMode.IMAGE
            )
        )

    def detect_face(self, image: Image.Image):

        image_np = np.array(image)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=image_np
        )

        detection_result = self.face_detection.detect(mp_image)

        if not detection_result.detections:
            return None

        bbox = detection_result.detections[0].bounding_box

        return {
            "x": int(bbox.origin_x),
            "y": int(bbox.origin_y),
            "width": int(bbox.width),
            "height": int(bbox.height)
        }