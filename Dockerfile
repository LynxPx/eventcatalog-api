FROM python:3.11-slim

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# work directory inside the container
WORKDIR /code

# Install pip dependencies
COPY poetry.lock pyproject.toml /code/
RUN pip install poetry && poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copy project
COPY . /code/

# Set the STOPSIGNAL to SIGINT
STOPSIGNAL SIGINT

# Command to run the application
CMD ["uvicorn", "eventcatalog_api.server.main:app", "--host", "0.0.0.0", "--port", "80"]