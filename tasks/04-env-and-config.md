# Task 4 — Environment variables

Goal: change the app message without editing the code by passing an environment variable.

Steps:

1) In the `starter` folder, run the container with `APP_MESSAGE` set:\
   `docker run --rm -p 8080:5000 -e APP_MESSAGE="Hello from ENV" myapp:v1`
2) Open or refresh [http://localhost:8080](http://localhost:8080) and see the new message.

Hints:

- Stop the container with Ctrl+C.
- Try different messages and ports. The `-e` flag means “add this environment variable to the container.”
