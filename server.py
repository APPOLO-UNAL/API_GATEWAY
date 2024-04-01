
# Split the URL into base and endpoint
base_url = "localhost"
base_endpoint = "api/v1" 

# Now you can use base_url, endpoint, and port in your code
comments_port="8080"
userSocial_port="8000"
rating_port="8081"
music_port="8080"
COMMENTS_URL_BASE="http://{0}:{1}/{2}/".format(base_url,comments_port,base_endpoint)
USERSOCIAL_URL_BASE="http://{0}:{1}/{2}/".format(base_url,userSocial_port,base_endpoint)
RATING_URL_BASE="http://{0}:{1}/{2}/".format(base_url,rating_port,base_endpoint)
MUSIC_URL_BASE="http://{0}:{1}/{2}/".format(base_url,music_port,base_endpoint)

