# pull official base image
FROM python:3.10-alpine3.17
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./app/requirements.txt ./
RUN pip install --requirement requirements.txt
# copy project
COPY ./app .

ENTRYPOINT [ "sh", "/usr/src/app/docker-entrypoint_dev.sh" ]
#ENTRYPOINT ["tail", "-f", "/dev/null"]