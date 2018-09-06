# WorkGen

## Setup
1. ```pip3 install -r requirements.txt```
2. Setup MySQL locally.
3. Create a database called workgen in MySQL
4. Set environment variables ```WORKGEN_USER``` and ```WORKGEN_PASSWORD``` as your MySql username and password
5. ```python3 manage.py migrate```


## Running the Web Server
1. First run ```redis-server``` on a separate terminal
2. Run ```./manage.py runserver``` from django project root
3. Start celery workers by running ```celery worker -A workgen --loglevel=DEBUG --concurrency=4```
