FROM python:3.10-slim

WORKDIR /app

# Install system deps (if needed)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY main.py ./

# Copy artifacts and model (ensure you copy correct paths)
# If you're building locally, copy pre-saved artifacts into the image:
# COPY /path/to/processed /mnt/data/processed
# COPY loan_best_model.joblib /app/loan_best_model.joblib

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]