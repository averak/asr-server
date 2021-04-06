import os
from flask import Flask

from webapi import predict


def create_app(test_config=None) -> Flask:
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        ALLOWED_EXTENSIONS=('wav'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.after_request
    def add_header(res):
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res

    @app.route('/')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(predict.bp, url_prefix='/predict')

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule('/', endpoint='index')

    return app
