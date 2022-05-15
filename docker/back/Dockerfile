# Django
FROM python:3.8
ENV PYTHONUNBUFFERED 1

ARG APP=/code

WORKDIR ${APP}

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    postgresql-client

COPY . ${APP}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${PORT}

ENTRYPOINT [ "/code/docker/back/docker-entrypoint.sh" ]

CMD ["runserver"]
