# Signing server

Simple signing server developed in Django framework.

After successful registration, each user uploads files to the server.<br/>
User can ask for each uploaded file for its digital signature.<br/>
The server signs the file and returns the digital signature to the user.<br/>
<br/>
Also, each user can verify each uploaded file, but in this case, the user must upload the digital signature file to the server.
<br/>
A lot like delegate server.
https://en.wikipedia.org/wiki/Server-based_signatures


## Getting Started

### Prerequisites

Python 3.5.2
Django 1.11.3
PostgreSQL

### Running the server
Navigate to signing_server/ and execute:<br/>
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
<br/>

Open localhost:8000


## Authors

* **Ignatij Gichevski** - (https://github.com/ignatij)
