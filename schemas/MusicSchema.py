import typing
import strawberry
import datetime
from utilities import *
from server import MUSIC_URL_BASE
from ms_types.MusicTypes import *

#Types
@strawberry.type
class QueryMusic:
        
    @strawberry.field
    def tracksByArtistByName(self,idArtist:str,idTrack:str)-> Response:
        return generalRequest(MUSIC_URL_BASE+"music/tracks/artist?track={0}&artist={1}".format(idTrack,idArtist),GET)
    
    @strawberry.field
    def tracks(self)->typing.List[Response]:
        response = generalRequest(MUSIC_URL_BASE+"music/tracks",GET)
        return response
    
    @strawberry.field
    def tracksByName(self,idTrack:str)-> typing.List[Response]:
        return generalRequest(MUSIC_URL_BASE+"music?name={0}".format(idTrack),GET)
    
    @strawberry.field
    def tracksByIdTrack(self,id:str)-> ResponseId:
        return generalRequest(MUSIC_URL_BASE+"id?album={0}".format(id),GET)
    
    @strawberry.field
    def artistByIdArtist(self,id:str)->ResponseId:
        return generalRequest(MUSIC_URL_BASE+"id?artist={0}".format(id),GET)

    @strawberry.field
    def tracksByAlbum(self,idAlbum:str)-> Response:
        return generalRequest(MUSIC_URL_BASE+"music?name={0}".format(idAlbum),GET)
    
    @strawberry.field
    def tracksByPopularity(self,start:str,end:str)-> typing.List[Response]:
        return generalRequest(MUSIC_URL_BASE+"music/artist/popularity?start={0}&end={1}".format(start,end),GET)
    
    @strawberry.field
    def tracksByDate(self,start:str,end:str)-> typing.List[Response]:
        return generalRequest(MUSIC_URL_BASE+"music/artist/releasedate?start={0}&end={1}".format(start,end),GET)