from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from schemas.Schema import Query, Mutation
from strawberry.schema.config import StrawberryConfig
import operator
from ms_types.AuthTypes import AuthError 
import logging

app = FastAPI()

@strawberry.type
class AuthError:
    message: str

    @strawberry.field
    def message(self) -> str:
        return self.message

def default_resolver(root, field):
    logging.debug(f"Resolver called with root type: {type(root)}, field: {field}")
    if isinstance(root, AuthError):
        if field == "message":
            return root.message
        else:
            raise AttributeError(f"AuthError does not have a field named {field}")
    else:  # Modified section
        try:
            return getattr(root, field)  # Use getattr here 
        except AttributeError:
            raise AttributeError(f"{type(root)} does not have a field named {field}") 



config = StrawberryConfig(
    default_resolver=default_resolver,
)

schema = strawberry.Schema(query=Query, mutation=Mutation, config=config)

app.add_route("/graphql", GraphQL(schema, debug=True))

@app.get("/")
def index():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
