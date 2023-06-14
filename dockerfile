FROM python:3.10.6-buster

WORKDIR /deliberAIde
RUN pip install --upgrade pip

COPY deliberAIde deliberAIde
COPY requirements.txt requirements.txt
COPY setup.py setup.py
#COPY stream.py stream.py

# First, pip install dependencies
# must develop requirements.txt
#RUN pip install -r requirements.txt
RUN pip install .

# ...
#CMD ["streamlit","run","stream.py"] # THIS TO DO
# CMD gunicorn -w  4 -b 0.0.0.0:5000 deliberAIde.interface.app:app
#CMD exec gunicorn -w 1 --bind :$PORT deliberAIde.interface.app:app
#docker run -e PORT=8000 -p 8080:8000 new3:latest
CMD python -m deliberAIde.interface.app $PORT
