FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /app/app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /app
EXPOSE 8000
