from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
import io
import numpy as np

# Initialize FastAPI
app = FastAPI(
    title="YOLO Model API",
    description="API to perform inference using a pretrained YOLO model",
    version="1.0.0"
)

# Load YOLO model
model = YOLO("obj-det-weighted.pt")  # Replace with your actual .pt file path

@app.get("/")
async def root():
    return {"message": "Welcome to the YOLO Model API!"}

@app.post("/predict/")
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
