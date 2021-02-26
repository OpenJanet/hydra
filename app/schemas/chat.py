from marshmallow import fields, Schema


class ChatSchema(Schema):
    message = fields.String()
