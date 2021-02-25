import requests

from flask import Flask, jsonify, request
from flask_rebar import Rebar
from flask_rebar import errors
from marshmallow import fields, Schema


rebar = Rebar()
registry = rebar.create_handler_registry(prefix='/api')


def create_app() -> Flask:
    app = Flask(__name__)
    rebar.init_app(app)
    return app
