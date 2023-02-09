
# Descripton

Own django template for a basic website. Prepared already:
- templates and static files (html and css, including js, htmx and bootstrap)
- .env support in settings 
- docker and docker-compose support for local development 
- rest api infrastructure

# Instructions

Activate (create) virutal environment:
```
(python3 -m venv venv)
source venv/bin/activate
```
Create own `.env`file to replace `.env_dummy` (see name_of_env_file variable in settings.py)

```
python manage.py check
python manage.py runserver --noreload 
```

# Setup 

```
python3 -m pip install --upgrade pip
pip install django
pip install django-crispy-forms
pip install django-environ
pip install black
pip install djangorestframework


pip freeze -l > requirements.txt 
```

For docker (mac os):
```
open -a docker
```

Then:
```
docker-compose build
docker-compose up
```
Or simply:
```
docker-compose up --build
```
Then in browser: http://0.0.0.0:8000/

# Tips 
- Secret Key: https://djecrety.ir/
- Django-environ: https://django-environ.readthedocs.io/en/latest/quickstart.html
- bootstrap: https://getbootstrap.com/
- black package for code formatting: $ black format_my_file.py 
- organizations (groups): https://github.com/bennylope/django-organizations
- rest api: https://www.django-rest-framework.org/tutorial/quickstart/