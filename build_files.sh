pip install venv
python3.9 -m venv env
env/Scripts/activate
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput