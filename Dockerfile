# Stage 1: Build dependencies
FROM python:3.12-slim AS build

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Stage 2: Runtime
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from build stage
COPY --from=build /usr/local /usr/local

# Copy project files
COPY . .

# Collect static files (optional, if you use Django staticfiles)
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run Gunicorn server
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
