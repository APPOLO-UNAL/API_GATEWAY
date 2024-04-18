import strawberry
import typing

#types
@strawberry.type
class ExternalUrls:
    spotify: str

@strawberry.type
class Images:
    height: int
    width: int
    url: str

@strawberry.type
class Album:
    album_type: str
    total_tracks: int
    external_urls: ExternalUrls
    id: str
    imagesFr: typing.List[Images]=None
    name: str
    release_date: str
    release_date_precision: str

@strawberry.type
class Followers:
    href: str
    total: int

@strawberry.type
class Artists:
    ExternalUrls: ExternalUrls
    id: str
    name: str
    Followers: Followers
    genres: typing.List[str]=None
    Images: typing.List[Images]=None
    popularity: int

@strawberry.type
class Items:
    album: Album=None
    artists: typing.List[Artists]=None
    external_urls: ExternalUrls=None

@strawberry.type
class track:
    href: str
    total: int
    items: typing.List[Items]=None

@strawberry.type
class Albums:
    href: str
    total: int
    items: typing.List[Items]=None

@strawberry.type
class Response:
    tracks: track
    albums: typing.List[Albums]
