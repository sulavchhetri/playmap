FROM mcr.microsoft.com/playwright/python:v1.36.0-focal
WORKDIR /data
COPY . .
RUN python /data/setup.py install
RUN pip install -r requirements.txt
RUN pip install .
