# Setup

(This has been developed using Python 3.8.3.)
Open a terminal, navigate into a directory of your choice, clone this repository, and
run:
```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
(venv) $ deactivate
```

# Example: basic authentication

1. Open a terminal, navigate into the project directory, and run:
```
$ source venv/bin/activate
$ export FLASK_APP=example_basic_authentication.py
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

3. Close the second terminal; run `deactivate` in the first terminal, and close it

# Example: token authentication

1. Open a terminal, navigate into the project directory, and run:
```
$ source venv/bin/activate
$ export FLASK_APP=example_token_authentication.py
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

3. Close the second terminal; run `deactivate` in the first terminal, and close it

# Example: JWS token authentication

1. Open a terminal, navigate into the project directory, and run:
```
$ source venv/bin/activate
$ export FLASK_APP=example_token_jws_authentication.py
$ flask run
```

2. Open a second terminal window, and run:
```
NB: The following commands must be executed within 120 seconds of step 1!

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
< Date: Fri, 25 Sep 2020 13:09:57 GMT
< 
* Closing connection 0
Unauthorized Access
```

```
NB: The following commands must be executed within 120 seconds of step 1!

~ $ export TOKEN=<anything_different_from_the_two_tokens_printed_in_the_first_terminal>
~ $ curl --verbose --header "Authorization: Bearer $TOKEN" http://localhost:5000/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
> Authorization: Bearer eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMTAzOTM4NCwiZXhwIjoxNjAxMDM5NTA0fQ.eyJpZCI6MX0.Lr_zzv7k2XfsPW_MmBoyCm3PXxKUtaFeGrshu18xw2Y7ajhsk_8BCueV-ZmuqE8pEgnIxNdtX_lGgM5sHZOoG
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: text/html; charset=utf-8
< Content-Length: 19
< WWW-Authenticate: Bearer realm="Authentication Required"
< Server: Werkzeug/1.0.1 Python/3.8.3
< Date: Fri, 25 Sep 2020 13:10:14 GMT
< 
* Closing connection 0
```

```
NB: The following commands must executed within 120 seconds of step 1!

~ $ export TOKEN=<the_first_of_the_two_tokens_printed_in_the_first_terminal>
~ $ curl --verbose --header "Authorization: Bearer $TOKEN" http://localhost:5000/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
> Authorization: Bearer eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMTAzOTM4NCwiZXhwIjoxNjAxMDM5NTA0fQ.eyJpZCI6MX0.Lr_zzv7k2XfsPW_MmBoyCm3PXxKUtaFeGrshu18xw2Y7ajhsk_8BCueV-ZmuqE8pEgnIxNdtX_lGgM5sHZOoGQ
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/1.0.1 Python/3.8.3
< Date: Fri, 25 Sep 2020 13:10:29 GMT
< 
{"message":"Hello, john!"}
* Closing connection 0
```

```
NB: The following commands must be executed at least 120 seconds after step 1!

~ $ export TOKEN=<the_first_of_the_two_tokens_printed_in_the_first_terminal>
~ $ curl --verbose --header "Authorization: Bearer $TOKEN" http://localhost:5000/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
> Authorization: Bearer eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMTAzOTM4NCwiZXhwIjoxNjAxMDM5NTA0fQ.eyJpZCI6MX0.Lr_zzv7k2XfsPW_MmBoyCm3PXxKUtaFeGrshu18xw2Y7ajhsk_8BCueV-ZmuqE8pEgnIxNdtX_lGgM5sHZOoGQ
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: text/html; charset=utf-8
< Content-Length: 19
< WWW-Authenticate: Bearer realm="Authentication Required"
< Server: Werkzeug/1.0.1 Python/3.8.3
< Date: Fri, 25 Sep 2020 13:12:18 GMT
< 
* Closing connection 0
```

3. Close the second terminal; run `deactivate` in the first terminal, and close it