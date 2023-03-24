FROM python:3.11-slim-bullseye

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py

RUN pip install -r requirements.txt

CMD ["python", "/app/main.py"]
