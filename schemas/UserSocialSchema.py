import strawberry
import typing
from utilities import *
from ms_types.UserSocialTypes import *
from ms_types.AuthTypes import User, UserInput, UserDeleteInput, UserUpdateInput, FollowInput, FollowResponse
from server import USERSOCIAL_URL_BASE

@strawberry.type
class QueryUserSocial:
    @strawberry.field
    def users(self) ->typing.List[User]:
        return generalRequest(USERSOCIAL_URL_BASE+"getAllUsers",GET)
    @strawberry.field
    def user(self,id: str)->User:
        return  generalRequest(USERSOCIAL_URL_BASE+"user/?uid={}".format(id),GET)
    @strawberry.field
    def userByEmail(self,email:str)->User:
        return  generalRequest(USERSOCIAL_URL_BASE+"user/?emailAddr={}".format(email),GET)
    @strawberry.field
    def userByUserName(self,userName:str)->User:
        return  generalRequest(USERSOCIAL_URL_BASE+"user/?userName={}".format(userName),GET)
@strawberry.type
class MutationsUserSocial:
    @strawberry.mutation
    def createUser(self,user:UserInput)->User:
        return generalRequest(USERSOCIAL_URL_BASE+"user/",POST,body=strawberry.asdict(user))
    @strawberry.mutation
    def deleteUser(self,user:UserDeleteInput)->UserDeleteResponse:
        return generalRequest(USERSOCIAL_URL_BASE+"user/",DELETE,body=strawberry.asdict(user))
    @strawberry.mutation
    def updateUser(self,id:str,user:UserUpdateInput)->User:
        return generalRequest(USERSOCIAL_URL_BASE+"user/?uid={}".format(id),PUT,body=strawberry.asdict(user))
    @strawberry.mutation
    def updateUserByEmail(self,email:str,user:UserUpdateInput)->User:
        return generalRequest(USERSOCIAL_URL_BASE+"user/?emailAddr={}".format(email),PUT,body=strawberry.asdict(user))
    @strawberry.mutation
    def updateUserByUserName(self,userName:str,user:UserUpdateInput)->User:
        return generalRequest(USERSOCIAL_URL_BASE+"user/?userName={}".format(userName),PUT,body=strawberry.asdict(user))
    
    @strawberry.mutation
    def follow(self,users:FollowInput)->FollowResponse:
        return generalRequest(USERSOCIAL_URL_BASE+"follow/",PUT,body=strawberry.asdict(users))
    @strawberry.mutation
    def unfollow(self,users:FollowInput)->FollowResponse:
        return generalRequest(USERSOCIAL_URL_BASE+"follow/",PUT,body=strawberry.asdict(users))