from .model_spacy import spacy_recognise_entities
from .model_distilBERT import distilBERT_recognise_entities

def run_model(model_type:str, input:str):
    match model_type:
        case "spaCy":
            return spacy_recognise_entities(input)
        case "DistilBERT":
            return distilBERT_recognise_entities(input)
        case _:
            print(f"ERROR - no type of {model_type}")