# Local training Jenkins image, with Python and Docker CLI installed.
FROM jenkins/jenkins:lts-jdk21
USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 docker-cli docker-buildx \
    && rm -rf /var/lib/apt/lists/*
USER jenkins
