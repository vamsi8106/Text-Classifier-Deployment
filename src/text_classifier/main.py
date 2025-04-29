from fastapi import FastAPI, HTTPException
from text_classifier.models.model import TextClassifier
from text_classifier.schemas.schemas import TextRequest, TextResponse
from text_classifier.utils.utils import setup_logger
import logging
import uvicorn

setup_logger()
logger = logging.getLogger(__name__)

app = FastAPI(title="Text Classification API")
classifier = TextClassifier()

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

def run():
    uvicorn.run("text_classifier.main:app", host="0.0.0.0", port=8000, reload=True)
