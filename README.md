# Signing server

Simple signing server developed in Django framework.

After successful registration, each user uploads files to the server.<br/>
User can ask for digital signature for each of the uploaded files.<br/>
The server signs the file and returns the digital signature to the user.<br/>
<br/><br/>
Also, each user can verify each uploaded file, but in this case, the user must upload the digital signature file to the server.
<br/>
A lot like delegate server.<br/>
https://en.wikipedia.org/wiki/Server-based_signatures


## Getting Started

### Prerequisites

Python 3.5.2<br/>
Django 1.11.3<br/>
PostgreSQL<br/>

### Running the server
Execute:<br/>
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Open localhost:8000
<br/><br/><br/>

## Authors

* **Ignatij Gichevski** - (https://github.com/ignatij)
