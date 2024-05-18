from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from entity_recogniser.recogniser import run_model
from metrics.log_metrics import log_metric
import traceback

simple_page = Blueprint('simple_page', __name__,
                        template_folder='../pages')

@simple_page.route('/')
def show():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        abort(404)

@simple_page.post('/get_tags')
def get_tags():
    try:
        response = run_model(request.form.get('ai_models'), request.form.get('input_text'))
        print("RESPONSE: ", response)
        log_metric({
            "input":request.form.get('input_text'),
            "prediction":response,
            "model_type":request.form.get('ai_models')
        })
        return render_template("results.html", tokens=response)
    except TemplateNotFound:
        abort(404)
    except Exception:
        log_metric({
            "input":request.form.get('input_text'),
            "prediction":response,
            "model_type":request.form.get('ai_models'),
            "error": str(traceback.format_exc())
        })
        return render_template("results.html", tokens=[])