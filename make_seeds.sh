./manage.py dumpdata core > seeds/users.json
./manage.py dumpdata organization > seeds/organization.json
./manage.py dumpdata agenda > seeds/agenda.json

./manage.py dumpdata core organization agenda > seeds/full_data.json