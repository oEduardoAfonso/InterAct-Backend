FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
RUN chmod +x flask.sh
CMD ["./flask.sh"]