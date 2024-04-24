FROM python:3.12

RUN mkdir /app
WORKDIR /app

RUN apt update

COPY requirements.txt ./
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]