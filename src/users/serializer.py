from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
