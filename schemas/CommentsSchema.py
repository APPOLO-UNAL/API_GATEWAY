import typing
import strawberry
import datetime
from utilities import *
from server import COMMENTS_URL_BASE,USERSOCIAL_URL_BASE
from ms_types.CommentsTypes import *


@strawberry.type
class QueryComment:
    
    @strawberry.field
    def comment(self, id: str) -> Comment:
        comment = generalRequest(f"{COMMENTS_URL_BASE}comments/{id}", GET)
        userId = comment["userId"]
        user = generalRequest(f"{USERSOCIAL_URL_BASE}user/?uid={str(userId)}", GET)
        comment["userName"] = user.get("userName", "unknow")
        comment["picture"] = user.get("picture", "https://static.vecteezy.com/system/resources/thumbnails/020/765/399/small/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg")
        return comment
    @strawberry.field
    def replies(self, parentId: str) -> typing.List[Comment]:
        replies = generalRequest(f"{COMMENTS_URL_BASE}comments/{parentId}/replies", GET)
        print(f"{COMMENTS_URL_BASE}comments/{parentId}/replies")
        print("xd")
        for reply in replies:
            userId = reply["userId"]
            user = generalRequest(f"{USERSOCIAL_URL_BASE}user/?uid={str(userId)}", GET)
            reply["userName"] = user.get("userName", "unknow")
            reply["picture"] = user.get("picture", "https://static.vecteezy.com/system/resources/thumbnails/020/765/399/small/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg")
        return replies
    @strawberry.field
    def comments(self)->typing.List[Comment]: 
        comments=generalRequest(f"{COMMENTS_URL_BASE}comments/",GET)
        for comment in comments:
            userId=comment["userId"]
            user=generalRequest(f"{USERSOCIAL_URL_BASE}user/?uid={str(userId)}",GET)
            comment["userName"] = user.get("userName", "unknow")
            comment["picture"] = user.get("picture", "https://static.vecteezy.com/system/resources/thumbnails/020/765/399/small/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg")

        return comments
    @strawberry.field
    def commentsByFollowed(self,userIdList:typing.List[str])->typing.List[Comment]: 
        userIds = "&".join(f"userId={userId}" for userId in userIdList)
        print(userIds)
        comments = generalRequest(f"{COMMENTS_URL_BASE}comments/followed/?{userIds}", GET)
        for comment in comments:
            userId=comment["userId"]
            user=generalRequest(f"{USERSOCIAL_URL_BASE}user/?uid={str(userId)}",GET)
            comment["userName"] = user.get("userName", "unknow")
            comment["picture"] = user.get("picture", "https://static.vecteezy.com/system/resources/thumbnails/020/765/399/small/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg")

        return comments
    @strawberry.field
    def itemComments(self,itemMusicId:str)->typing.List[Comment]:
        return generalRequest(f"{COMMENTS_URL_BASE}item/{itemMusicId}/comments",GET)
    @strawberry.field
    def userComments(self,userId:str)->typing.List[Comment]:
        comments= generalRequest(f"{COMMENTS_URL_BASE}user/{userId}/comments",GET)
        for comment in comments:
            userId=comment["userId"]
            user=generalRequest(f"{USERSOCIAL_URL_BASE}user/?uid={str(userId)}",GET)
            comment["userName"] = user.get("userName", "unknow")
            comment["picture"] = user.get("picture", "https://static.vecteezy.com/system/resources/thumbnails/020/765/399/small/default-profile-account-unknown-icon-black-silhouette-free-vector.jpg")
        return comments
    @strawberry.field
    def average(self,id:str)->str:
        average = generalRequest(f"{COMMENTS_URL_BASE}av/{id}/",GET)
        return average
    

    
    
    
    
@strawberry.type
class MutationsComment:

    @strawberry.mutation
    def updateComment(self,id:str,comment:CommentUpdate) -> Comment:
        return generalRequest(f"{COMMENTS_URL_BASE}comments/{id}",PATCH,body=strawberry.asdict(comment))
    
    @strawberry.mutation
    def createComment(self,comment:CommentInput) ->typing.Optional[Comment]:
        try:
            if not userExists(comment.userId):  raise Exception("The user doesnt exist")
            createdComment=generalRequest(f"{COMMENTS_URL_BASE}comments/",POST,body=strawberry.asdict(comment))
            if("message" in createdComment):    raise Exception(createdComment["message"])
            return createdComment
        except Exception as e:
            return e
    @strawberry.mutation
    def replyComment(self,parentId:str,reply:ReplyInput) -> Comment:
        parentComment=generalRequest(f"{COMMENTS_URL_BASE}comments/{parentId}",GET)
        if(parentComment): #Validate if the comment to be replied actually exists
            reply.itemMusicId=parentComment["itemMusicId"]
            reply.parentId=parentId
            return generalRequest(f"{COMMENTS_URL_BASE}comments/{parentId}",POST,body=strawberry.asdict(reply))
        else:
            raise Exception("Comment to be replied doesn't exits")
    @strawberry.mutation
    def deleteComment(self,id:str) -> DeleteCommentResponse:
        response=generalRequest(f"{COMMENTS_URL_BASE}comments/{id}",DELETE)
        return response
    @strawberry.mutation
    def likeComment(self,idComment:str,reaction:ReactInput)->Comment:
            if not userExists(reaction.userIdLike):   raise Exception("The user doesnt exist")
            if not commentExists(idComment): raise Exception("The comment doesnt exist")
            return generalRequest(f"{COMMENTS_URL_BASE}comments/{idComment}/likes",PATCH,body=strawberry.asdict(reaction))

    @strawberry.mutation
    def dislikeComment(self,idComment:str,reaction:ReactInput)->Comment:
            if not userExists(reaction.userIdLike):  raise Exception("The user doesnt exist")
            if not commentExists(idComment): raise Exception("The comment doesnt exist")
            return generalRequest(f"{COMMENTS_URL_BASE}comments/{idComment}/dislikes",PATCH,body=strawberry.asdict(reaction))