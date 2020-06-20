FROM python:3.6.9
COPY . /
RUN pip install -r /requirements.txt
EXPOSE 5000
ENV FLASK_ENV="docker"
ENTRYPOINT ["python"]
CMD ["server/flask_server.py"]

