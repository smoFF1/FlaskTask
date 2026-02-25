FROM python:3.15.0a6-slim-trixie
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt 
EXPOSE 5000
COPY . /app
ENTRYPOINT [ "python", "app.py" ]
