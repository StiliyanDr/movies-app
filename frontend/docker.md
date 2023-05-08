# Docker commands for frontend app

Open a terminal and run the following commands.  

```bash
(movies-app) $ cd frontend

# Build the image (using a Debian parent image)
(movies-app/frontend) $ docker build -t movies-app-frontend:vN .

# Make sure the envs are up to date
(movies-app/frontend) $ vi envs
# ...

# Running on a development server (not really a production server)
# Note: network already created with
#   docker network create my-net
(movies-app/frontend) $ docker run --name frontend -d \
                                   -p 5050:8080 \
                                   --env-file envs \
                                   --network my-net \
                                   movies-app-frontend:vN
```
