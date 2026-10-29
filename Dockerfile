FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD gunicorn --bind 127.0.0.1:5000 app:app
