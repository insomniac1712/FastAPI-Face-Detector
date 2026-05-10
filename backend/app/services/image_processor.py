from PIL import ImageDraw


def draw_roi(image, roi):
    """
    Draw rectangle around detected face
    """

    draw = ImageDraw.Draw(image)

    x = roi["x"]
    y = roi["y"]
    width = roi["width"]
    height = roi["height"]

    draw.rectangle(
        [
            (x, y),
            (x + width, y + height)
        ],
        outline="red",
        width=4
    )

    return image