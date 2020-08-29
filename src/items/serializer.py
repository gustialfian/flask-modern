from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Integer()
    name = fields.String()


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
