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

### Using Docker (Recommended)
1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```
2. Access the services:
   - Frontend: `http://localhost:3000`
   - Python Downloader: `http://localhost:8000`

### Running Services Individually

#### Frontend (Next.js)
1. Navigate to the `frontend-nextjs` directory:
   ```bash
   cd frontend-nextjs
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
4. Access the frontend at `http://localhost:3000`.

#### Backend (Python Downloader)
1. Navigate to the `backend-python-downloader` directory:
   ```bash
   cd backend-python-downloader
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
4. Access the backend at `http://localhost:8000`.

## Notes
- Ensure Docker is installed and running if using the Docker setup.
- For individual services, ensure Node.js, npm, and Python are installed on your system.
