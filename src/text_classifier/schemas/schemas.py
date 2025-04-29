from pydantic import BaseModel, Field

class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, example="This is amazing!")

class TextResponse(BaseModel):
    label: str
    score: float
