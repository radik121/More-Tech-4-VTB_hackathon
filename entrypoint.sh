#!/bin/sh

python ./api/manage.py makemigrations
python ./api/manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python ./api/manage.py shell

exec "$@"
