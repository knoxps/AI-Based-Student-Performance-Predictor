# Deployment Guide — AI Student Performance Predictor

This document shows simple options to deploy the Streamlit app in this repository.

Prerequisites
- A working Git repository (push to GitHub/GitLab/Bitbucket) for cloud deployments.
- `requirements.txt` must list all Python dependencies used by the app (already present in this repo).

Options

1) Streamlit Community Cloud (recommended for simple public deployments)
---------------------------------------------------------------
- Push your repo to GitHub.
- Go to https://share.streamlit.io and log in with GitHub.
- Click **New app** → choose your repo and branch → set `Main file` to `app/app.py`.
- Click **Deploy**. The platform will use `requirements.txt` and run the app automatically.

Notes:
- No Dockerfile or Procfile required.
- Private repos are supported but may require a subscription.

2) Render.com
----------------
- Create an account at https://render.com and connect your GitHub repo.
- Create a new **Web Service** and select your repository and branch.
- For **Build Command** use:

  pip install -r requirements.txt

- For **Start Command** use:

  streamlit run app/app.py --server.port $PORT --server.headless true

- Render will expose the `PORT` environment variable automatically.

3) Heroku (using Procfile)
--------------------------
- Ensure `Procfile` is present (this repo includes one).
- Push to a Heroku app (create via `heroku create`), then:

  git push heroku main

- Heroku will install from `requirements.txt` and run the command in `Procfile`.

4) Docker (for a VPS or container platform)
-------------------------------------------
- Build the image locally:

  docker build -t student-predictor:latest .

- Run it:

  docker run -p 8501:8501 student-predictor:latest

- For platforms like AWS ECS, DigitalOcean App Platform, Fly.io, or GCP Cloud Run, push the image to a container registry and create the service.

Helpful tips
- Use `--server.headless true` to avoid interactive prompts on the server.
- Use the included `.streamlit/config.toml` to disable usage stats and set headless mode by default.
- If deployment fails due to missing system packages, add them to the `Dockerfile` or specify a `apt-get install` step in the platform's build settings.

Next steps I can take for you
- Create and push a GitHub repository for this project and link it to Streamlit Cloud (you'll need to provide GitHub access).
- Connect and configure Render or Heroku automatically.
- Build and test a Docker image here and run it once to confirm.

Tell me which platform you prefer and I'll proceed with that flow.
