FROM python:alpine3.21

EXPOSE 3001
EXPOSE 3002
EXPOSE 3003

RUN apk update
RUN apk upgrade
#RUN apk add gcc
RUN apk add alpine-sdk

## Copy over our application file
RUN mkdir app
WORKDIR "/app"
COPY dis_sender.py dis_sender.py

## Clone the open-dis libraries that I need 
RUN mkdir open_dis_python
WORKDIR "/app/open_dis_python"
COPY open_dis_python .
#RUN pip install --upgrade pip
#RUN pip install numpy
RUN pip install .

WORKDIR "/app"
CMD ["python3", "/app/dis_sender.py"]