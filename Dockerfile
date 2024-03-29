FROM python:3.10

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./backup_drive_api.py" ]
