from .person import PersonSchema
from .relationship import RelationshipSchema

person_item_schema = PersonSchema(many=False)
person_list_schema = PersonSchema(many=True)

relationship_item_schema = RelationshipSchema(many=False)
