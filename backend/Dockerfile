FROM python:3.11.7
RUN apt-get update
RUN apt-get install -y \
  dos2unix \
  libpq-dev \
  libmariadb-dev-compat \
  libmariadb-dev \
  gcc
WORKDIR ./backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFED 1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .