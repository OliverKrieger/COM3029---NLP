import os

working_dir = os.getcwd()
models_path = os.path.join(working_dir, "models")

spacy_path = os.path.join(models_path, "spacy")
spacy_model = os.path.join(spacy_path, "model-best")

distilBERT_path = os.path.join(models_path, "distilBERT")
distilBERT_model = os.path.join(distilBERT_path, "model-best")

metrics_path = os.path.join(working_dir, "metrics")
logs_path = os.path.join(metrics_path, "logs")

static_path = os.path.join(working_dir, "static")
static_figs_path = os.path.join(static_path, "figs")
static_figs_performance_path = os.path.join(static_figs_path, "performance")

unit_test_path = os.path.join(working_dir, "unit_tests")