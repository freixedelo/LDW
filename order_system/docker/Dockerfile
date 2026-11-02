FROM python:3.13-slim
ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
build-essential nodejs npm
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod 0755 /entrypoint.sh
CMD ["/entrypoint.sh"]