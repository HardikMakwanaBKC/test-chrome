# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Chrome dependencies (needed for headless Chrome)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    libx11-dev \
    libx11-xcb1 \
    libxcb1 \
    libdbus-1-3 \
    libfontconfig1 \
    libxrender1 \
    libxext6 \
    libnss3 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libappindicator3-1 \
    libnss3-dev \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome WebDriver (ensure the correct version based on your Chrome version)
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get -y --fix-broken install

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
