FROM python:3.11-slim

WORKDIR /app

# Install system deps for typical Python packages (adjust if your requirements need more)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Ensure local pip installs are on PATH
ENV PATH="/root/.local/bin:${PATH}"

EXPOSE 8501

ENV STREAMLIT_SERVER_HEADLESS=true

CMD ["streamlit", "run", "app/app.py", "--server.port", "8501", "--server.headless", "true"]
