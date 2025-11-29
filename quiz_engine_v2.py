"""
OOP Assignment: Quiz-Fragen-System für Linux Essentials
Ein Programm zum Erstellen u. Abfragen von Prüfungsfragen

Autor: Dave
Datum: 16.11.2025
Assignment: Python OOP Grundlagen
"""

# Importierte Module
import json
import random
import os
from datetime import date
import time
import threading
import sys

# Konstanten f. d. Formatierung
BREITE = 95
INNENBREITE = 91
RAHMEN = "="
EINRUECKUNG = 31
OPT_EINRUECKUNG = 38


def header():
    """Header mit Rahmen ausgeben."""
    trennung()
    zeige_zeile(" Linux Essentials Quiz-System ")
    trennung()
    leer()


def footer():
    """Zeigt den Programm-Footer."""
    trennung()
    zeige_zeile(" Ende vom Quiz ")
    trennung()


def leer():
    """Leere Zeile einfügen"""
    print(RAHMEN * 2 + "".center(INNENBREITE) + RAHMEN * 2)


def trennung():
    """Trennlinie"""
    print(RAHMEN * BREITE)


def tren_leer():
    """Trennlinie mit leerer Zeile."""
    leer()
    trennung()
    leer()


def zeige_zeile(text):
    """Zeigt eine zentrierte Zeile mit Rahmen."""
    print(RAHMEN * 2 + text.center(INNENBREITE) + RAHMEN * 2)


def zeige_option(text):
    """Zeigt eine linksbündige Option mit Rahmen."""
    print(
        RAHMEN * 2
        + " " * OPT_EINRUECKUNG
        + text.ljust(INNENBREITE - OPT_EINRUECKUNG)
        + RAHMEN * 2
    )


def einr_input(prompt):
    """Nutzt Input mit Rahmen."""
    leer()
    input(RAHMEN * 2 + " " * EINRUECKUNG + prompt)


def hole_antwort(prompt):
    """Holt Nutzer-Input mit Validierung u. Rahmen (ohne Enter-Druck)."""
    import msvcrt  # Windows-spezifisch für Tastatur-Input

    while True:
        leer()
        # Prompt anzeigen
        sys.stdout.write(RAHMEN * 2 + " " * EINRUECKUNG + prompt)
        sys.stdout.flush()

        # Warte auf Tastendruck (ohne Enter)
        if sys.platform == "win32":
            taste = msvcrt.getch().decode("utf-8").upper()
        else:
            # Fallback für Linux/Mac: mit Enter
            taste = input().upper()

        # Zeige die Auswahl mit == an
        sys.stdout.write(f" {taste} ==")
        sys.stdout.flush()
        print()  # Neue Zeile

        if taste in ["A", "B", "C", "D"]:
            return taste
        else:
            leer()
            zeige_zeile(" FEHLER: Bitte nur A, B, C oder D! ")


def formatiere_zeit(sekunden):
    """Formatiert Sekunden in MM:SS Format."""
    minuten = int(sekunden // 60)
    sek = int(sekunden % 60)
    return f"{minuten:02d}:{sek:02d}"


def pruefe_zeitlimit(start_zeit, zeitlimit_sekunden):
    """Prüft ob das Zeitlimit überschritten wurde."""
    verstrichene_zeit = time.time() - start_zeit
    verbleibende_zeit = zeitlimit_sekunden - verstrichene_zeit
    ist_abgelaufen = verbleibende_zeit <= 0
    return ist_abgelaufen, max(0, verbleibende_zeit)


def zeige_zeitwarnung(verbleibende_zeit):
    """Zeigt Warnung wenn weniger als 5 Minuten übrig."""
    minuten = verbleibende_zeit / 60
    if 0 < minuten <= 5:
        leer()
        zeige_zeile(
            f" ⚠️  WARNUNG: Nur noch {formatiere_zeit(verbleibende_zeit)} übrig! "
        )
        leer()


def zeige_menue():
    """
    Zeigt das Menü zur Auswahl des Quiz-Modus.

    Returns:
        str: Die Wahl des Users ("1", "2", "3", "4" oder "0")
    """
    leer()
    zeige_zeile(" QUIZ-MODUS WÄHLEN ")
    leer()
    zeige_zeile(" [1] Lernmodus - Alle Fragen (276) ")
    zeige_zeile(" [2] Prüfungsmodus - 40 Fragen, 60 Min ")
    zeige_zeile(" [3] Custom - Anzahl wählen ")
    zeige_zeile(" [4] Fragen bearbeiten ")
    zeige_zeile(" [0] Beenden ")
    leer()
    trennung()

    while True:
        leer()
        wahl = input(RAHMEN * 2 + " " * EINRUECKUNG + "Deine Wahl (0/1/2/3/4): ")

        if wahl in ["0", "1", "2", "3", "4"]:
            return wahl
        else:
            leer()
            zeige_zeile(" FEHLER: Bitte nur 0, 1, 2, 3 oder 4 eingeben! ")


def hole_anzahl_fragen(max_fragen):
    """
    Fragt User nach gewünschter Anzahl Fragen.

    Args:
        max_fragen (int): Maximum verfügbare Fragen

    Returns:
        int: Gewählte Anzahl Fragen
    """
    leer()
    zeige_zeile(f" Wie viele Fragen möchtest du? (1-{max_fragen}) ")

    while True:
        leer()
        try:
            anzahl = int(input(RAHMEN * 2 + " " * EINRUECKUNG + "Anzahl: "))
            if 1 <= anzahl <= max_fragen:
                return anzahl
            else:
                leer()
                zeige_zeile(f" FEHLER: Bitte eine Zahl zwischen 1 und {max_fragen}! ")
        except ValueError:
            leer()
            zeige_zeile(" FEHLER: Bitte eine gültige Zahl eingeben! ")


def oeffne_fragen_editor():
    """Öffnet die Fragendatei im Standard-Editor."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_pfad = os.path.join(script_dir, "fragen.json")
    anleitung_pfad = os.path.join(script_dir, "FRAGEN-HINZUFUEGEN.md")

    leer()
    zeige_zeile(" FRAGEN-EDITOR ")
    leer()
    zeige_zeile(" Welche Datei möchtest du öffnen? ")
    leer()
    zeige_zeile(" [1] fragen.json (Fragen bearbeiten) ")
    zeige_zeile(" [2] FRAGEN-HINZUFUEGEN.md (Anleitung lesen) ")
    zeige_zeile(" [0] Zurück ")
    leer()
    trennung()

    while True:
        leer()
        wahl = input(RAHMEN * 2 + " " * EINRUECKUNG + "Deine Wahl (0/1/2): ")

        if wahl == "0":
            return
        elif wahl == "1":
            leer()
            zeige_zeile(" Öffne fragen.json... ")
            leer()
            if sys.platform == "win32":
                os.startfile(json_pfad)
            elif sys.platform == "darwin":
                os.system(f'open "{json_pfad}"')
            else:
                os.system(f'xdg-open "{json_pfad}"')
            time.sleep(1)
            return
        elif wahl == "2":
            leer()
            zeige_zeile(" Öffne FRAGEN-HINZUFUEGEN.md... ")
            leer()
            if sys.platform == "win32":
                os.startfile(anleitung_pfad)
            elif sys.platform == "darwin":
                os.system(f'open "{anleitung_pfad}"')
            else:
                os.system(f'xdg-open "{anleitung_pfad}"')
            time.sleep(1)
            return
        else:
            leer()
            zeige_zeile(" FEHLER: Bitte nur 0, 1 oder 2 eingeben! ")


class LiveTimer:
    """Klasse für Live-Timer-Anzeige während des Quiz."""

    def __init__(self, start_zeit, zeitlimit_sekunden):
        """
        Initialisiert den Live-Timer.

        Args:
            start_zeit (float): Startzeit (time.time())
            zeitlimit_sekunden (int): Zeitlimit in Sekunden
        """
        self.start_zeit = start_zeit
        self.zeitlimit_sekunden = zeitlimit_sekunden
        self.running = False
        self.thread = None

    def start(self):
        """Startet den Live-Timer in einem separaten Thread."""
        self.running = True
        self.thread = threading.Thread(target=self._update_timer, daemon=True)
        self.thread.start()

    def stop(self):
        """Stoppt den Live-Timer."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=1)

    def _update_timer(self):
        """Aktualisiert die Timer-Anzeige jede Sekunde."""
        while self.running:
            verstrichene_zeit = time.time() - self.start_zeit
            verbleibende_zeit = max(0, self.zeitlimit_sekunden - verstrichene_zeit)

            # Timer-Zeile ausgeben (überschreibt vorherige)
            timer_text = f"⏱️  Zeit verbleibend: {formatiere_zeit(verbleibende_zeit)}"
            sys.stdout.write(
                f"\r{RAHMEN*2} {timer_text.center(INNENBREITE)} {RAHMEN*2}"
            )
            sys.stdout.flush()

            if verbleibende_zeit <= 0:
                break

            time.sleep(1)


# Klasse f. d. Fragen
class Frage:
    """
    Eine Quiz-Frage für Linux Essentials Prüfungsvorbereitung.

    Diese Klasse reprÃ¤sentiert eine Multiple-Choice-Frage mit vier
    Antwortmöglichkeiten u. Kategorisierung nach Themengebiet.

    Attributes:
        fragetext (str): Der Text der Frage
        optionen (list): Liste mit 4 AntwortmÃ¶glichkeiten
        richtige_antwort (int): Index der richtigen Antwort (0-3)
        kategorie (str): Kategorie der Frage (z.B. "Kommandozeile")
    """

    def __init__(self, fragetext, optionen, richtige_antwort, kategorie):
        """
        Initialisiert eine neue Quiz-Frage.

        Args:
            fragetext (str): Der Text der Frage
            optionen (list): Liste mit 4 AntwortmÃ¶glichkeiten
            richtige_antwort (int): Index der richtigen Antwort (0-3)
            kategorie (str): Kategorie der Frage
        """
        # Kontrolle d eingereichten Fragen-Daten
        if len(optionen) != 4:
            raise ValueError("Es müssen genau 4 Optionen sein!")

        if not 0 <= richtige_antwort <= 3:
            raise ValueError("Richtige Antwort muss 0-3 sein!")

        # Attribute setzen
        self.frage = fragetext
        self.optionen = optionen
        self.richtige_antwort = richtige_antwort
        self.kategorie = kategorie

    def zeige_frage(self):
        """
        Zeigt die Frage mit allen Antworten an.

        Die Ausgabe zeigt Kategorie, Fragetext u. vier Optionen
        mit den Buchstaben A-D in einem Rahmen.
        """
        zeige_zeile(f" Kategorie: {self.kategorie} ")
        leer()
        zeige_zeile(f" Frage: {self.frage} ")
        leer()
        buchstaben = ["A", "B", "C", "D"]
        for i, option in enumerate(self.optionen):
            zeige_option(f" {buchstaben[i]}: {option} ")

    def checke_antwort(self, nutzer_antwort):
        """
        Checkt ob die Antwort des Users korrekt ist.

        Args:
            nutzer_antwort (str): Die Antwort des Users ("A", "B", "C", oder "D")

        Returns:
            bool: True wenn die Antwort richtig ist, False sonst
        """
        # Dictionary z. Zuordnung d. Buchstaben zu Indizes
        antwort_zuordnen = {"A": 0, "B": 1, "C": 2, "D": 3}
        nutzer_index = antwort_zuordnen.get(nutzer_antwort)

        # Kontrolle der Antwort
        if nutzer_index is None:
            return False
        # Vergleich mit richtiger Antwort
        elif nutzer_index == self.richtige_antwort:
            return True

    def zeige_antwort(self):
        """
        Zeigt die richtige Antwort an.

        Die Ausgabe erfolgt mit dem entsprechenden
        Buchstaben (A-D) u. dem Text d. richtigen Antwort.
        """
        buchstaben = ["A", "B", "C", "D"]
        richtige_buchstabe = buchstaben[self.richtige_antwort]
        richtige_option = self.optionen[self.richtige_antwort]
        zeige_zeile(f" {richtige_buchstabe}: {richtige_option} ")

    def shuffle_optionen(self):
        """Mischt die Antwortoptionen und passt den richtigen Index an."""
        # Erstellt eine Liste mit Paaren aus Index u. Option
        optionen_mit_index = list(enumerate(self.optionen))

        # Mischt die Liste
        random.shuffle(optionen_mit_index)

        # Findet die neuen Optionen
        self.optionen = [opt for idx, opt in optionen_mit_index]

        # findet den neuen Index der richtigen Antwort
        for new_idx, (old_idx, opt) in enumerate(optionen_mit_index):
            if old_idx == self.richtige_antwort:
                self.richtige_antwort = new_idx
                break


def lade_fragen():
    """
    Lädt alle Fragen aus fragen.json.

    Returns:
        list: Liste mit Frage-Objekten
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_pfad = os.path.join(script_dir, "fragen.json")

    with open(json_pfad, "r", encoding="utf-8") as f:
        data = json.load(f)

    fragen_liste = []
    for q in data["fragen"]:
        frage = Frage(
            fragetext=q["frage"],
            optionen=q["optionen"],
            richtige_antwort=q["richtige_antwort"],
            kategorie=q["kategorie"],
        )
        fragen_liste.append(frage)
    # Fragen mischen
    random.shuffle(fragen_liste)

    return fragen_liste


# Hauptprogramm
def main():
    """
    Hauptfunktion - Quiz-Engine mit verschiedenen Modi.

    Modi:
    - Lernmodus: Alle Fragen ohne Zeitlimit
    - Prüfungsmodus: 40 Fragen mit 60 Min Timer
    - Custom: Beliebige Anzahl ohne Zeitlimit
    """
    header()

    # Menü anzeigen u. Modus wählen
    modus = zeige_menue()

    if modus == "0":
        leer()
        zeige_zeile(" Bis bald! ")
        footer()
        return
    elif modus == "4":
        # Fragen-Editor öffnen
        oeffne_fragen_editor()
        leer()
        zeige_zeile(" Zurück zum Hauptmenü ")
        footer()
        return

    # Fragen laden
    fragen_liste = lade_fragen()
    max_fragen = len(fragen_liste)

    # Timer-Variablen
    hat_zeitlimit = False
    start_zeit = None
    zeitlimit_sekunden = 0
    live_timer = None

    # Anzahl Fragen je nach Modus
    if modus == "1":
        # Lernmodus: Alle Fragen
        pass
    elif modus == "2":
        # Prüfungsmodus: 40 Fragen mit Gewichtung, 60 Min
        # Gewichtung nach LPI 010-160 v1.6
        gewichtung = {
            "1.": 7,  # Topic 1: 17.5% (7 von 40 Fragen)
            "2.": 9,  # Topic 2: 22.5% (9 von 40 Fragen)
            "3.": 9,  # Topic 3: 22.5% (9 von 40 Fragen)
            "4.": 8,  # Topic 4: 20% (8 von 40 Fragen)
            "5.": 7,  # Topic 5: 17.5% (7 von 40 Fragen)
        }

        # Fragen nach Topics gruppieren und gewichtet auswählen
        exam_fragen = []
        for topic_prefix, anzahl in gewichtung.items():
            # Filtere Fragen nach Topic (z.B. alle die mit "1." beginnen)
            topic_fragen = [
                f for f in fragen_liste if f.kategorie.startswith(topic_prefix)
            ]
            # Mische und nimm die benötigte Anzahl
            random.shuffle(topic_fragen)
            exam_fragen.extend(topic_fragen[:anzahl])

        # Gesamte Prüfung nochmal mischen
        random.shuffle(exam_fragen)
        fragen_liste = exam_fragen

        hat_zeitlimit = True
        zeitlimit_sekunden = 60 * 60  # 60 Minuten
        start_zeit = time.time()
        leer()
        trennung()
        leer()
        zeige_zeile(" ⏱️  Timer gestartet: 60 Minuten ")
        leer()
        # Live-Timer starten
        live_timer = LiveTimer(start_zeit, zeitlimit_sekunden)
        live_timer.start()
    elif modus == "3":
        # Custom: User wählt Anzahl
        anzahl = hole_anzahl_fragen(max_fragen)
        fragen_liste = fragen_liste[:anzahl]

    # Antworten für jede Frage shufflen
    for frage in fragen_liste:
        frage.shuffle_optionen()

    richtige_antworten = 0
    zeige_zeile(f" Insgesamt {len(fragen_liste)} Fragen geladen ")
    leer()

    # Quiz durchlaufen
    for i, frage in enumerate(fragen_liste, 1):

        # Zeitlimit prüfen (nur Prüfungsmodus)
        if hat_zeitlimit:
            ist_abgelaufen, verbleibende_zeit = pruefe_zeitlimit(
                start_zeit, zeitlimit_sekunden
            )

            if ist_abgelaufen:
                leer()
                trennung()
                leer()
                zeige_zeile(" ZEIT ABGELAUFEN! ")
                zeige_zeile(" Quiz wird beendet... ")
                leer()
                trennung()
                break

            # Warnung bei wenig Zeit
            if i % 10 == 0:  # Alle 10 Fragen prüfen
                zeige_zeitwarnung(verbleibende_zeit)

        zeige_zeile(f" Frage {i} von {len(fragen_liste)} ")

        # Zeit-Info im Prüfungsmodus
        if hat_zeitlimit:
            _, verbleibende_zeit = pruefe_zeitlimit(start_zeit, zeitlimit_sekunden)
            zeige_zeile(f" ⏱️  Zeit: {formatiere_zeit(verbleibende_zeit)} ")

        leer()

        # Frage anzeigen u. Antwort holen
        frage.zeige_frage()
        antwort = hole_antwort("Deine Antwort (A/B/C/D): ")

        # Antwort kontrollieren u. Feedback geben
        if frage.checke_antwort(antwort):
            leer()
            zeige_zeile(" RICHTIG! Sehr gut! ")
            tren_leer()
            richtige_antworten += 1
        else:
            leer()
            zeige_zeile(" FALSCH! Die richtige Antwort ist: ")
            frage.zeige_antwort()
            tren_leer()

    # Live-Timer stoppen (falls aktiv)
    if live_timer:
        live_timer.stop()
        print()  # Neue Zeile nach Timer-Stop

    # Endergebnis
    leer()
    trennung()
    leer()
    zeige_zeile(" 📊 ENDERGEBNIS ")
    leer()

    # Beantwortete Fragen (bei Zeitablauf)
    beantwortete_fragen = i if hat_zeitlimit else len(fragen_liste)

    zeige_zeile(f" Richtig: {richtige_antworten}/{beantwortete_fragen} ")

    if beantwortete_fragen > 0:
        prozent = (richtige_antworten / beantwortete_fragen) * 100
        zeige_zeile(f" Prozent: {prozent:.1f}% ")

        # Bestanden-Info für Prüfungsmodus
        if modus == "2":
            if prozent >= 60:
                zeige_zeile(" BESTANDEN! (≥60% erforderlich) ")
            else:
                zeige_zeile(" NICHT BESTANDEN (<60%) ")

    # Zeit-Statistik
    if hat_zeitlimit:
        verstrichene_zeit = time.time() - start_zeit
        zeige_zeile(f" Benötigte Zeit: {formatiere_zeit(verstrichene_zeit)} ")

        if verstrichene_zeit < zeitlimit_sekunden:
            gesparte_zeit = zeitlimit_sekunden - verstrichene_zeit
            zeige_zeile(f" Zeit übrig: {formatiere_zeit(gesparte_zeit)} ")

    leer()
    trennung()
    leer()

    input(" " * EINRUECKUNG + "ENTER zum Beenden... ")

    footer()


if __name__ == "__main__":
    main()
