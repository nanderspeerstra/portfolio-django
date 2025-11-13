# Portfolio & Gallery Website (Django)

A personal portfolio and image gallery built with Django. This site showcases your work, photography, and personal projects with a clean, responsive design and admin-managed media uploads.

---

## Features

- Personal portfolio homepage
- Categorized image gallery (professional & personal)
- Admin interface for uploading and managing photos
- Static assets organized with vendor libraries
- Pre-commit hooks for code quality
- Docker-ready for deployment
- GitHub Actions for CI/CD

---

## Tech Stack

- Backend: Django 4.x
- Frontend: HTML, SCSS, JS (vanilla)
- Database: SQLite (default, can be swapped)
- CI/CD: GitHub Actions
- Containerization: Docker

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/nanderdev/portfolio-gallery.git
cd portfolio-gallery
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start development server

```bash
python manage.py runserver
```

---

## Code Quality

This project uses Pre-Commit with:

- black for formatting
- ruff and flake8 for linting
- detect-secrets for secret scanning
- djlint for Django template hygiene

To run hooks manually:

```bash
pre-commit run --all-files
```

---

## Docker

Build and run the app with Docker:

```bash
docker build -t portfolio .
docker run -p 8000:8000 portfolio
```

---

## Secrets & Environment

Create a `.env` file based on `.env.example`:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## Media & Static Files

- Uploaded images are stored in `/media/` (excluded from Git)
- Static assets are in `/static/`, including vendor libraries

---

## Deployment

Automated via GitHub Actions:

- CI: Pre-commit and Django tests on PRs
- CD: Docker image pushed on release
- Release PRs managed with Release Please

---

## License

This project is licensed under the MIT License.

---

## Author

Made by Nander
Portfolio: https://nander.dev
GitHub: https://github.com/nanderdev
