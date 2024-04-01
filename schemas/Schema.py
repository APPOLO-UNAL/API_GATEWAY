import strawberry
from .RatingSchema import QueryRating,MutationsRating
from .CommentsSchema import MutationsComment,QueryComment
from .UserSocialSchema import MutationsUserSocial,QueryUserSocial
from .MusicSchema import QueryMusic
@strawberry.type
class Query(QueryComment,QueryRating,QueryUserSocial,QueryMusic):
    pass

@strawberry.type
class Mutation(MutationsComment,MutationsRating,MutationsUserSocial):
    pass