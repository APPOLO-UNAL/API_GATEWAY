import strawberry
import typing
@strawberry.type
class Rating:
    _id: str
    user_ID: str
    rate: int
    item_ID:str
    date: str

@strawberry.input
class RatingInput:
    user_ID: str
    rate: str
    item_ID: str

@strawberry.input
class RatingUpdate:
    rate: str
