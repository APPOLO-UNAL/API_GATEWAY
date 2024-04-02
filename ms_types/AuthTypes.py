import strawberry
from ms_types.UserSocialTypes import User, UserInput, UserDeleteInput, UserUpdateInput, FollowInput, FollowResponse

@strawberry.type
class UserAuth:
    id: strawberry.ID
    email: str
    created_at: str
    updated_at: str
    nickname: str
    keyIdAuth: str

@strawberry.type
class AuthToken:
    token: str
    user: UserAuth  

@strawberry.type
class AuthError:
    message: str
