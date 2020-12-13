FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /usr/src/app/backend

# Run unit tests
RUN [ "python", "./test_classifier.py" ]

# Run integration tests
RUN [ "python", "./test_integration.py" ]

WORKDIR /usr/src/app

RUN sed -i "s/localhost/host.docker.internal/g" frontend/index.html

RUN chmod +x ./start.sh

EXPOSE 8080
EXPOSE 5000

CMD [ "./start.sh" ]
