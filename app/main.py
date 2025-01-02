from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io
import numpy as np

# Initialize FastAPI
app = FastAPI(
    title="YOLO Model API",
    description="API to perform inference using a pretrained YOLO model. Use the `/predict/` endpoint to upload an image and get predictions.",
    version="1.0.0"
)

# Add CORS middleware for broader access, if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load YOLO model
model = YOLO("app/obj-det-weighted.pt")  # Ensure the model path is correct

@app.get("/")
async def root():
    return {"message": "Welcome to the YOLO Model API! Visit `/docs` for SwaggerUI."}

@app.post("/predict/", summary="Predict using YOLO model", description="Upload an image file to perform object detection.")
async def predict(file: UploadFile = File(...)):
    """
    Upload an image for YOLO model prediction.
    """
    try:
        # Read the uploaded image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # Convert image to numpy for YOLO inference
        np_image = np.array(image)

        # Perform inference
        results = model.predict(np_image)

        # Parse results
        predictions = []
        for result in results:
            for box in result.boxes:
                predictions.append({
                    "class": model.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "bbox": [float(coord) for coord in box.xyxy[0].tolist()]
                })

        return JSONResponse(content={"predictions": predictions})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
