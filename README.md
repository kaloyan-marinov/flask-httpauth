# Example: basic authentication

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

# Example: token authentication

1. Open a terminal, navigate into the project directory, and run:
```
$ source venv/bin/activate
$ explort FLASK_APP=example_token_authentication.py
$ flask run
```

2. Open a second terminal window, and run:
```
~ $ curl --verbose http://localhost:5000/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: text/html; charset=utf-8
< Content-Length: 19
< WWW-Authenticate: Bearer realm="Authentication Required"
< Server: Werkzeug/1.0.1 Python/3.8.3
< Date: Fri, 25 Sep 2020 03:41:28 GMT
< 
* Closing connection 0
Unauthorized Access
```

```
~ $ curl --verbose --header "Authorization: Bearer secret-token-1" http://localhost:5000/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
> Authorization: Bearer secret-token-1
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/1.0.1 Python/3.8.3
< Date: Fri, 25 Sep 2020 03:45:21 GMT
< 
{"message":"Hello, john!"}
* Closing connection 0
```

```
~ $ curl --verbose --header "Authorization: Bearer secret-token-22" http://localhost:5000/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
> Authorization: Bearer secret-token-22
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: text/html; charset=utf-8
< Content-Length: 19
< WWW-Authenticate: Bearer realm="Authentication Required"
< Server: Werkzeug/1.0.1 Python/3.8.3
< Date: Fri, 25 Sep 2020 03:45:44 GMT
< 
* Closing connection 0
Unauthorized Access
```

```
~ $ curl --verbose --header "Authorization: Bearer secret-token-2" http://localhost:5000/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
> Authorization: Bearer secret-token-2
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 28
< Server: Werkzeug/1.0.1 Python/3.8.3
< Date: Fri, 25 Sep 2020 03:45:52 GMT
< 
{"message":"Hello, susan!"}
* Closing connection 0
```