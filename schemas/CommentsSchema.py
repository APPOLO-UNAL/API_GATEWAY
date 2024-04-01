import typing
import strawberry
import datetime
from utilities import *
from server import COMMENTS_URL_BASE,USERSOCIAL_URL_BASE
from ms_types.CommentsTypes import *


@strawberry.type
class QueryComment:
    
    @strawberry.field
    def comment(self,id:str)-> Comment:
        return generalRequest(f"{COMMENTS_URL_BASE}comments/{id}",GET)
    @strawberry.field
    def replies(self,parentId:str)->typing.List[Comment]:
        return generalRequest(f"{COMMENTS_URL_BASE}comments/{parentId}/replies",GET)
    
    @strawberry.field
    def comments(self)->typing.List[Comment]:
        return generalRequest(f"{COMMENTS_URL_BASE}comments/",GET)
    @strawberry.field
    def itemComments(self,itemMusicId:str)->typing.List[Comment]:
        return generalRequest(f"{COMMENTS_URL_BASE}item/{itemMusicId}/comments",GET)
    @strawberry.field
    def userComments(self,userId:str)->typing.List[Comment]:
        return generalRequest(f"{COMMENTS_URL_BASE}user/{userId}/comments",GET)
    
    
    
    
@strawberry.type
class MutationsComment:

    @strawberry.mutation
    def updateComment(self,id:str,comment:CommentUpdate) -> Comment:
        return generalRequest(f"{COMMENTS_URL_BASE}comments/{id}",PATCH,body=strawberry.asdict(comment))
    
    @strawberry.mutation
    def createComment(self,comment:CommentInput) ->typing.Optional[Comment]:
        try:
            userId=comment.userId
            user=generalRequest(f"{USERSOCIAL_URL_BASE}user/?uid={userId}",GET)
            if("error" in user):
                raise Exception("The user doesnt exist")
            createdComment=generalRequest(f"{COMMENTS_URL_BASE}comments/",POST,body=strawberry.asdict(comment))
            if("message" in createdComment):
                raise Exception(createdComment["message"])
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
    