import threading
from flask_cors import CORS


from flask import Flask, request
from fluentd_client import FluentdClient



def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def send_to_fluentd():
        '''
        '["sel", "dmesg"]'
        '''
        log_type_list = request.get_json()
        threads = []
        n_thread = len(log_type_list)
        fluentd_client = FluentdClient()
        for i in range(n_thread):
            threads.append(threading.Thread(
                target=fluentd_client.send_logs, args=[log_type_list[i], ]))
            threads[i].start()
        return "200"
    return app


if __name__ == '__main__':
    # the following app.run just only for develop env
    # you should run app by 'gunicorn -c gunicorn.conf.py wsgi' command in production env
    app = create_app()
    # add CORS support
    CORS(app, allow_headers='*', origins='*')
    app.run(host='0.0.0.0', port=55666, threaded=True, debug=True)
    # swagger UI: http://0.0.0.0:55666/v1/ui/

# ====================== Debug =======================================
# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def send_to_fluentd():
#     '''
#     '["sel", "dmesg"]'
#     '''
#     log_type_list = request.get_json()
#     threads = []
#     n_thread = len(log_type_list)
#     fluentd_client = FluentdClient()
#     for i in range(n_thread):
#         threads.append(threading.Thread(
#             target=fluentd_client.send_logs, args=[log_type_list[i], ]))
#         threads[i].start()
#     return app

# if __name__ == '__main__':
#     # the following app.run just only for develop env
#     # you should run app by 'gunicorn -c gunicorn.conf.py wsgi' command in production env
#     app.run()
# =================================================================
