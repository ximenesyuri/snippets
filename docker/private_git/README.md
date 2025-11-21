# About

How to use private github repositories via ssh without exposing the ssh key in the image log. 

# Usage

1. Pick the `Dockerfile` and the `docker-compose.yml` and modify according your needs.
2. Execute the build as follows: 

```bash
DOCKER_BUILDKIT=1 SSH_PRIVATE_KEY="$(base64 -w0 $HOME/.ssh/id_ed25519)" docker compose up --build
```

# Tips

If using in a CI pipeline, store the `base64` version of the key in the git provider secrets and use it directly.
