from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from text_classifier.models.model import TextClassifier
from text_classifier.schemas.schemas import TextRequest, TextResponse
from text_classifier.utils.utils import setup_logger
import logging
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware


# Set up logging
setup_logger()
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(title="Text Classification API")
# Enable CORS for browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize classifier
classifier = TextClassifier()

# Prediction endpoint
@app.post("/predict", response_model=TextResponse)
def classify_text(request: TextRequest):
    try:
        result = classifier.predict(request.text)
        return TextResponse(label=result['label'], score=result['score'])
    except ValueError as e:
        logger.warning(f"Bad request: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Internal error: {e}")
        raise HTTPException(status_code=500, detail="server error, Try Again!")

# Serve static files (CSS, JS, etc.) if needed
app.mount("/static", StaticFiles(directory="text_classifier/static"), name="static")

# Serve index.html at root "/"
@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join("text_classifier", "static", "index.html"))

# Run the app
def run():
    uvicorn.run("text_classifier.main:app", host="0.0.0.0", port=8080, reload=True)

# Optional: allow running with `python main.py`
if __name__ == "__main__":
    run()
