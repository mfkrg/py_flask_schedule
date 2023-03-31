FROM python

COPY . /flask

WORKDIR /flask

EXPOSE 8800

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir flask selenium minio

CMD [ "python", "./main.py"]