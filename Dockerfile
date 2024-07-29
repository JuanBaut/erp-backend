ARG PYTHON_BASE=3.12
# build stage
FROM python:$PYTHON_BASE AS builder

# install PDM
RUN pip install -U pdm
# disable update check
ENV PDM_CHECK_UPDATE=false

# copy files
COPY pyproject.toml pdm.lock manage.py /project/
COPY erp_backend/ /project/erp_backend
COPY base/ /project/base

# install dependencies and project into the local packages directory
WORKDIR /project
RUN pdm install --check --prod --no-editable

CMD ["pdm", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
