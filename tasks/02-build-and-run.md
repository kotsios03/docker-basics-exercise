# Task 2 — Build and run the app

Goal: Build an image and run a container mapping a port.

Steps:

1) Change into the `starter` folder
2) Build the image:
   - `docker build -t myapp:v1 .`
3) Run the container, mapping host 8080 to container 5000:
   - `docker run --name myapp1 -p 8080:5000 myapp:v1`
4) Open [http://localhost:8080](http://localhost:8080) in a browser to see the message.

Hints:

- If the port is busy, choose another host port, e.g., `-p 8081:5000`
- Stop the container with Ctrl+C (foreground) or `docker stop myapp1` (background)
