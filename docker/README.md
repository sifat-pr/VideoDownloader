# Docker Setup

This folder contains Dockerfiles and docker-compose.yml for containerizing the services.

## Setup
1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```
2. Access the services:
   - Frontend: `http://localhost:3000`
   - API Server: `http://localhost:5000`
   - Python Downloader: `http://localhost:8000`
