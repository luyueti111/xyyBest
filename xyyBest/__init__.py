import os

from flask import Flask
from xyyBest.settings import config

from xyyBest.blueprints.project import project_bp
from xyyBest.extensions import mail, db


def creat_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask("xyyBest")
    app.config.from_object(
        config[config_name]
    )

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_shell_context(app)
    register_template_context(app)

    return app


def register_logging(app):
    pass


def register_extensions(app):
    db.init_app(app)
    mail.init_app(app)


def register_blueprints(app):
    app.register_blueprint(project_bp, url_prefix='/project')


def register_shell_context(app):
    @app.shell_context_processors
    def mail_context():
        return dict(db=db)


def register_template_context(app):
    pass


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(error):
        return '400'


def register_commands(app):
    pass
