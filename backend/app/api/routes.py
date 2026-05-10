from fastapi import APIRouter


from app.db.database import SessionLocal
from app.db.models import ROI

router = APIRouter()

@router.get("/api/roi")
async def get_roi_data():

    db = SessionLocal()

    try:

        rois = (
            db.query(ROI)
            .order_by(ROI.created_at.desc())
            .limit(20)
            .all()
        )

        response = []

        for roi in rois:

            response.append({
                "id": roi.id,
                "x": roi.x,
                "y": roi.y,
                "width": roi.width,
                "height": roi.height,
                "created_at": roi.created_at.isoformat()
            })

        return response

    finally:
        db.close()