FROM python:3.11
WORKDIR /app
RUN pip install fastapi uvicorn streamlit yt_dlp
CMD ["streamlit", "run", "main.py"]
