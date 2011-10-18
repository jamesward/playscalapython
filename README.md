Run locally
-----------

Start the Play JSON server:

    cd jsonserver
    play deps
    play run

Test the JSON server:  
[http://localhost:9000](http://localhost:9000)

Start the Python JSON client (and HTML server):

    cd jsonclient
    pip install -r requirements.txt
    python web.py

Test the Python JSON client:  
[http://localhost:5000](http://localhost:5000)


Run on Heroku
-------------

Deploy the Play JSON server:

    cd jsonserver
    git init
    git add .
    git commit -m init
    heroku create -s cedar
    git push heroku master

Deploy the Python JSON client:

    cd jsonclient
    git init
    git add .
    git commit -m init
    heroku create -s cedar
    heroku config:add JSON_SERVICE_URL=http://replacewiththeurltotheplayapp.herokuapp.com
    git push heroku master

Test the Python JSON client:

    heroku open

