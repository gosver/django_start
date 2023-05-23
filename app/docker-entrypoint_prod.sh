#!/bin/sh

if [ "$DB_DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "Mysql started"
fi

python main/manage.py migrate --noinput || exit 1
python main/manage.py collectstatic --noinput || exit 1


#gunicorn main.z_config.wsgi:application --bind 0:0:0.0:8000
#gunicorn --chdir main/z_config wsgi:application --bind 0:0:0.0:8000
#PYTHONPATH=`pwd`/main gunicorn --bind 0.0.0.0:8000 z_config.wsgi:application
#PYTHONPATH=`pwd`/main daphne -b 0.0.0.0 -p 8001 z_config.asgi:application
#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
supervisord -c /etc/supervisord.conf

exec "$@"