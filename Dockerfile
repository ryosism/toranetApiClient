FROM python:3.7

WORKDIR /app
ADD . /app

RUN apt-get update && apt-get install -y \
      wget \
      xz-utils

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update
RUN apt-get install -y google-chrome-stable

RUN pip install -r requirements.txt

EXPOSE 8080

# CMD ["python", "main.py", "app.yaml"]
ENTRYPOINT gunicorn -b :$PORT main:app
