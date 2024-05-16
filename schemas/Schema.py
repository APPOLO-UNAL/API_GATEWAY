import strawberry
from .CommentsSchema import MutationsComment, QueryComment
from .UserSocialSchema import MutationsUserSocial, QueryUserSocial
from .MusicSchema import QueryMusic
from .AuthSchema import MutationsAuth  

@strawberry.type
class Query(QueryComment,QueryUserSocial,QueryMusic):
    pass

@strawberry.type
class Mutation(MutationsComment,MutationsUserSocial, MutationsAuth):
    pass


#types