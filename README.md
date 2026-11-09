AI Chat API

A Python chatbot backend built with FastAPI and Uvicorn.

Technology Stack

Python 3.12+

FastAPI

Uvicorn

uv

Docker

Docker Compose

Project Structure

ai-chat-api/
|-- src/
|   |-- ai_chat_api/
|       |-- __init__.py
|       |-- main.py
|-- .dockerignore
|-- .env.example
|-- .gitignore
|-- Dockerfile
|-- compose.yaml
|-- pyproject.toml
|-- uv.lock
|-- README.md

Prerequisites

For local development:

Python 3.12+

uv

For containerized development:

Docker Desktop

Docker Compose

Local Setup

Install dependencies:

uv sync

Create a local environment file:

Copy-Item .env.example .env

Start the development server:

uv run uvicorn ai_chat_api.main:app --env-file .env --reload

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

Health endpoint:

http://127.0.0.1:8000/health

Docker Setup

Build and start the application:

docker compose up --build

Stop the application:

docker compose down

API Endpoints

Method

Endpoint

Description

GET

/health

Application health check

Environment Variables

Variable

Description

Default

APP_ENV

Application environment

development

APP_VERSION

Application version

0.1.0