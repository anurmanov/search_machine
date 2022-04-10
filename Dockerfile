FROM tiangolo/uvicorn-gunicorn-fastapi:latest
EXPOSE 5000
WORKDIR /
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y && pip3 install --upgrade pip && pip3 install -r requirements.txt
ENTRYPOINT ["/bin/bash", "/app/scripts/run.sh"]
