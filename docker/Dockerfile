FROM python:3.9.7

RUN mkdir /www
WORKDIR /www
RUN mkdir /requirements
COPY ./requirements/ ./requirements
RUN pip install -r ./requirements/local.txt
# separted in other dockerfile
RUN pip install -r ./requirements/test.txt

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
ENV PYTHONUNBUFFERED 1
EXPOSE 8000