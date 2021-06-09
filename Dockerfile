
FROM alpine:3.5
RUN apk add --update py2-pip
RUN pip install --upgrade pip
COPY requirements.txt /var/www/html/test/
RUN pip install --no-cache-dir -r /var/www/html/requirements.txt
COPY app.py /var/www/html/test/
COPY index.html /var/www/html/test/
EXPOSE 80
CMD ["python", "/var/www/html/test/"]

