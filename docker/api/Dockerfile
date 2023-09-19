FROM python:3.11-buster as builder

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN touch README.md

RUN poetry config virtualenvs.create false && poetry config installer.max-workers 10
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

#EXPOSE 5000

#ENTRYPOINT ["poetry", "run", "python3", "-m", "main.main"]
#ENTRYPOINT ["python3", "-m", "main.main"]

FROM python:3.11-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY ./src ./





