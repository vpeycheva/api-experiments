# Flask Rest API

This code is a self explanatory code, I got from [impythonist](https://impythonist.wordpress.com/2015/07/12/build-an-api-under-30-lines-of-code-with-python-and-flask/) blog.

I decided to go with sqlite, since its easy and fast, one posible upgrade of the task
would be to go with docker-compose with flask and mysql.
## To run the api
1. Execute `pip3 install -r requirements.txt `
2. Execute `./server.py`
3. The output will look like:
```bash
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
