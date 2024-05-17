import spacy
from utils.paths import spacy_model

nlp = spacy.load(spacy_model)

def spacy_recognise_entities(input:str):
    doc = nlp(input)
    print("SERVER RESULT: ", [(ent.text+"<"+ent.label_+">") for ent in doc.ents])
    return [(ent.text+"["+ent.label_+"]") for ent in doc.ents]