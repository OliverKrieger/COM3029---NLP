from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from utils.paths import distilBERT_model

tokenizer = AutoTokenizer.from_pretrained(distilBERT_model)
model = AutoModelForTokenClassification.from_pretrained(distilBERT_model)

from transformers import pipeline

classifier = pipeline("ner", model=distilBERT_model)

def distilBERT_recognise_entities(input:str):
    return [(ent["word"], ent["entity"]) for ent in classifier(input)]