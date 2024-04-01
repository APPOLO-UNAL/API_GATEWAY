import strawberry
from ms_types.UserSocialTypes import User, UserInput, UserDeleteInput, UserUpdateInput, FollowInput, FollowResponse


@strawberry.type
class AuthToken:
    token: str
    user: User  

@strawberry.type
class AuthError:
    message: str
