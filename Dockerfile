FROM library/python:3.7-slim

WORKDIR /opt/app

COPY . .

RUN pip3.7 install -r requirements.txt

EXPOSE 8080

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]
