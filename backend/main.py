try:
    from fastapi import FastAPI
    from pydantic import BaseModel
    from transformers import pipeline
except ImportError as e:
    raise ImportError(f"Required packages not installed. Please run: pip install fastapi pydantic transformers") from e

app = FastAPI()

model = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(data: TextInput):
    result = model(data.text)[0]
    return {
        "label": result["label"],
        "score": float(result["score"])
    }