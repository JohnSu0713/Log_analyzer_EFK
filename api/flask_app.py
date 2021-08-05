import threading
import sys

from flask import Flask, request
from lib.fluentd_client import *
sys.path.append("..")


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def send_to_fluentd(log_type_list):
        '''
        { "type": "sel, dmesg" }
        '''
        types = request.json["type"]
        log_type_list = types.split(", ")
        threads = []
        n_thread = len(log_type_list)
        fluentd_client = FluentdClient()
        for i in range(n_thread):
            threads.append(threading.Thread(
                target=fluentd_client.send_logs, args=[log_type_list[i], ]))
            threads[i].start()
    return app


if __name__ == '__main__':
    # the following app.run just only for develop env
    # you should run app by 'gunicorn -c gunicorn.conf.py wsgi' command in production env
    app = create_app()
    # add CORS support
    CORS(app, allow_headers='*', origins='*')
    app.run(host='0.0.0.0', port=55666, threaded=True, debug=True)
    # swagger UI: http://0.0.0.0:55666/v1/ui/

