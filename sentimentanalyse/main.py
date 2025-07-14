
from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

# Importiere die Konfigurationen
from config import logger, APP_TITLE

# Erstelle die FastAPI-Instanz mit Titel und Beschreibung
app = FastAPI(
    title=APP_TITLE,
    description="Eine einfache API zur Sentimentanalyse von Texten.",
    version="1.0.0"
)


class TextInput(BaseModel):
    text: str



@app.get("/")
async def root(): # Nachricht zur Bestätigung, dass die API online ist.
    logger.debug("Root-Endpunkt wurde aufgerufen (Health Check).")
    return {"message": "Sentiment Analysis API ist online und bereit."}


@app.post("/analyze")
async def analyze_sentiment(input: TextInput):# Analysiert den übergebenen Text und gibt Polarität und Sentiment zurück.
    logger.info(f"Anfrage für Analyse erhalten. Text: '{input.text}'")

    try:
        blob = TextBlob(input.text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "positiv"
        elif polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "negativ"

        result = {"polarity": round(polarity, 4), "sentiment": sentiment}
        logger.info(f"Analyse abgeschlossen. Ergebnis: {result}")
        return result

    except Exception as e:
        logger.error(f"Ein Fehler ist bei der Analyse aufgetreten: {e}", exc_info=True)
        return {"error": "Bei der Verarbeitung ist ein interner Fehler aufgetreten."}


# Diese Log-Meldung wird einmal geschrieben, wenn der Server startet.
logger.info(f"FastAPI-Anwendung '{APP_TITLE}' wurde geladen und ist bereit, Anfragen zu empfangen.")
