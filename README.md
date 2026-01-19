# Music App API

A minimalistic FastAPI application with a health check endpoint.

## Features

- ✅ Health check endpoint with status and timestamp
- ✅ Automatic interactive API documentation
- ✅ Fast and lightweight
- ✅ Music search powered by Deezer API

## Requirements

- Python 3.8+
- Conda or pip

## Installation

### Option 1: Using Conda (Recommended)

1. Navigate to the project directory:
```bash
cd music-app
```

2. Create a new conda environment:
```bash
conda create -n music-app python=3.11
```

3. Activate the environment:
```bash
conda activate music-app
```

4. Install FastAPI and Uvicorn:
```bash
conda install fastapi uvicorn
```

### Option 2: Using pip

1. Navigate to the project directory:
```bash
cd music-app
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at:
- **Application**: http://localhost:8000
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc

## API Endpoints

### Root Endpoint

**Endpoint:** `GET /`

**Description:** Returns an interactive psychedelic music search interface with Deezer API integration.

**Response:** HTML page with music search functionality

### Music Search

**Endpoint:** `GET /api/search`

**Description:** Search for music using the Deezer API.

**Query Parameters:**
- `q` (required): Search query (song, artist, or album name)

**Response:**
```json
{
  "data": [
    {
      "title": "Song Title",
      "artist": {
        "name": "Artist Name",
        "picture_big": "https://..."
      },
      "preview": "https://...",
      "album": {
        "cover_big": "https://..."
      }
    }
  ]
}
```

### Health Check

**Endpoint:** `GET /health`

**Description:** Returns the application health status and current timestamp.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-01-19T09:48:50.656Z"
}
```

**Example using curl:**
```bash
curl http://localhost:8000/health
```

**Example using Python:**
```python
import requests

response = requests.get("http://localhost:8000/health")
print(response.json())
```

## Project Structure

```
music-app/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Development

To run with auto-reload on code changes:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Production Deployment

For production, run without the `--reload` flag:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## License

MIT