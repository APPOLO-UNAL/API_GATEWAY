# Split the URL into base and endpoint
base_url = "host.docker.internal"
base_external_url="localhost"
base_endpoint = "api/v1" 

# Now you can use base_url, endpoint, and port in your code
comments_container_name = "comments_ms"
userSocial_container_name="usersocial_ms"
music_container_name="music_ms"
auth_container_name="auth_ms"

comments_port = "8082"
userSocial_port = "8000"
rating_port = "8081"
auth_port = "3000"

music_port="8080"
COMMENTS_URL_BASE = "http://{0}:{1}/{2}/".format(base_url, comments_port, base_endpoint)
USERSOCIAL_URL_BASE = "http://{0}:{1}/{2}/".format(base_url, userSocial_port, base_endpoint)
RATING_URL_BASE = "http://{0}:{1}/{2}/".format(base_url, rating_port, base_endpoint)
AUTH_URL_BASE = "http://{0}:{1}/{2}/".format(base_external_url, auth_port, base_endpoint) 
MUSIC_URL_BASE="http://{0}:{1}/{2}/".format(base_url,music_port,base_endpoint)

#types