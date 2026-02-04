# Jagodanki

Portfolio dziennikarskie Jagody Skorupy.

## Uruchomienie (venv)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Otwórz http://127.0.0.1:5000

## Uruchomienie (Docker)

```bash
docker build -t jagodanki .
docker run -p 5000:5000 jagodanki
```

Otwórz http://127.0.0.1:5000

## Technologie

- Python / Flask
- Jinja2
- CSS (custom properties, bez frameworków)
