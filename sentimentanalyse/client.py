import requests

# Definiert die Basis-URL des lokalen FastAPI-Servers.
localhost = "http://127.0.0.1:8000"

def analyze_text(text: str):
    """
    Sendet einen Text an den /analyze-Endpunkt des FastAPI-Servers.

    :param text: Der zu analysierende Text als String.
    :return: Das JSON-Ergebnis vom Server (z.B. {'polarity': 0.7, 'sentiment': 'positiv'}).
    """
    # Baut die vollständige URL für den API-Endpunkt zusammen.
    api_url = f"{localhost}/analyze"


    # Der Text wird im JSON-Format im Body der Anfrage übermittelt.
    response = requests.post(api_url, json={"text": text})


    return response.json()


if __name__ == "__main__":
    # Definiert einen Beispieltext für die Analyse.
    example_text = "Der Film war großartig und sehr spannend!"

    # Ruft die Funktion auf, um den Text an den Server zu senden.
    result = analyze_text(example_text)

    # Gibt das vom Server erhaltene Ergebnis auf der Konsole aus.
    print(f"Analyse für den Text: '{example_text}'")
    print(f"Ergebnis vom Server: {result}")