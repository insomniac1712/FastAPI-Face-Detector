from app.db.database import SessionLocal
from app.db.models import ROI


def save_roi(roi_data):

    db = SessionLocal()
    try:

        roi = ROI(
            x=roi_data["x"],
            y=roi_data["y"],
            width=roi_data["width"],
            height=roi_data["height"]
        )

        db.add(roi)

        db.commit()

    finally:
        db.close()