# Image de base Python
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exposer le port utilisé par ton app.py
EXPOSE 5001

# Commande de démarrage
CMD ["python", "app.py"]
