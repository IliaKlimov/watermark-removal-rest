## Create python virtual environment and activate it

<div class="termy">

```console
$ python -m venv venv

$ . venv/bin/activate
```

</div>

## Install requirements

<div class="termy">

```console
$ pip install -r requirements.txt
```

</div>


## Run app

Run the server with:

<div class="termy">

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>