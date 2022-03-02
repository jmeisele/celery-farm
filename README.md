# Overview

🚧🚧🚧 Work in progress 🚧🚧🚧

Asynchronous Tasks with FastAPI, MongoDB, Redis and Celery with React front end.

Full stack solution incroporating an open source long running solver optimization suite.

## Architecture

![Arch](./docs/arch.drawio.svg)

Gunicorn is used for managing the Uvicorn workers (ASGI servers). Redis acts as our broker to our celeryworkers, and finally MongoDB to persist data.

A full optimization loop looks like this:

1. Client sends Problem data and Solver parameters via POST request. The data will be validated against the the Problem schema and Solver schema, thanks to Pydantic.
2. The server will respond with a unique ID back to the client and asynchronously:
   - Inserts problem data, solver params into MongoDB under the unique ID
   - Send the unique ID to our Celery workers via the Redis broker
3. Celery workers pick up the unique ID from the redis broker and pulls the problem data and solver parameters from MongoDB. The worker builds the Solver model instance and starts the opitmization process using the SCIP suite.
4. Our Celery worker constantly stores the state of the task in our Redis broker which can be polled.
5. A successful optimization updates the record in MongoDB by the unique ID.
6. The client can then fetch the results by sending a GET request with the unique ID as a parameter.

## Contributors

<a href="https://github.com/jmeisele/celery-farm/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jmeisele/celery-farm" />
</a>

