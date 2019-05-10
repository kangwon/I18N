# How to Use

1. Clone the project and go to the directory.
```shell
git clone https://github.com/kangwon/I18N.git
cd I18N
```
2. Create a virtual environment and activate it.
```shell
python3 -m venv venv
source venv/bin/activate
```
3. Install the requirements.
```shell
(venv) pip isntall -r proejct/requirements.txt
```
4. Run the server. You can find more details at [the Django doument](https://docs.djangoproject.com/en/2.2/ref/django-admin/#runserver).
```shell
(venv) python project/manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 10, 2019 - 01:06:19
Django version 2.2.1, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
The Django REST Framework provides handy interface. Try exploring the API on a browser at http://localhost:8000.


# Using Technologies

- Language: Python3.6
- Web Framework: Django REST Framework
- Database: SQLite3
