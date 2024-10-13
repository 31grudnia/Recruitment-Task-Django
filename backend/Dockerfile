FROM python:3.12-slim as PYTHON_IMAGE

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /recruitment_task/backend

COPY requirements.txt /recruitment_task/backend
RUN pip3 install -r requirements.txt

COPY . /recruitment_task/backend

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]