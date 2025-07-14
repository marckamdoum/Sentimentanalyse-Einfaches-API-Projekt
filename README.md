# Sentimentanalyse-Einfaches-API-Projekt
Dieses Projekt demonstriert eine einfache Sentimentanalyse-Anwendung mit einer API-Schnittstelle. ✅ Backend (API-Server) – Entwickelt mit FastAPI, stellt eine REST-API zur Verfügung, die Text entgegennimmt und eine einfache Sentimentbewertung zurückgibt (positiv, negativ, neutral).  ✅ Client (Python-Skript) – Sendet Texte per POST-Anfrage an den Server und gibt die Analyseergebnisse aus.
# Technologien
Python 3.12+

FastAPI

Uvicorn (Server)

Requests (Client)
# schnellstar
Backend starten:
uvicorn app:app --reload --port 8000
Client ausführen:
python client.py
Schwagger-Dokumentation (API-Doku):
http://localhost:8000/docs

# Screenshot
<img width="975" height="510" alt="image_sentimentanalyse" src="https://github.com/user-attachments/assets/56c03966-b255-412f-8f9c-647263fe024c" />
