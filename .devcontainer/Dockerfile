# .devcontainer/Dockerfile
FROM python:3.12-bookworm

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /workspace

# Copy pyproject.toml and poetry.lock if they exist
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root

# Install Google Chrome and ChromeDriver
RUN apt-get update && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y && \
    wget https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.165/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/bin/chromedriver && \
    chown root:root /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm -f google-chrome-stable_current_amd64.deb chromedriver_linux64.zip

# Copy the rest of the application code
COPY . .