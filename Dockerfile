ARG PYTHON_BASE=3.12

FROM python:$PYTHON_BASE AS builder

RUN pip install -U pdm
ENV PDM_CHECK_UPDATE=false

COPY src/ /project/

WORKDIR /project
