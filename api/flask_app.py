

def create_app():
    pass



if __name__ == '__main__':
    # the following app.run just only for develop env
    # you should run app by 'gunicorn -c gunicorn.conf.py wsgi' command in production env
    app = create_app()
    # add CORS support
    CORS(app, allow_headers='*', origins='*')
    app.run(host='0.0.0.0', port=55666, threaded=True, debug=True)
    # swagger UI: http://0.0.0.0:55666/v1/ui/