# Blackboard

A Python-based blackboard application built with Flask.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following content:
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///blackboard.db
```

4. Run the application:
```bash
python run.py
```

The application will be available at http://localhost:5000

## Project Structure

```
blackboard/
├── blackboard/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       ├── base.html
│       └── index.html
├── tests/
├── .env
├── pyproject.toml
├── requirements.txt
└── run.py
```

## Development

- Use `black` for code formatting
- Use `isort` for import sorting
- Use `flake8` for linting
- Write tests using `pytest`

## Testing

Run tests with:
```bash
pytest
```