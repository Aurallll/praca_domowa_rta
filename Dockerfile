# Wybieramy oficjalny obraz Pythona jako bazę
FROM python:3.11-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki do kontenera
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Otwieramy port, z którego korzysta Flask
EXPOSE 5000

# Uruchamiamy aplikację
CMD ["python", "app.py"]
