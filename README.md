# ASSOGEST

## Setup

```bash
# Create a virtual environment with Python3
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the requirements
./pip-install.sh

# Create the database
./manage.py migrate
```

## Update requirements

```bash
./pip-freeze.sh
```

## Database

Currently the project uses a SQLite database. It is created automatically when running migration

Next step: Use PostgreSQL

## Seeds

### Write seeds

```bash
./make_seeds.sh
```

Or alternatively:

```bash
./manage.py dumpdata core > seeds/users.json
./manage.py dumpdata organization > seeds/organization.json
./manage.py dumpdata agenda > seeds/agenda.json
// OR 
./manage.py dumpdata core organization agenda > seeds/full_data.json
```

### Load seeds

```bash
./load_seeds.sh
```

Or alternatively:

```bash
./manage.py loaddata seeds/users.json
./manage.py loaddata seeds/organization.json
./manage.py loaddata seeds/agenda.json
// OR
./manage.py loaddata seeds/full_data.json
```

### Users in seeds

- admin@django.com / django1234 (super user)
- seb@asso.com / django1234
- jake.peralta@asso.com / django1234
- rosa.diaz@b99.com / django1234
- amy.santiago@b99.com / django1234
- raymond.holt@b99.com / django1234
- charles.boyle@b99.com / django1234

