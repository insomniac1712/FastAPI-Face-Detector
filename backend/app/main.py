from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.websocket.stream import router as websocket_router
from app.db.database import Base, engine
from app.db import models
from app.api.routes import router as api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Face Detection API")
app.include_router(api_router)
app.include_router(websocket_router)
app.include_router(api_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(websocket_router)

@app.get("/")
async def root():
    return {"message": "Backend running!"}

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "face-detection-api"
    }