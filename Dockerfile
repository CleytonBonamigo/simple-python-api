FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV FLASK_ENV=development

COPY . .

EXPOSE 6000

ENTRYPOINT [ "python", "main.py", "--port=6000" ]