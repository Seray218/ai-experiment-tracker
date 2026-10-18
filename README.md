
# AI Experiment Tracker API

A lightweight REST API built with **FastAPI** for tracking and managing machine learning experiments.
%100 handmade:)

This project focuses on API development, input validation, UUID-based identification, and automated testing.

## Features

- Create machine learning experiment records
- Retrieve all experiments or find one by UUID
- Partially update experiments using PATCH
- Delete experiments
- Automatic UUID generation
- Input validation with Pydantic
- HTTP error handling
- Interactive Swagger UI documentation
- Automated API tests with Pytest

## Tech Stack

- **Python**
- **FastAPI** — REST API framework
- **Pydantic** — Data validation
- **Uvicorn** — ASGI server
- **Pytest** — Automated testing
- **HTTPX** — HTTP testing support

## Project Structure

```text
ai-experiment-tracker/
├── api.py
├── test_api.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Seray218/ai-experiment-tracker.git
cd ai-experiment-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the API

Start the development server:

```bash
uvicorn api:api --reload
```

Open Swagger UI:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/experiments/` | Create an experiment |
| GET | `/experiments/` | List all experiments |
| GET | `/experiments/{experiment_id}` | Retrieve an experiment by UUID |
| PATCH | `/experiments/{experiment_id}` | Partially update an experiment |
| DELETE | `/experiments/{experiment_id}` | Delete an experiment |

## Example Request

### POST /experiments/

```json
{
  "model_name": "RandomForest",
  "dataset": "Iris",
  "accuracy": 0.95,
  "status": "completed"
}
```

Example response:

```json
{
  "model_name": "RandomForest",
  "dataset": "Iris",
  "accuracy": 0.95,
  "status": "completed",
  "id": "550e8400-e29b-41d4-a716-446655440000"
}
```

The API automatically generates a unique UUID for each experiment.

### Experiment Status

Supported values:

- `pending`
- `running`
- `completed`
- `failed`

Accuracy values must be between `0.0` and `1.0`.

## Automated Testing

Run the tests with:

```bash
python -m pytest -v
```

The project includes **5 automated tests** covering:

1. Successful experiment creation
2. Invalid accuracy validation
3. Experiment retrieval by UUID
4. Partial experiment updates
5. Experiment deletion

## Current Limitations

- Experiments are stored in an in-memory Python list.
- Records are lost when the server restarts.
- The API tracks experiment metadata but does not perform actual model training.
- Authentication and persistent database storage are not yet implemented.

## Future Improvements

- PostgreSQL database integration
- Authentication and authorization
- ML model serving
- Docker deployment
- CI/CD integration

## Author

Developed by [Seray218](https://github.com/Seray218).
