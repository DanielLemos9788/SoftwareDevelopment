FROM python:3.9-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONUNBUFFERED=1

# Turns off buffering for easier container logging
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libcurl4-openssl-dev \
    netcat \
&& rm -rf /var/lib/apt/lists/*

COPY requirements /tmp/requirements

RUN pip install --upgrade pip==20.2.3
RUN pip install -Ur /tmp/requirements/requirements.txt

ENV APP_HOME=/pokemon_services

WORKDIR $APP_HOME

COPY postgres-healthy.sh /tmp/postgres-healthy.sh

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
RUN mkdir -p $APP_HOME && chown user:user $APP_HOME

USER user

ENTRYPOINT ["bash", "/tmp/postgres-healthy.sh"]

CMD python pokemon_services/manage.py migrate && python pokemon_services/manage.py runserver 0:8000



