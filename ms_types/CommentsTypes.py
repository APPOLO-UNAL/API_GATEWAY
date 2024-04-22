import strawberry
import typing
@strawberry.type
class Comment:
    _id: str
    userId: str
    content: str
    parentId: typing.Optional[str]
    itemMusicId:str
    rate: typing.Optional[str]
    itemMusicType: str
    likes: typing.List[str]
    dislikes: typing.List[str]
    userName: str=None
    createdAt: str
    updatedAt: str


@strawberry.input
class CommentUpdate:
    content: str
    rate:int

@strawberry.input
class CommentInput:
    userId: str
    content: str
    rate:int
    itemMusicId: str
    itemMusicType: str

@strawberry.input
class ReplyInput:
    content: str
    userId: str
    itemMusicType: str
    itemMusicId: typing.Optional[str]=None
    parentId: typing.Optional[str]=None
    
@strawberry.input
class ReactInput:
    userIdLike: str
    unReact: typing.Optional[bool]=None

# Response Types
@strawberry.type
class DeleteCommentResponse:
    acknowledged: str
    deletedCount: int

@strawberry.type
class ReactResponse:
    likes: typing.Optional[str]
    dislikes: typing.Optional[str]
