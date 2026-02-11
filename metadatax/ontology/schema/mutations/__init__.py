from graphene import ObjectType

from .source import PostSourceMutation, DeleteSourceMutation
from .sound import PostSoundMutation, DeleteSoundMutation

__all__ = [
    'OntologyMutation'
]


class OntologyMutation(ObjectType):
    # Source
    post_source = PostSourceMutation.Field()
    delete_source = DeleteSourceMutation.Field()
    # Sound
    post_sound = PostSoundMutation.Field()
    delete_sound = DeleteSoundMutation.Field()
