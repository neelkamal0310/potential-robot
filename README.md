# Usage

* Clone the repo
```
git clone git@github.com:neelkamal0310/potential-robot.git
cd potential-robot
```
* Activate virtual env and install requirements
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
* Run migrations
```
python manage.py migrate
```
* Create a user
```
python manage.py createsuperuser
```
* Load data
```
python manage.py loaddata initial
```
* Run server
```
python manage.py runserver
```
* Go to the dashboard [here](http://127.0.0.1:8000/admin/) and login using the credentials.
