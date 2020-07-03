# Installation

### Install pipenv
```
pipenv shell
```
### Install dependency
```
pipenv install
``` 

### Run the server
```
python manage.py runserver
```
### Run the test
```
python manage.py test
```

### Migrate Database
```
python3 manage.py migrate
```

#### Steps to setup a new Model
* First Create a class inside a models.py file.
* Define Class attruibutes. (Class attributes will be the table columns.)
* Create migrations for that class
```
python mmanage.py makemigrations
```
