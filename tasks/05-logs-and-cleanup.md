# Task 5 — Logs and cleanup

Goal: read container logs and clean up containers/images you no longer need.

Steps:

1) List running containers: `docker ps`
2) View container logs (replace name/ID): `docker logs myapp1`\
   (Logs show the printouts your app makes while running.)
3) Stop a container: `docker stop myapp1`
4) Remove a container: `docker rm myapp1`
5) List images: `docker images`
6) Remove an image (replace tag): `docker rmi myapp:v1`
7) Clean up unused resources (stopped containers, dangling images, etc.): `docker system prune`

Hints:

- Use `docker ps -a` to see stopped containers too.
- `docker rm -f` forces removal of a running container—be careful.
- Read the prompt before confirming `docker system prune` so you know what will be removed.
