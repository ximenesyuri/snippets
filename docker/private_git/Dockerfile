FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        openssh-client \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /services

COPY requirements.txt .

RUN --mount=type=secret,id=ssh_key \
    set -eu; \
    mkdir -p /root/.ssh; \
    chmod 700 /root/.ssh; \
    base64 -d /run/secrets/ssh_key > /root/.ssh/id_ed25519; \
    chmod 600 /root/.ssh/id_ed25519; \
    touch /root/.ssh/known_hosts; \
    ssh-keyscan github.com >> /root/.ssh/known_hosts; \
    GIT_SSH_COMMAND="ssh -i /root/.ssh/id_ed25519 -o StrictHostKeyChecking=yes" \
      pip install --no-cache-dir -r requirements.txt; \
    rm -rf /root/.ssh
