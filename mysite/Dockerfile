FROM python:3.11.0-bullseye
# EXPOSE 8000
RUN pip install django
WORKDIR /mysite
COPY . /mysite
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ALLOWED_HOSTS=['app']
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
