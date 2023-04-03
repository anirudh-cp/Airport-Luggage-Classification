FROM python:3.7.1

ADD . /website
WORKDIR /website

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "run" ]