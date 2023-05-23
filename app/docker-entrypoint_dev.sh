#!/bin/sh

# switch on if use mysql  for waiting
#if [ "$DB_DATABASE" = "mysql" ]
#then
#    echo "Waiting for mysql..."
#
#    while ! nc -z $DB_HOST $DB_PORT; do
#      sleep 0.1
#    done
#
#    echo "Mysql started"
#fi

python main/manage.py makemigrations --noinput || exit 1
python main/manage.py migrate --noinput || exit 1
echo "migrations added"
exec "$@"