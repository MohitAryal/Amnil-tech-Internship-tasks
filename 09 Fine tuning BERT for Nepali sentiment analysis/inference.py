import torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer

app = FastAPI(
    title="Nepali Sentiment Analysis API",
    description="FastAPI endpoint for sentiment classification",
)

MODEL_NAME = "mohit4519/nepali-sentiment"

# Load on startup
tokenizer = AutoTokenizer.from_pretrained('Shushant/nepaliBERT')
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.float16,
    use_safetensors=True
)


class InputText(BaseModel):
    text: str


class OutputLabel(BaseModel):
    label: int


@app.post("/predict", response_model=OutputLabel)
def predict_sentiment(payload: InputText):

    # Tokenize input
    inputs = tokenizer(
        payload.text,
        return_tensors="pt",
        padding=True,
        truncation=True
    ).to(model.device)

    # Run inference
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=-1)

    # Label 
    class_id = torch.argmax(probs, dim=-1).item()
    if class_id == 1:
        new_class_id = 2 
    elif class_id == 2:
        new_class_id = 1
    else:
        new_class_id = class_id

    return OutputLabel(label=new_class_id)