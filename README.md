# ASSOGEST

## Setup

```bash
# Create a virtual environment with Python3
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the requirements
./pip-install.sh

# Install npm dependencies
npm install

# Start Docker services (PostgreSQL, Redis, and Celery)
docker-compose up -d

# Create the database
./manage.py migrate

# Start the development server (in two separate terminals)
npm run dev
```

## Update requirements

```bash
./pip-freeze.sh
```

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
- raymond.holt@b99.com / django1234 (organization admin)
- charles.boyle@b99.com / django1234

## Services

The application uses several services managed through Docker:
- PostgreSQL as the database
- Redis as the message broker
- Celery for asynchronous tasks (email sending)

Development emails are stored in the `tmp/emails/` directory.

