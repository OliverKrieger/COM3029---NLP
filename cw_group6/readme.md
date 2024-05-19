## Dependencies

- Flask 3.0.3 (https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- jinja2
- spaCy 3.7.2
- spacy-transformers
- htmx (https://htmx.org/)
- transformers==4.36.2
- matplotlib


## Startup

run `python -m flask --app main run` in the app folder

# Docker Runner

- make sure Docker installed
- make sure WSL installed

Within the `app` folder

build `docker build -t nerapp .`
run server `docker run --rm -it -p 5000:5000 nerapp`