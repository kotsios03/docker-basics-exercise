# Task 3 — Volumes (bind mounts)

Goal: See local files inside the container using a bind mount.

Steps:

1) In the `starter` folder, create a folder named `data` and a file `note.txt`
2) Run the container with a bind mount from `starter/data` to `/app/data`:
   - Windows PowerShell: `docker run --rm -v ${PWD}/data:/app/data myapp:v1 python -c "import os; print(os.listdir('/app/data'))"`
   - macOS/Linux: `docker run --rm -v $(pwd)/data:/app/data myapp:v1 python -c "import os; print(os.listdir('/app/data'))"`
3) You should see `note.txt` listed from inside the container.

Hints:

- On Windows CMD, use `%cd%` instead of `${PWD}`
- You can also start the web app and mount the folder: `-v ${PWD}/data:/app/data`
