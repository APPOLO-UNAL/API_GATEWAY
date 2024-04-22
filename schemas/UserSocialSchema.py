import strawberry
import typing
from utilities import *
from ms_types.UserSocialTypes import *
from server import USERSOCIAL_URL_BASE,COMMENTS_URL_BASE
@strawberry.type
class QueryUserSocial:
    @strawberry.field
    def users(self) ->typing.List[User]:
        return generalRequest(f"{USERSOCIAL_URL_BASE}getAllUsers", GET)
    @strawberry.field
    def user(self,id: str)->User:
        return  generalRequest(f"{USERSOCIAL_URL_BASE}user/?uid={id}",GET)
    @strawberry.field
    def userByEmail(self,email:str)->User:  
        return  generalRequest(f"{USERSOCIAL_URL_BASE}user/?emailAddr={email}",GET)
    @strawberry.field
    def userByUserName(self,userName:str)->User:
        return  generalRequest(f"{USERSOCIAL_URL_BASE}user/?userName={userName}",GET)
    @strawberry.field
    def followers(self,id:str)->Followers:
        return generalRequest(f"{USERSOCIAL_URL_BASE}followers/?uid={id}",GET)
    @strawberry.field
    def followersCount(self,id:str)->Followers:
        return generalRequest(f"{USERSOCIAL_URL_BASE}followsCount/?uid={id}",GET)
    @strawberry.field
    def following(self,id:str)->Following:
        return generalRequest(f"{USERSOCIAL_URL_BASE}following/?uid={id}",GET)
    @strawberry.field
    def followingCount(self,id:str)->Following:
        return generalRequest(f"{USERSOCIAL_URL_BASE}followingCount/?uid={id}",GET)
    

@strawberry.type
class MutationsUserSocial:
    @strawberry.mutation
    def createUser(self,user:UserInput)->User:
        return generalRequest(f"{USERSOCIAL_URL_BASE}user/",POST,body=strawberry.asdict(user))
    @strawberry.mutation
    def deleteUser(self,user:UserDeleteInput)->UserDeleteResponse:
        try:
            userObj=generalRequest(f"{USERSOCIAL_URL_BASE}user/?userName={user.userName}",GET)
            if("error" in userObj):
                raise Exception("User doesnt exist")
            userId=userObj["uid"]
            generalRequest(f"{COMMENTS_URL_BASE}user/{userId}/comments",DELETE) #Delete the comments made by the user
            return generalRequest(f"{USERSOCIAL_URL_BASE}user/",DELETE,body=strawberry.asdict(user))
        except Exception as e:
            return e
    @strawberry.mutation
    def updateUser(self,id:str,user:UserUpdateInput)->User:
        return generalRequest(f"{USERSOCIAL_URL_BASE}user/?uid={id}",PUT,body=strawberry.asdict(user))
    @strawberry.mutation
    def updateUserByEmail(self,email:str,user:UserUpdateInput)->User:
        return generalRequest(f"{USERSOCIAL_URL_BASE}user/?emailAddr={email}",PUT,body=strawberry.asdict(user))
    @strawberry.mutation
    def updateUserByUserName(self,userName:str,user:UserUpdateInput)->User:
        return generalRequest(f"{USERSOCIAL_URL_BASE}user/?userName={userName}",PUT,body=strawberry.asdict(user))
    
    @strawberry.mutation
    def follow(self,users:FollowInput)->FollowResponse:
        return generalRequest(f"{USERSOCIAL_URL_BASE}follow/",PUT,body=strawberry.asdict(users))
    @strawberry.mutation
    def unfollow(self,users:FollowInput)->FollowResponse:
        return generalRequest(f"{USERSOCIAL_URL_BASE}unfollow/",PUT,body=strawberry.asdict(users))