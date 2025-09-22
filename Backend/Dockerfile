FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    texlive-latex-base texlive-latex-extra texlive-fonts-recommended \
    && apt-get clean

WORKDIR /app


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY main.py .
COPY src/ ./src/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

