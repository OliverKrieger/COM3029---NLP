from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from entity_recogniser.recogniser import run_model
from metrics.log_metrics import log_metric, get_log_metrics
from metrics.model_performance import evaluate_model_performance
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
    
@simple_page.route('/admin')
def admin():
    try:
        return render_template("admin.html")
    except TemplateNotFound:
        abort(404)

@simple_page.post('/login')
def admin_login():
    try:
        if request.form.get('username') == "admin" and request.form.get('password') == "nerproject":
            return render_template("admin_panel.html", login_token="869ec48ioh8fkyad")
        else:
            return render_template("401.html")
    except TemplateNotFound:
        abort(404)

@simple_page.post('/logs')
def admin_logs():
    try:
        if request.form.get('login_token') == "869ec48ioh8fkyad":
            return render_template("logs_panel.html", log_data=get_log_metrics())
    except TemplateNotFound:
        abort(404)

@simple_page.post('/performance')
def admin_performance():
    try:
        if request.form.get('login_token') == "869ec48ioh8fkyad":
            return render_template("performance_panel.html")
    except TemplateNotFound:
        abort(404)

@simple_page.post('/performance-results')
def admin_performance_results():
    try:
        response = evaluate_model_performance(request.form.get('ai_models'), request.form.get('text_input'), request.form.get('time_for_requests'), request.form.get('number_of_requests'))
        print("RESPONSE:", response)
        return render_template("performance_results.html", performance_data=response)
    except TemplateNotFound:
        abort(404)