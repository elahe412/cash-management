# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /cash_management
COPY requirements.txt /cash_management/
RUN pip install -r requirements.txt
COPY . /cash_management/

CMD python /cash_management/manage.py migrate && python /cash_management/manage.py runserver  0.0.0.0:8000
