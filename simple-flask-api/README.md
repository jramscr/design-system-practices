# Simple Flask API

A containerized application demonstrating API communication between a Flask server and a Python client using Docker Compose.

## Overview

This project consists of two services that communicate over a Docker bridge network:

- **Server**: A Flask API that serves JSON responses
- **Client**: A Python script that polls the server every 2 seconds

## Project Structure

```
simple-flask-api/
├── docker-compose.yml    # Docker Compose configuration
├── server/
│   └── app.py           # Flask server application
└── client/
    └── app.py           # Client polling script
```

## Services

### Server

- **Host Port**: 5002 (mapped from container port 5000)
- **Container Port**: 5000
- **Framework**: Flask
- **Endpoint**: `GET /`
- **Response**: `{"message": "Hello, Flask!"}`

The server runs a simple Flask application that responds to GET requests with a JSON message.

### Client

- **Port**: 5001 (exposed but not actively used)
- **Behavior**: Continuously polls the server every 2 seconds
- **Target**: `http://server:5002/` (uses Docker service name for internal communication)

The client makes HTTP GET requests to the server and prints the JSON response. It includes error handling for connection issues.

## Docker Configuration

- **Python Version**: 3.9-slim
- **Network**: bridge-network (bridge driver)
- **Dependencies**: Client service depends on server service

## Usage

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Start both services:
   ```bash
   docker-compose up
   ```

2. View logs to see the client polling the server:
   ```bash
   docker-compose logs -f client
   ```

3. Test the server directly:
   ```bash
   curl http://localhost:5002/
   ```

### Stopping the Application

```bash
docker-compose down
```

## Notes

- The client runs in an infinite loop, polling the server every 2 seconds
- Both services run in debug mode
- The services communicate over a Docker bridge network

