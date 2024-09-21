FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY server /app/server
WORKDIR /app/server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]