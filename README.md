# ToDo

Python/Django practice

## Run project

- Install python (brew/apt install python) /pip included
- Install virtualenv `pip3 install virtualenv`
- Run `pip install` in project root
- Run `src/manage.py runserver` for run project or setup IDE run config

### Commands for start new project

- Create project folder `mkdir project_name` 
- Change dir `cd porject_name`
- Create virtual environment `virtualenv -p python3 venv`
- Activate virtual env. `. venv/bin/activate`
- Install django `pip install django`
- Save dependencies to file `pip freeze > requirements.txt`
- Init django project `django-admin startproject core`
- Rename wrap folder `mv core src`
- Change dir: `cd src`
- Initial migration for default apps by django (auth, ...) `./manage.py migrate`
- Create super user `./manage.py createsuperuser`
- Create new our django app `./manage.py startapp webapp`