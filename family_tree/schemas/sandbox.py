from marshmallow import fields, post_load, Schema, validates, ValidationError


class Sandbox(Schema):
    id = fields.Int(dump_only=True)
    relation_type = fields.Str(required=True)
    relation_id = fields.Int(required=True)

    @post_load
    def sandbox_post_lost(self, data):
        import pdb; pdb.set_trace()
        pass


person_item_schema = PersonSchema(many=False)
person_list_schema = PersonSchema(many=True)
