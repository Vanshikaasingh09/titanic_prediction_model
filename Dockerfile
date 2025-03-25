# Use Python as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app.py .
COPY survival_model.pkl .
COPY requirements.txt .

# Install dependencies with correct scikit-learn version
RUN pip install --no-cache-dir -r requirements.txt scikit-learn==1.6.1

# Expose Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
