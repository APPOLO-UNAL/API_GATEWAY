# Prerequisites

Before getting started, make sure you have the following prerequisites:

- Ensure that the following ports are available:
    - 8080
    - 80
    - 81
    - 9200
    - 8082
    - 8000
    - 5000

- Download and update (pull) the following repositories:
    - [appolo_ag_rp](https://github.com/APPOLO-UNAL/appolo_ag_rp)
    - [comments_ms](https://github.com/APPOLO-UNAL/comments_ms)
    - [music_ms](https://github.com/APPOLO-UNAL/music_ms)
    - [usersocial_ms](https://github.com/APPOLO-UNAL/usersocial_ms)

# Docker Compose Setup

To set up the project using Docker Compose, follow these steps:

1. Make sure you have Docker installed on your system.

2. Open a terminal and navigate to the project directory.

3. Run the following command to start the containers:
     ```
     docker-compose up -d
     ```

# Restarting Docker Compose

To restart Docker Compose, follow these steps:

1. Open a terminal and navigate to the project directory.

2. Run the following command to stop the containers:
     ```
     docker-compose down
     ```

3. Run the following command to remove the images (except for Elasticsearch):
     ```
     docker rmi image_id
     ```

     Replace `image_id` with the actual ID of each image you want to remove, except for Elasticsearch.

4. After removing the images, you can start the containers again using the Docker Compose setup steps mentioned above.
