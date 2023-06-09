FROM python:3.8.6-buster


WORKDIR /prod

RUN pip install --upgrade pip

COPY Makefile Makefile

# First, pip install dependencies
COPY requirements.txt requirements.txt # must develop requirements.txt
RUN pip install -r requirements.txt

# Then only, install taxifare!
COPY deliberAIde deliberAIde
COPY  api api


COPY setup.py setup.py
RUN pip install .




# ...
CMD uvicorn api.app:app --host 0.0.0.0 --port $PORT # THIS TO DO
