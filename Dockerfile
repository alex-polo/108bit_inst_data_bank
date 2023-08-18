FROM python:3.11

RUN mkdir /inst_data_bank
WORKDIR /inst_data_bank

COPY requirements.txt .
RUN pip install -r requirements.txt

#COPY . .
COPY server .

#WORKDIR src
CMD gunicorn server:app --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000