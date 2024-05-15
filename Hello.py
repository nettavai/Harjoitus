sanakirja = {
    "auto": "ajoneuvo",
    "omena": "hedelmä",
    "tietokone": "laitteisto"
}

def hae_sanakirjasta(avain):
    if avain in sanakirja:
        return sanakirja[avain]
    else:
        return "Sanaa ei löytynyt sanakirjasta."

# Testataan sanakirjan hakua
print(hae_sanakirjasta("auto"))  # Tulostaa: ajoneuvo
print(hae_sanakirjasta("omena"))  # Tulostaa: hedelmä
print(hae_sanakirjasta("kissa"))  # Tulostaa: Sanaa ei löytynyt sanakirjasta.

