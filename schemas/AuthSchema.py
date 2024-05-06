import strawberry
from utilities import generalRequest
from ms_types.AuthTypes import AuthToken, AuthError, UserAuth

AUTH_MS_BASE_URL = "http://localhost:3000/api/v1"

LoginResult = strawberry.union("LoginResult", types=(AuthToken, AuthError))

@strawberry.type
class MutationsAuth:
    @strawberry.mutation
    def login(self, email: str, password: str) -> LoginResult: # type: ignore
        payload = {
            "user": {
                "email": email,
                "password": password
            }
        }
        response = generalRequest(f"{AUTH_MS_BASE_URL}/sign_in", "POST", body=payload)

        if not response:
            return AuthError(message="No response from the server or connection error.")

        if response.get('status_code', 400) in [200, 201]:  
            user_data = response.get('data', {}).get('user')
            if user_data:
                return AuthToken(
                    token=user_data.get('token'),  
                    user=UserAuth(
                        id=str(user_data.get('id')),
                        email=user_data.get('email'),
                        created_at=user_data.get('created_at'),
                        updated_at=user_data.get('updated_at'),
                        nickname=user_data.get('nickname', None),
                        keyIdAuth=user_data.get('keyIdAuth', None)
                    )
                )
            else:
                return AuthError(message="User data not found in the response.")
        else:
            error_message = response.get('message', 'Failed to authenticate with the provided credentials.')
            return AuthError(message=error_message)

    @strawberry.mutation
    def signup(self, email: str, password: str, nickname: str) -> LoginResult: # type: ignore
        payload = { 
            "user": {
                "email": email,
                "password": password,
                "nickname": nickname
            }
        }
        response = generalRequest(f"{AUTH_MS_BASE_URL}/sign_up", "POST", body=payload)

        if not response:
            return AuthError(message="No response from the server or connection error.")

        if response.get('status_code', 400) in [200, 201]:  
            user_data = response.get('user')  
            if user_data:
                return AuthToken(
                    token=None, 
                    user=UserAuth(
                        id=str(user_data.get('id')),
                        email=user_data.get('email'),
                        created_at=user_data.get('created_at'),
                        updated_at=user_data.get('updated_at'),
                        nickname=user_data.get('nickname', None),
                        keyIdAuth=user_data.get('keyIdAuth', None)
                    )
                )
            else:
                return AuthError(message="User data not found in the response.")
        else:
            error_message = response.get('message', 'Failed to register. Please try again.')
            return AuthError(message=error_message)
