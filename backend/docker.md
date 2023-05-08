# Docker commands for backend app

Open a terminal and run the following commands.  

```bash
(movies-app) $ cd backend

# Build the image (using a Debian parent image)
(movies-app/backend) $ docker build -t movies-app-backend:vN .

# Edit the envs file to provide an actual MongoDB URI
(movies-app/backend) $ vi envs
# ...

# Running on a development Flask server and
# with 'dev' secret key, not really a production server
# Note: network already created with
#   docker network create my-net
(movies-app/backend) $ docker run --name backend -d \
                                  -p 5000:5000 \
                                  --env-file envs \
                                  --network my-net \
                                  movies-app-backend:vN
```
