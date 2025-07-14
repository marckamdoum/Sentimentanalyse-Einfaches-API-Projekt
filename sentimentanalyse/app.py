import streamlit as st
from client import analyze_text

st.title("Sentimentanalyse von Film-Feedback")

# Erstellt ein mehrzeiliges Textfeld für die Benutzereingabe.
user_input = st.text_area("Geben Sie Ihr Feedback ein:")

# Dieser Code-Block wird nur ausgeführt, wenn der Benutzer auf den Button klickt.
if st.button("Analysieren"):
    # Ruft die Funktion aus der client.py auf, um die API-Anfrage an den Server zu senden.
    result = analyze_text(user_input)

    # Zeigt das vom Server erhaltene Ergebnis direkt in der Web-Oberfläche an.
    st.write(f"Polarität: {result['polarity']}, Klassifizierung: {result['sentiment']}")