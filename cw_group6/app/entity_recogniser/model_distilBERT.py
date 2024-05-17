from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


from utils.paths import distilBERT_model

tag_list = ["B-O", "B-AC", "B-LF", "I-LF"]
id2label = [{idx:tag} for idx, tag in enumerate(tag_list)]
label2id = [{tag:idx} for idx, tag in enumerate(tag_list)]

tokenizer = AutoTokenizer.from_pretrained(distilBERT_model)
model = AutoModelForTokenClassification.from_pretrained(distilBERT_model)

from transformers import pipeline

classifier = pipeline("ner", model=distilBERT_model)


def distilBERT_recognise_entities(input:str):
    print("OUTPUT:", classifier(input))

    return [(ent["word"], ent["entity"]) for ent in classifier(input)]