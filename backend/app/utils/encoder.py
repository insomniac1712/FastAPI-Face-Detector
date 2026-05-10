import base64
import binascii
import io
from typing import Optional

from PIL import Image, UnidentifiedImageError

def decode_base64_image(data: str) -> Optional[Image.Image]:
    """
    Decode base64 string to PIL Image
    """

    try:
        if "," not in data:
            return None
        
        encoded_data = data.split(",")[1]

        image_data = base64.b64decode(encoded_data)

        image = Image.open(io.BytesIO(image_data))

        image = image.convert("RGB")

        return image
    
    except (UnidentifiedImageError, ValueError, IndexError, binascii.Error):
        return None

def encode_image_to_base64(image: Image.Image) -> str:
    """
    Encode PIL Image to base64 string
    """
    buffer = io.BytesIO()

    image.save(buffer, format="JPEG")

    encoded_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return f"data:image/jpeg;base64,{encoded_data}"