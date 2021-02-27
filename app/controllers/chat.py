import requests
import os

from flask_rebar import errors

from app.app import registry
from app.app import rebar
from app.schemas.chat import ChatSchema


@registry.handles(rule="/chat", method="POST", request_body_schema=ChatSchema())
def post_chat():
    # TODO: Do not use dockers internal host.
    chat = rebar.validated_body
    resp = requests.post(os.getenv('JANET_URL',
                         'http://localhost:5005/webhooks/rest/webhook'),
                         json=chat)

    return resp.json()[0]
