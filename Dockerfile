FROM python:3.11-slim

RUN echo "j'utilise le python 3.11"

WORKDIR /app

RUN echo "definit le repetoire de travail"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "copier tous les element necessaire"

RUN pip install -r requirements.txt

RUN pip install pydantic[email]

RUN echo "installer les dependances"

EXPOSE 8000

RUN echo "exposer le port d'ecoute"

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

RUN echo "demarrer l'api"


