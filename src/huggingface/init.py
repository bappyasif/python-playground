from transformers import AutoTokenizer, AutoModelForSequenceClassification
from fastapi import FastAPI

app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

@app.post("/classify")
async def classify_text(text: str):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt")

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted label
    logits = outputs.logits
    predicted_label = logits.argmax().item()

    return {"label": predicted_label}

# Load model directly
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
# model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

# response = model.generate(
#     **tokenizer(
#         "Text to summarize",
#         return_tensors="pt",
#         max_length=512,
#         truncation=True,
#     ),
#     max_length=142,
#     no_repeat_ngram_size=3,
#     num_beams=4,
# )

# print(response)



# from transformers import pipeline
# import torch # due to this im going with alternative approach of using transformers directly


# model = pipeline(task='summarization', model='facebook/bart-large-cnn')

# response = model("Text to summarize")

# print(response)

# model = pipeline(
#     "question-answering",
#     model="deepset/roberta-base-squad2",
#     tokenizer="deepset/roberta-base-squad2"
# )