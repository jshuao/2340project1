Commands to run to setup the project

python3 -m venv venv

source venv/bin/activate

pip install -r jobboard/requirements.txt

cd jobboard

python manage.py migrate

python manage.py runserver
