FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev gcc

WORKDIR /app

# install general dependencies
ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY pyproject.toml /app/
COPY poetry.lock /app/
RUN pip install poetry
RUN poetry install --no-root

COPY ./ /app/

ENV FLASK_ENV="development"

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "-c", "flask run --host 0.0.0.0"]