FROM alpine:latest
LABEL maintainer = "Hamza Hussain"
RUN apk update
RUN apk add --update py-pip python-dev build-base
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
