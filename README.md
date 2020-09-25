1. Open a terminal, navigate into the project directory, and run:
```
$ source venv/bin/activate
$ explort FLASK_APP=example_basic_authentication.py
$ flask run
```

2. Open a second terminal window, and run:
```
~ $ curl --include http://localhost:5000/
HTTP/1.0 401 UNAUTHORIZED
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: <Flask 'example'> realm="Authentication Required"
Server: Werkzeug/1.0.1 Python/3.8.3
Date: Thu, 24 Sep 2020 15:13:54 GMT

Unauthorized Access
```

```
~ $ curl --include --user john:hello http://localhost:5000/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/1.0.1 Python/3.8.3
Date: Thu, 24 Sep 2020 15:14:39 GMT

{"message":"Hello, john!"}
```

```
~ $ curl --include --user susan:hello http://localhost:5000/
HTTP/1.0 401 UNAUTHORIZED
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: <Flask 'example'> realm="Authentication Required"
Server: Werkzeug/1.0.1 Python/3.8.3
Date: Thu, 24 Sep 2020 15:14:47 GMT

Unauthorized Access
```

```
~ $ curl --include --user susan:bye http://localhost:5000/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 28
Server: Werkzeug/1.0.1 Python/3.8.3
Date: Thu, 24 Sep 2020 15:14:52 GMT

{"message":"Hello, susan!"}
```