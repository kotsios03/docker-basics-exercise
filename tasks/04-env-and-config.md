# Task 4 — Environment variables

Goal: Change the app message using an environment variable.

Steps:

1) In the `starter` folder, run the container with `APP_MESSAGE` set:
   - `docker run --rm -p 8080:5000 -e APP_MESSAGE="Hello from ENV" myapp:v1`
2) Refresh [http://localhost:8080](http://localhost:8080) and observe the new message.

Hints:

- Stop the container with Ctrl+C
- Try different messages and ports
