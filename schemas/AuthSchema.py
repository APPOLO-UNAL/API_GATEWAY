import strawberry
from utilities import generalRequest
from server import AUTH_URL_BASE
from ms_types.AuthTypes import AuthToken, AuthError, UserAuth

AUTH_MS_BASE_URL = "http://localhost:3000/api/v1"

LoginResult = strawberry.union("LoginResult", types=(AuthToken, AuthError))

@strawberry.type
class MutationsAuth:
    @strawberry.mutation
    def login(self, email: str, password: str) -> LoginResult:
        
        payload = {
            "user": {
                "email": email,
                "password": password
            }
        }
        # Make sure to pass full_response=True to get the full response object
        response = generalRequest(f"{AUTH_MS_BASE_URL}/sign_in", "POST", body=payload, full_response=True)
        
        if not response or response.status_code != 200:
            return AuthError(message="Failed to authenticate")

        # Extract the JWT token from the Authorization header
        auth_header = response.headers.get('Authorization')
        if not auth_header:
            return AuthError(message="Authorization token not found in response")

        # Extract the token part if the header is in the format "Bearer <token>"
        token = auth_header.split(" ")[1] if "Bearer" in auth_header else None

        if not token:
            return AuthError(message="JWT token could not be extracted from the Authorization header")

        # Assuming the user information is still part of the response body
        user_info = response.json().get('user', {})
        if user_info:
            return AuthToken(
                token=token,  # Use the extracted token
                user=UserAuth(
                    id=str(user_info.get('id')),
                    email=user_info.get('email'),
                    created_at=user_info.get('created_at'),
                    updated_at=user_info.get('updated_at'),
                    nickname=user_info.get('nickname', ''),
                    keyIdAuth=user_info.get('keyIdAuth', ''),
                )
            )
        else:
            return AuthError(message="User information not found in response")
