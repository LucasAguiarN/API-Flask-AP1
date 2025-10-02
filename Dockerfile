FROM python:3.13.2

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

EXPOSE 5000
CMD ["flask", "run"]