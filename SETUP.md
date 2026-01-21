# Setup — Install Docker and prepare a registry

Follow these steps before starting the exercise.

## 1) Install Docker

- Windows
  - Install Docker Desktop: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
  - Requirements: WSL 2 and virtualization enabled (Docker Desktop installer helps configure this)
  - Verify in a new terminal (PowerShell): `docker --version`

- macOS
  - Install Docker Desktop: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
  - Verify: `docker --version`

- Linux (Ubuntu/Debian)
  - Follow official docs: [docs.docker.com/engine/install/ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  - After install, add your user to the `docker` group (optional):
    - `sudo usermod -aG docker $USER` then sign out/in
  - Verify: `docker --version`

## 2) Verify your installation

- Run: `docker run hello-world`
- You should see a message that Docker is working.

## 3) Optional: Create a registry account

- Docker Hub: [hub.docker.com](https://hub.docker.com/)
- OR GitHub Container Registry (GHCR): [docs.github.com/packages](https://docs.github.com/packages)

You can complete Tasks 1–5 without logging into a registry. Task 6 (push) requires an account and login.
