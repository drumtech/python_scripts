FROM python:3.10
ENV PYTHONUNBUFFERED 1
ADD simple_api /simple_api
WORKDIR /simple_api
RUN pip install --upgrade pip;\
    pip install -r requirements.txt
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["/usr/local/bin/python"]
EXPOSE 8000/tcp
