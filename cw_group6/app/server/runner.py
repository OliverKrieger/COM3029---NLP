from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from entity_recogniser.recogniser import run_model

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
    response = run_model(request.form.get('ai_models'), request.form.get('input_text'))
    return str(response)