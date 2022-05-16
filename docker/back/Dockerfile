# Django
FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG APP=/code

WORKDIR ${APP}

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    libc-dev \
    bash \
    postgresql-client \
    && pip install --upgrade pip


COPY . ${APP}

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE ${PORT}

ENTRYPOINT [ "/code/docker/back/docker-entrypoint.sh" ]

CMD ["runserver"]
