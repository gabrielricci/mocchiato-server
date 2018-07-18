#!flask/bin/python
from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'PATCH'])
@app.route('/<path:full_path>', methods=["GET", "POST", "PUT", "PATCH"])
def index(full_path=None):
    sleep_time = int(request.args.get('sleep', 600))
    if sleep_time > 0:
        time.sleep(sleep_time)

    return request.get_data()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
