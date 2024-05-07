from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from schemas.Schema import Query, Mutation
from strawberry.schema.config import StrawberryConfig
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body = await request.body()
        print(f"Request: {request.method} {request.url}")
        print(f"Headers: {request.headers}")
        print(f"Body: {body.decode()}")
        response = await call_next(request)
        return response


import operator
from ms_types.AuthTypes import AuthError 
from starlette.requests import Request

import logging
app = FastAPI()

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body = await request.body()
        print(f"Request: {request.method} {request.url}")
        print(f"Headers: {request.headers}")
        print(f"Body: {body.decode()}")
        response = await call_next(request)
        return response



@strawberry.type
class AuthError:
    message: str

    def __getitem__(self, item):
        try:
            return getattr(self, item)
        except AttributeError:
            raise KeyError(f"{item} is not a valid attribute of {type(self).__name__}")

def default_resolver(root, field):
    logging.debug(f"Resolver called with root type: {type(root)}, field: {field}")
    if isinstance(root, AuthError):
        if field == "message":
            return root.message
        else:
            raise AttributeError(f"AuthError does not have a field named {field}")
    else:  # Modified section
        try:
            return operator.getitem(root, field)
        except AttributeError:
            raise AttributeError(f"{type(root)} does not have a field named {field}") 



config = StrawberryConfig(
    default_resolver=default_resolver,
)

schema = strawberry.Schema(query=Query, mutation=Mutation, config=config)

app=FastAPI()
app.add_middleware(LogMiddleware)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def index(): 
    return {"error":"Wrong url, go to /graphql"}
app.add_route("/graphql",GraphQL(schema,debug=True))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)