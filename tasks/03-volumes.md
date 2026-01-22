# Task 3 — Volumes (bind mounts)

Goal: share a local folder with the container and prove the container can see it.

Steps:

1) In the `starter` folder, make a folder named `data` and a file `note.txt` inside it (any text is fine).
2) Run the container with a bind mount from `starter/data` to `/app/data`:
   - Windows PowerShell: `docker run --rm -v ${PWD}/data:/app/data myapp:v1 python -c "import os; print(os.listdir('/app/data'))"`
   - macOS/Linux: `docker run --rm -v $(pwd)/data:/app/data myapp:v1 python -c "import os; print(os.listdir('/app/data'))"`
3) You should see `note.txt` printed, which means the container can read your local file.

Hints:

- On Windows CMD, use `%cd%` instead of `${PWD}`.
- A “bind mount” just means “use this local folder inside the container.”
- You can also start the web app and mount the folder: add `-v ${PWD}/data:/app/data` to your `docker run` command.
