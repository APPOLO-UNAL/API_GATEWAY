import strawberry
from .RatingSchema import QueryRating,MutationsRating
from .CommentsSchema import MutationsComment,QueryComment
from .UserSocialSchema import MutationsUserSocial,QueryUserSocial
@strawberry.type
class Query(QueryComment,QueryRating,QueryUserSocial):
    pass

@strawberry.type
class Mutation(MutationsComment,MutationsRating,MutationsUserSocial):
    pass

#types