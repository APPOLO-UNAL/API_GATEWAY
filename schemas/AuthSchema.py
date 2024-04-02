import strawberry
from typing import Union
from utilities import generalRequest
from server import AUTH_URL_BASE
from ms_types.AuthTypes import AuthToken, AuthError, User

AUTH_MS_BASE_URL = "http://localhost:3000/api/v1"

@strawberry.type
class MutationsAuth:
    @strawberry.mutation
    def login(self, email: str, password: str) -> Union[AuthToken, AuthError]:
        # This mutation attempts a login and expects user details in response if successful
        payload = {"email": email, "password": password}
        response = generalRequest(f"{AUTH_MS_BASE_URL}/sign_in", "POST", body=payload)
        
        if 'error' in response or not response.get('success'):
            return AuthError(message=response.get('message', 'Unexpected error occurred'))
        
        user_info = response.get('user', {})
        if user_info:
            return AuthToken(
                token="YourTokenHere",  # Placeholder for actual token handling if implemented as devise is used
                user=User(
                    id=user_info.get('id'),
                    email=user_info.get('email'),
                    created_at=user_info.get('created_at'),
                    updated_at=user_info.get('updated_at'),
                    nickname=user_info.get('nickname'),
                    keyIdAuth=user_info.get('keyIdAuth'),
                )
            )
        else:
            return AuthError(message="User information not found in response")
