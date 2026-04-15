FROM python:3.14-slim

WORKDIR /Frontend

RUN pip install --no-cache-dir streamlit requests

COPY /FRONTEND/ .


CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]