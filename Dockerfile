FROM python:3.9-alpine3.13
LABEL maintainer="caleb@caleb.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /tmp/
COPY requirements.dev.txt /tmp/
COPY . /app /app/
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py
RUN /py/bin/pip install --upgrade pip
RUN /py/bin/pip install --no-cache-dir -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then \
    /py/bin/pip install --no-cache-dir -r /tmp/requirements.dev.txt; \
    fi

RUN rm -rf /tmp/requirements.txt && \
    adduser \
    --disabled-password \
    --no-create-home \
    user    

RUN chown -R user:user /app
ENV PATH="/py/bin:$PATH"
USER user