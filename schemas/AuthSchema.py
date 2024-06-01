import strawberry
from utilities import generalRequest
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
from ms_types.AuthTypes import AuthToken, AuthError, UserAuth

AUTH_MS_BASE_URL = "http://auth_ms:3000/api/v1"
LDAP_SERVER = 'ldap://appolo-ldap:389'
LDAP_PORT = 389
LDAP_USER = 'cn=admin,dc=arqsoft,dc=unal,dc=edu,dc=co'
LDAP_PASSWORD = 'admin'


server = Server(LDAP_SERVER, port=LDAP_PORT, get_info=ALL)

LoginResult = strawberry.union("LoginResult", types=(AuthToken, AuthError))
@strawberry.type
class MutationsAuth:
    @strawberry.mutation
    def signup(self, email: str, password: str, nickname: str) -> LoginResult: # type: ignore
        # Connect to LDAP
        conn = Connection(server, user=LDAP_USER, password=LDAP_PASSWORD, auto_bind=True)
        
        # Define DN and attributes
        dn = f"cn={nickname},ou=users,dc=arqsoft,dc=unal,dc=edu,dc=co"
        attributes = {
            'objectClass': ['inetOrgPerson', 'top'],
            'cn': nickname,
            'sn': nickname,
            'mail': email,
            'userPassword': password
        }

        # Add user to LDAP
        if not conn.add(dn, attributes=attributes):
            return AuthError(message="Failed to create user in LDAP.")

        # If you need to interact with another auth service as well, do it here
        payload = { 
            "user": {
                "email": email,
                "password": password,
                "nickname": nickname
            }
        }
        response = generalRequest(f"{AUTH_MS_BASE_URL}/sign_up", "POST", body=payload)

        if response and "error" not in response:
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
        else:
            error_message = response.get('error', 'Failed to communicate with the authentication service.')
            return AuthError(message=error_message)