# Task 6 — Tag and push (optional)

Goal: Tag your image and push it to a registry.

Prerequisite: A Docker Hub account or GHCR permissions and login.

Steps (Docker Hub example):

1) Log in: `docker login`
2) Tag your image with your username: `docker tag myapp:v1 <your-username>/myapp:1.0`
3) Push: `docker push <your-username>/myapp:1.0`
4) View your image at [hub.docker.com](https://hub.docker.com/)

Optional (GHCR):

- Tag: `docker tag myapp:v1 ghcr.io/<your-username>/myapp:1.0`
- Login: `echo <TOKEN> | docker login ghcr.io -u <your-username> --password-stdin`
- Push: `docker push ghcr.io/<your-username>/myapp:1.0`

Hints:

- If push is denied, double-check the tag and login
- Use `docker logout` to sign out
