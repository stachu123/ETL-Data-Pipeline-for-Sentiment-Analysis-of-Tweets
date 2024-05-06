FROM apache/airflow:latest
ENV PIP_USER=false
COPY requirements.txt .
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PIP_USER=true
