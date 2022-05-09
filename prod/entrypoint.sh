#!/bin/bash

if [ "$DATABASE" = "mariadb" ]
then
	echo "Waiting for mariadb to be up"

	while ! nc -z $MARIADB_HOST $MARIADB_PORT; do
	  sleep 0.2
	done

	echo "Mariadb started"
fi

echo "GRANT ALL on *.* to '${MARIADB_USER}'; "| mysql -u root --password="${MARIADB_ROOT_PASSWORD}" -h "${MARIADB_HOST}"

python manage.py flush --no-input
python manage.py migrate
python manage.py loaddata db.json
python manage.py collectstatic --noinput 

exec "$@"

