FROM alpine:latest
LABEL maintainer = "Hamza Hussain"
RUN apk update
RUN apk add --update py-pip python-dev build-base
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]
