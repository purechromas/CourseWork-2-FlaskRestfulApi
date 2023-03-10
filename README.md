## WELCOME IN MY COURSE WORK WITH FLASK AND RELATED LIBRARIES
***
#### This is a repository for a SKYPRO course work project!
***
#### This is REST-ful API created for a movie site -> Kinopoisk
***
### INSTALLATION:

* python -m venv venv (after this you need to activate it)
* pip install -r requirements.txt
* python create_tables_and_load_data.py (run the script)
* python app.py

### API ENDPOINTS
    
* GET /movies 
* GET /movies/{pk}
* GET /genres
* GET /genres/{pk}
* GET /directors
* GET /directors/{pk}
* GET /movies/?status=new&page=1
* GET /movies/?page=2
* POST /auth/register
* POST /auth/login
* PUT /auth/login
* GET /user
* PATCH /user
* PUT /user/password
* POST /favorites/movies/{pk}
* DELETE /favorites/movies/{pk}

### TESTS

* There is also folder with name tests witch is testing dao and service.

### LIBRARIES

* flask
* flask_restx
* flask_sqlalchemy
* marshmallow
* unitest
* pyjwt
* hmac
* hashlib
* base64
* calendar
* datetime
* pytest

### MADE BY BLAGOVEST NEDKOV