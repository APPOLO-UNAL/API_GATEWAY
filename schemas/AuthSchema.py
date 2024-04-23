import strawberry
from utilities import generalRequest
from ms_types.AuthTypes import AuthToken, AuthError, UserAuth

AUTH_MS_BASE_URL = "http://localhost:3000/api/v1"

# Define the union for the login result which can either be AuthToken or AuthError
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

        # Handling the response based on the assumed successful status code and structure
        if response.get('status_code', 400) in [200, 201]:  # Checks for successful HTTP status codes
            user_data = response.get('data', {}).get('user')
            if user_data:
                return AuthToken(
                    token=user_data.get('token'),  # Assuming token is part of the user data in the response
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
            # Error handling based on the API's error message or a default message
            error_message = response.get('message', 'Failed to authenticate with the provided credentials.')
            return AuthError(message=error_message)
