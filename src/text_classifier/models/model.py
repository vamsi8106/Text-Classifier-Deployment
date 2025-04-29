from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

class TextClassifier:
    def __init__(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"):
        try:
            logger.info(f"Loading model: {model_name}")
            self.classifier = pipeline("text-classification", model=model_name)
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise RuntimeError("Model loading failed.")

    def predict(self, text: str) -> dict:
        try:
            result = self.classifier(text)
            logger.info(f"Prediction completed")
            return result[0]
        except Exception as e:
            logger.error(f"Prediction error: {e}")
            raise ValueError("Prediction failed.")
