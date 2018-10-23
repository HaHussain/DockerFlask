FROM alpine:latest
LABEL maintainer = "Hamza Hussain"
RUN apk update
RUN apk add --update py-pip python-dev build-base
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
