import strawberry
import typing
@strawberry.type
class User:
    uid: str
    emailAddr: str
    userName: str
    nickname: str
    keyIdAuth: str
    description: str
    picture : str
    favArtists: typing.Optional[typing.List[str]]
    favAlbums: typing.Optional[typing.List[str]]
    favSongs: typing.Optional[typing.List[str]]
    favPlaylists: typing.Optional[typing.List[str]]
    pinnedComm: typing.Optional[typing.List[str]]
@strawberry.type
class UserDeleteResponse:
    success: str  
@strawberry.type
class FollowResponse:
    result: typing.Optional[bool]
# Input Types  
@strawberry.input
class UserInput:
    emailAddr: str
    userName: str
    nickname: str
    keyIdAuth: str
    description: str
    picture : str
@strawberry.input
class UserDeleteInput:
    userName: str
@strawberry.input
class UserUpdateInput:
    nickname: str
    description: str
    picture: str
    favArtists: typing.Optional[typing.List[str]]=None
    favAlbums: typing.Optional[typing.List[str]]=None
    favSongs: typing.Optional[typing.List[str]]=None
    favPlaylists: typing.Optional[typing.List[str]]=None
    pinnedComm: typing.Optional[typing.List[str]]=None
@strawberry.input
class FollowInput:
    uid1: str
    uid2: str

@strawberry.type
class UserFollowers:
    followers: typing.Optional[typing.List[str]]=None

@strawberry.type
class FollowersCount:
    followers: str

@strawberry.type
class UserFollowing:
    following: typing.Optional[typing.List[str]]=None

@strawberry.type
class FollowingCount:
    following: str