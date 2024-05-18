import os

working_dir = os.getcwd()
models_path = os.path.join(working_dir, "models")

spacy_path = os.path.join(models_path, "spacy")
spacy_model = os.path.join(spacy_path, "model-best")

distilBERT_path = os.path.join(models_path, "distilBERT")
distilBERT_model = os.path.join(distilBERT_path, "model-best")

logs_path = os.path.join(working_dir, "metrics", "logs")