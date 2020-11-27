FROM python:3.8
LABEL maintainer="Rafi Bayer rafibayer7@gmail.com"

RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY /server /server
EXPOSE 9091
WORKDIR /server
CMD ["python", "server.py"]
