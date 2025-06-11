# Video Downloader Project

This project is a full-stack application for downloading videos from various platforms. It consists of the following components:

## Technology Overview
| Component                | Technology       | Purpose                                      |
|--------------------------|------------------|----------------------------------------------|
| Frontend                 | Next.js          | User interface and API routes               |
| Backend Downloader       | Python (FastAPI) | Video downloading and processing            |
| Containerization         | Docker           | Containerized deployment of all services    |

## Project Structure
- `backend-python-downloader/`: Python backend for video downloading.
- `docker/`: Docker setup for containerization.
- `frontend-nextjs/`: Next.js frontend application.

## Running the Project
1. **Setup Docker**:
   - Build and start the containers:
     ```bash
     docker-compose up --build
     ```
   - Access the services:
     - Frontend: `http://localhost:3000`
     - Python Downloader: `http://localhost:8000`

2. **Run Services Individually** (Optional):
   - Follow the setup instructions in each component's `README.md` file.
