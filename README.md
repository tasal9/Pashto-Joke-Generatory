# Pashto Joke Generator

[![Python Tests](https://github.com/tasal9/Pashto-Joke-Generatory/actions/workflows/python-tests.yml/badge.svg)](https://github.com/tasal9/Pashto-Joke-Generatory/actions)

Simple static Pashto joke generator with a small Python utility and tests.

Files of interest:

- `index.html` — frontend UI (Pashto) that loads `jokes.json` and shows a random joke.
- `jokes.json` — an array of joke objects (single or twopart).
- `static/js/scripts.js` — frontend logic.
- `generator.py` — small Python helper to pick a random joke.
- `tests/run_tests.py` — lightweight test runner using plain asserts.

How to run (static site):

1. Start a simple HTTP server from the project root:

```bash
python -m http.server 8000
```

2. Open `http://localhost:8000` in your browser and click the button to get Pashto jokes.

How to run tests:

```bash
python tests/run_tests.py
```

Notes:

- All code uses the Python standard library — no external dependencies required.
- If you'd like `pytest`, install it and convert the tests accordingly.

Live Demo (GitHub Pages)
-------------------------

After enabling GitHub Pages in repository settings and pointing it to the `main` branch (root), the site will be available at:

```
https://tasal9.github.io/Pashto-Joke-Generatory/
```

If you prefer I can enable Pages via the CLI, but it may require additional repository permissions.
# Pashto Joke Generator

Simple static Pashto joke generator with a small Python utility and tests.

Files of interest:

- `index.html` — frontend UI (Pashto) that loads `jokes.json` and shows a random joke.
- `jokes.json` — an array of joke objects (single or twopart).
- `static/js/scripts.js` — frontend logic.
- `generator.py` — small Python helper to pick a random joke.
- `tests/run_tests.py` — lightweight test runner using plain asserts.

How to run (static site):

1. Start a simple HTTP server from the project root:

```bash
python -m http.server 8000
```

2. Open `http://localhost:8000` in your browser and click the button to get Pashto jokes.

How to run tests:

```bash
python tests/run_tests.py
```

Notes:

- All code uses the Python standard library — no external dependencies required.
- If you'd like `pytest`, install it and convert the tests accordingly.
