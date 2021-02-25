import requests

from flask import Flask, jsonify, request
from flask_rebar import Rebar
from flask_rebar import errors
from marshmallow import fields, Schema


rebar = Rebar()
registry = rebar.create_handler_registry(prefix='/api')

app = Flask(__name__)


def create_app() -> Flask:
    app = Flask(__name__)
    rebar.init_app(app)
    return app


class HealthSchema(Schema):
    status = fields.String()


@registry.handles(rule='/health', method="GET", marshal_schema=HealthSchema())
def get_health():
    return {"status": "OK"}


if __name__ == '__main__':
    create_app().run()
