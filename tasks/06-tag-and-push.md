# Task 6 — Tag and push (optional)

Goal: give your image a name that includes your username and push it to an online registry.

Prerequisite: a Docker Hub account (or GHCR permissions) and login.

Steps (Docker Hub example):

1) Log in: `docker login`
2) Tag your image with your username (format: `username/repo:tag`):\
   `docker tag myapp:v1 <your-username>/myapp:1.0`
3) Push the tagged image:\
   `docker push <your-username>/myapp:1.0`
4) Open [hub.docker.com](https://hub.docker.com/) and find your image page.

Optional (GHCR):

- Tag: `docker tag myapp:v1 ghcr.io/<your-username>/myapp:1.0`
- Login: `echo <TOKEN> | docker login ghcr.io -u <your-username> --password-stdin`
- Push: `docker push ghcr.io/<your-username>/myapp:1.0`

Hints:

- If the push is denied, double-check the tag format and that you are logged in.
- Use `docker logout` to sign out when you are done.
