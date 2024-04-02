from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from strawberry.schema.config import StrawberryConfig
from schemas.Schema import Query, Mutation
import operator
from ms_types.AuthTypes import AuthError  # Import AuthError for type checking

app = FastAPI()

def default_resolver(root, field):
    # Check if root is an instance of AuthError and handle it specifically
    if isinstance(root, AuthError):
        if field == "message":
            return root.message
        else:
            # Handle other fields or raise an error if necessary
            raise AttributeError(f"AuthError does not have a field named {field}")
    try:
        return operator.getitem(root, field)
    except KeyError:
        return getattr(root, field)

config = StrawberryConfig(default_resolver=default_resolver)

schema = strawberry.Schema(query=Query, mutation=Mutation, config=config)

app.add_route("/graphql", GraphQL(schema, debug=True))

@app.get("/")
def index():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
