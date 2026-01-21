# Task 5 — Logs and cleanup

Goal: Inspect logs and remove unused resources.

Steps:

1) List running containers: `docker ps`
2) View container logs (replace name/ID): `docker logs myapp1`
3) Stop a container: `docker stop myapp1`
4) Remove a container: `docker rm myapp1`
5) List images: `docker images`
6) Remove an image (replace tag): `docker rmi myapp:v1`
7) Clean up unused resources: `docker system prune`

Hints:

- Use `docker ps -a` to see stopped containers
- Use `docker rm -f` to force remove a running container (careful)
