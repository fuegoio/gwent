FROM python:3.7.3-stretch

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD run.py /app/

ADD gwent /app/gwent

CMD ["python", "run.py"]

