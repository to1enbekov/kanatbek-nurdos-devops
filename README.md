# Kanatbek Nurdos — DevOps Fundamentals Lab (Week 6)

**Student:** Nurdos Kanatbek | **Group:** IT2-2310 | **Student ID:** 37253

Project for the Linux → Git → GitHub → Docker → Jenkins laboratory work.

## Application

A minimal Python HTTP service (no third-party Python packages) prints student information on startup and serves it at `http://localhost:8000/`; health endpoint: `/health`.

```bash
python3 -m unittest discover -s tests -v
python3 app/main.py
```

## Docker

```bash
docker build -t kanatbek-nurdos-devops .
docker run -d --name kanatbek-nurdos-container -p 8000:8000 -e STUDENT_NAME=Nurdos -e STUDENT_SURNAME=Kanatbek -e STUDENT_GROUP=IT2-2310 -e STUDENT_ID=37253 kanatbek-nurdos-devops
docker logs kanatbek-nurdos-container
curl http://localhost:8000/health
```

To run Compose instead, stop and remove the manually created container first, then use `docker compose up -d --build` and `docker compose down`.

## Jenkins

`Jenkinsfile` contains five required stages: Checkout, Build, Test, Docker Build and Docker Run. Read `docs/SETUP_GUIDE_RU.md` before configuring Jenkins.

## Documentation

- `docs/SETUP_GUIDE_RU.md`: preparation, meaningful commits, GitHub, Docker and Jenkins.
- `docs/VIDEO_SCRIPT_RU.md`: screen demonstration with Russian narration.
- `docs/REPORT_TEMPLATE_RU.md`: draft report structure; insert authentic screenshots before submission.

`.gitignore` excludes logs, backup, `.env` and private demo files.
## Development checks

Run automated tests before merging changes:
python3 -m unittest discover -s tests -v
