FROM python:3.11.10-bookworm AS builder-image

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y build-essential && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install pipx

RUN pipx install poetry

RUN export PATH=$PATH:/root/.local/bin

RUN echo 'export PATH=$PATH:/root/.local/bin' >> ~/.bashrc

WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1

RUN /root/.local/bin/poetry install

EXPOSE 8000

CMD ["/root/.local/bin/poetry", "run", "fastapi", "run", "app/server.py"]