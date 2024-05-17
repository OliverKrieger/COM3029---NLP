from app.entity_recogniser.model_spacy import spacy_recognise_entities

def run_model(model_type:str, input:str):
    match model_type:
        case "spacy":
            return spacy_recognise_entities(input)
        case _:
            print(f"ERROR - no type of {model_type}")