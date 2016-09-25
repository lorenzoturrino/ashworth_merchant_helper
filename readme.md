MVP for the paytastic hackaton. send a POST request, get the best option for your transaction. 
admin forms to define the various quotes (read-only) and a log of all the past transactions (read only too)

data structure expected by the api: json encoded body
{
    'value': transaction_value,
    'currency': 3_letter_currency_code,
    'cardNumber': optional_card_number,
}

Sections:
    -merchantscript, a fake html page + a sample jquery form injector+handler
    -paymentbackend, a django application
    
Backend Installation:
    - Install python (used 3.4.5, not sure on 2.7 compatibility) and pip
    - optional: create a virtualenv
    - run $ pip install -r requirements.txt
    - cd into paymentbackend and run $ python manage.py migrate to update the DB schema
    - run $ python manage.py createsuperuser to add an admin user to the db.
 
Frontend: no installation. if you have node and want a quick way to serve files locally do.
    - Install Node
    - run $ npm install http-server -g

Running project:
    - in a shell, cd to paymentbackend and run $ python manage.py runserver
    - in a second shell, cd to merchantscript and run $ http=server
    - you might need to tweak the js script since it's hardcoded to look for the backend at 'http://127.0.0.1:8000/'
    - the admin dasboard is availalbe on the backend server at /admin
 
Code by Lorenzo Turrino