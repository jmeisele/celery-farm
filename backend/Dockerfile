FROM python:3.9.7-slim-buster as base

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip3 install poetry==1.1.11

RUN apt-get update \
    && apt-get -y install netcat gcc

# Install SCIP dependencies
RUN apt-get -y install \
        libblas3 libboost-program-options1.67.0 \
        libcliquer1 libgfortran5 \
        libgmpxx4ldbl libgsl23 \
        libgslcblas0 liblapack3\
        libopenblas-base libtbb2\
        curl\
    && apt-get clean

COPY ./SCIPOptSuite-7.0.3-Linux-debian.deb /app
RUN dpkg -i SCIPOptSuite-7.0.3-Linux-debian.deb \
    && rm SCIPOptSuite-7.0.3-Linux-debian.deb

RUN poetry config virtualenvs.create false

FROM base as prod
RUN poetry install --no-dev
COPY . /app/

FROM base as dev
RUN poetry install
COPY . /app/