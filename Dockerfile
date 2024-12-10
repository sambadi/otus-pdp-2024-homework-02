FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install poetry==1.8.3 && poetry install

CMD ["poetry", "run", "pyright", "./homework_02"]