FROM python:3

WORKDIR /usr/src/app

COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt ./
# COPY src ./
COPY src /youtrack-githooks
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
