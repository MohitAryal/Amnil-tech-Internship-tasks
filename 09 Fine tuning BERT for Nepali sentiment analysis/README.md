"""---
language: ne
license: apache-2.0
tags:
- sentiment-analysis
- nepali
- onnx
- bert
- text-classification
datasets:
- custom-nepali-sentiment
metrics:
- f1
- accuracy
model-index:
- name: mohit4519/nepali-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Nepali Sentiment Dataset
      type: custom
    metrics:
    - type: f1
      value: 0.XX  # Replace with your actual score
      name: Macro F1
---

# Nepali Sentiment Analysis (ONNX)

This model is a fine-tuned BERT model for Nepali sentiment analysis, exported to ONNX format for optimized inference.

## Model Details

- **Base Model**: Shushant/nepaliBERT
- **Task**: Sentiment Classification (3-class)
- **Labels**:
  - 0: Negative
  - 1: Neutral
  - 2: Positive
- **Format**: ONNX (optimized for fast inference)

## Usage

### Installation

```bash
pip install -r requirements.txt
```

### Inference
```bash
uvicorn inference:app
```


## Performance

- **Macro F1 Score**: 0.78
- **Accuracy**: 0.8

## Training Data

Trained on Nepali sentiment dataset containing social media text, reviews, and comments.

## Limitations

- Best performance on Nepali text
- May have reduced accuracy on code-mixed or transliterated text
- Performance varies across different domains
"""