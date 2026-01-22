# Task 2 — Build and run the app

Goal: build a Docker image and start a container you can view in the browser.

Steps:

1) Change into the `starter` folder: `cd starter`
2) Build the image (makes `myapp:v1` from the Dockerfile—`v1` is just a version label you pick):\
   `docker build -t myapp:v1 .`
3) Run the container and map your laptop’s port 8080 to the app’s port 5000:\
   `docker run --name myapp1 -p 8080:5000 myapp:v1`
4) Open [http://localhost:8080](http://localhost:8080) in a browser. You should see the greeting.

Hints:

- If 8080 is busy, change the first number, e.g., `-p 8081:5000`.
- Stop the container with Ctrl+C (if it is in the foreground) or `docker stop myapp1` (if it is running in the background).
