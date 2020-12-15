# Sentiment Analysis Application

## Link to Trello
[https://trello.com/b/9uwlT1Hw/project-2](https://trello.com/b/9uwlT1Hw/project-2)

## Run the docker image

To run the service, run the following command:
```
docker run -p 8080:8080 -p 5000:5000 themrzz/de-project-2:latest
```

This will run:
- The API, on port 5000
- The website itself, on port 8080

Go to [http://localhost:8080](http://localhost:8080) and start playing with the application!

## Locally building the container

Building the docker file:
```
docker build -t "de-project-2" .
```

This will run the unit tests & the integration test.

Running the image:
```
docker run -p 8080:8080 -p 5000:5000 "de-project-2"
```

## Tests
Running the unit tests (inside the `backend` folder):
```
python test_unit.py
```

Running the integration tests (inside the `backend` folder):
```
python test_integration.py
```

Running the stress tests (inside the `backend` folder):
```
python test_stress.py
```
