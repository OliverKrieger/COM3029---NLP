FROM docker.io/pytorch/pytorch:2.2.1-cuda12.1-cudnn8-runtime
 
WORKDIR /app
RUN python -m pip install -U setuptools pip wheel
ADD requirements.txt .

RUN python -m pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

ADD . .
RUN python test_runner.py

CMD ["bash", "docker_start.bat"]