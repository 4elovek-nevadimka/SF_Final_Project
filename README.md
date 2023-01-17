# SF_FINAL_PROJECT
Final Project SkillFactory course

## SQL startup
create database:

```sh
$ create database final_project_dev;
```
create user:
```sh
$ CREATE USER final_project WITH
	LOGIN
	CREATEDB
	CREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'final_project';
```

## Project startup
install requirements:

```sh
$ pip install -r requirements.txt
```
apply migrations:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
init database by test data:
```sh
$ python manage.py init_db
```
run:
```sh
$ python manage.py runserver
```

## You are awesome :)
