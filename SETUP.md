# Setup — Install Docker and prepare a registry

Goal: make sure Docker runs on your computer before you start the tasks.

## 1) Install Docker

- Windows
  - Install Docker Desktop: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
  - Requirements: WSL 2 and virtualization enabled (the installer can set these up)
  - Open a new PowerShell window and check: `docker --version`

- macOS
  - Install Docker Desktop: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
  - Check: `docker --version`

- Linux (Ubuntu/Debian)
  - Follow the official guide: [docs.docker.com/engine/install/ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  - Optional: add your user to the `docker` group so you can run Docker without `sudo`:
    - `sudo usermod -aG docker $USER` then sign out/in
  - Check: `docker --version`

## 2) Verify your installation

- Run: `docker run hello-world`
- You should see a short success message. If it fails, make sure Docker Desktop is open and fully started.

## 3) Optional: Create a registry account

- Docker Hub: [hub.docker.com](https://hub.docker.com/)
- OR GitHub Container Registry (GHCR): [docs.github.com/packages](https://docs.github.com/packages)

You can complete Tasks 1–5 without logging into a registry. Task 6 (push) needs an account and login.
