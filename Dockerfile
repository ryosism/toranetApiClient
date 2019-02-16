FROM python:3.7

WORKDIR /app
ADD . /app
ADD . /lib

RUN apt-get update && apt-get install -y \
      wget \
      xz-utils

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt-get update
RUN apt-get install google-chrome-stable
RUN pip install -i requirements.txt -t lib/

CMD ["python", "main.py", "app.yaml"]
