from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from strawberry.schema.config import StrawberryConfig
from schemas.Schema import Query,Mutation
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

def default_resolver(root, field):
    try:
        return operator.getitem(root, field)
    except KeyError:
        return getattr(root, field)

config = StrawberryConfig(
    default_resolver=default_resolver,
)

schema= strawberry.Schema(query=Query,mutation=Mutation,config=config)

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
    return {"mess":"a"}
app.add_route("/graphql",GraphQL(schema,debug=True))
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)