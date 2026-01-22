# Docker Basics: Mini Exercise (45–60 min)

Build and run a tiny web app while learning the most common Docker actions: images, containers, ports, volumes, environment variables, logs, and pushing to a registry.

Audience: High school students and first-time Docker users. No prior Docker experience required.

## Setup

If you don't have Docker or a registry account yet, start with [SETUP.md](SETUP.md).

## What you'll practice

- Building an image from a Dockerfile (the recipe for a container)
- Running containers and mapping ports so you can open the app in a browser
- Using volumes (bind mounts) to share files between your laptop and the container
- Passing environment variables to change app behavior without editing code
- Viewing logs and cleaning up old containers/images
- Tagging and pushing an image to a registry (optional)

## Quick start

0) Finish [SETUP.md](SETUP.md) if you haven't yet.
1) Clone or fork this repo to your computer.
2) Open the tasks one by one in order:
   - tasks/01-install-and-verify.md
   - tasks/02-build-and-run.md
   - tasks/03-volumes.md
   - tasks/04-env-and-config.md
   - tasks/05-logs-and-cleanup.md
   - tasks/06-tag-and-push.md (optional)
3) Keep notes or take screenshots of what you run.

## Repo structure

- starter/ — a tiny web app with a Dockerfile
- tasks/ — step-by-step instructions for each concept
- CHECKLIST.md — quick self-check list

## Submission

- Share the commands you ran and your image name/tags.
- If you pushed to a registry, include the link to your image page.

## Teacher notes

See teacher-guide.md for a rubric and suggested walkthrough.
