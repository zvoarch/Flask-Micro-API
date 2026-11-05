# Flask-Micro-API

Two small REST APIs built with Flask, each with a matching client script that calls the API to show it works.

## Project structure

| File | Description |
|------|-------------|
| `flaskWebApp.py` | App 1: a read-only API over a car dataset (`cars.csv`) using pandas. Runs on port **8080**. |
| `client_app.py` | Client for App 1: calls its endpoints and prints the JSON responses. |
| `flaskWebApp2.py` | App 2: an in-memory items API with a health check. Runs on port **5000**. |
| `client_app2.py` | Client for App 2: fetches the item list and prints it. |
| `cars.csv` | Car dataset used by App 1 (205 cars, including `CarName` and `price`). |
| `requirements.txt` | Python dependencies. |

App 2 stores its data in memory: a `DATA` list of campus locations (`id`, `campus`, `lat`, `lon`).

## Setup

```bash
python -m venv .venv
```

Activate the virtual environment:

- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install dependencies:

```bash
pip install -r requirements.txt
```

## App 1: Cars API

Start the server:

```bash
python flaskWebApp.py
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/firstten` | First 10 rows of the car dataset |
| GET | `/manufacturers` | Unique manufacturer names (first word of `CarName`) |
| GET | `/cars/prices` | Every car's name and price |

Test it from a second terminal while the server is running:

```bash
python client_app.py
```

## App 2: Items API

Start the server:

```bash
python flaskWebApp2.py
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | HTML page linking to the routes |
| GET | `/api/health` | Health check, returns `{"status": "ok"}` |
| GET | `/api/items` | All campus items |
| GET | `/api/items/<id>` | One item by ID (404 if not found) |

Example response from `/api/items/1`:

```json
{"id": 1, "campus": "MMC", "lat": 25.7605781, "lon": -80.36934121}
```

Test it from a second terminal while the server is running:

```bash
python client_app2.py
```

## Tech stack

- [Flask](https://flask.palletsprojects.com/): web framework
- [pandas](https://pandas.pydata.org/): CSV loading and data handling (App 1)
- [requests](https://requests.readthedocs.io/): HTTP client for the client scripts
