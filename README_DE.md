# 🎓 Phase 2: Quiz-Engine

**🇩🇪 Deutsche Version** | **[🇬🇧 English Version](README.md)**

---

Ein interaktives Quiz-System für Linux Essentials 010-160 Prüfungsvorbereitung mit OOP, JSON-Datenstruktur und verschiedenen Lernmodi.

---

## 🎯 Projektziel

Aufbauend auf [Phase 1.5 (Assignment 2)](../phase1.5-oop/assignment2_quiz_system.py) wurde die Quiz-Engine erweitert mit:
- Trennung von Daten (JSON) und Logik (Python)
- Zufällige Fragen- und Antwort-Reihenfolge
- Verschiedene Quiz-Modi (Lernen, Prüfung, Custom)
- Timer für realistische Prüfungsbedingungen

---

## ✨ Features

### Version 1.0 (quiz_engine_v1.py)
- 277 Fragen direkt im Code (embedded)
- OOP mit `Frage` Klasse
- Professionelle Formatierung
- Basis für V2 - zeigt Code-Evolution

### Version 2.0 (quiz_engine_v2.py)
- ✅ **276 Fragen aus JSON** - einfach erweiterbar
- ✅ **3 Quiz-Modi:**
  - **Lernmodus:** Alle 276 Fragen durchgehen
  - **Prüfungsmodus:** 40 Fragen, 60 Minuten Timer
  - **Custom-Modus:** Beliebige Anzahl wählen
- ✅ **Randomisierung:**
  - Fragen in zufälliger Reihenfolge
  - Antworten gemischt (A-D)
- ✅ **Statistiken:**
  - Prozentuale Auswertung
  - Richtige vs. falsche Antworten
  - Zeitanzeige (Prüfungsmodus)
  - Bestanden/Nicht Bestanden (≥60%)

---

## 📊 Fragen-Datenbank

**fragen.json** enthält 276 Prüfungsfragen aus allen offiziellen Topics.

### Kategorien-Verteilung

| Kategorie | Anzahl |
|-----------|--------|
| 1.1 Linux Evolution | 28 |
| 4.3 Where Data is Stored | 27 |
| 4.4 Computer on Network | 26 |
| 3.2 Searching and Extracting | 24 |
| 2.1 Command Line Basics | 21 |
| 3.3 Shell Scripting | 19 |
| 4.2 Computer Hardware | 18 |
| 1.2 Open Source Applications | 16 |
| 4.1 Choosing an OS | 14 |
| *...und 10 weitere* | 83 |

### JSON-Struktur

```json
{
  "metadata": {
    "version": "1.0",
    "total_fragen": 276,
    "kategorien": {...},
    "beschreibung": "Linux Essentials 010-160 v1.6"
  },
  "fragen": [
    {
      "frage": "Wer hat den Linux-Kernel ursprünglich entwickelt?",
      "optionen": [
        "Richard Stallman",
        "Linus Torvalds",
        "Dennis Ritchie",
        "Ken Thompson"
      ],
      "richtige_antwort": 1,
      "kategorie": "1.1 Linux Evolution"
    }
  ]
}
```

---

## 🎮 Verwendung

### Start
```bash
python quiz_engine_v2.py
```

### Menü-Optionen
```
==============================================================================================
==                                 QUIZ-MODUS WÄHLEN                                        ==
==============================================================================================
==                                                                                          ==
==                          [1] Lernmodus - Alle Fragen (276)                              ==
==                          [2] Prüfungsmodus - 40 Fragen, 60 Min                          ==
==                          [3] Custom - Anzahl wählen                                     ==
==                          [0] Beenden                                                    ==
==                                                                                          ==
==============================================================================================
```

### Modi im Detail

#### 🎓 Lernmodus
- Alle 276 Fragen
- Kein Zeitlimit
- Sofortiges Feedback nach jeder Frage
- Ideal zum umfassenden Lernen

#### ⏱️ Prüfungsmodus
- 40 zufällige Fragen
- 60 Minuten Zeitlimit
- Timer läuft im Hintergrund
- Zeitwarnung bei <5 Minuten
- Bestanden/Nicht Bestanden Anzeige (≥60% = bestanden)
- Realistisch wie echte Linux Essentials Prüfung

#### 🎛️ Custom-Modus
- Beliebige Anzahl (1-276) wählen
- Kein Zeitlimit
- Ideal für gezieltes Üben
- Flexibel für verschiedene Lernziele

---

## 🧠 Lernziele Phase 2

### Technische Skills
- ✅ JSON Import/Export
- ✅ `random` Modul (shuffle, sample)
- ✅ `time` Modul für Timer
- ✅ `os` Modul für Pfade
- ✅ List Slicing
- ✅ Enumerate mit Start-Index

### OOP Konzepte
- ✅ Instanzmethoden erweitern (`shuffle_optionen`)
- ✅ Klassen-Design verbessern
- ✅ Daten von Logik trennen

### Best Practices
- ✅ Externe Datenquellen nutzen
- ✅ Benutzerfreundliche Menüs
- ✅ Input-Validierung
- ✅ Error-Handling
- ✅ Relative Pfade (portabel)

---

## 📁 Projekt-Struktur

```
phase-2/
├── quiz_engine_v1.py       # Version 1 (277 Fragen embedded)
├── quiz_engine_v2.py       # Version 2 (lädt aus JSON)
├── fragen.json             # Fragen-Datenbank (276 Fragen)
├── README.md               # English documentation
└── README_DE.md            # Diese Datei
```

---

## 🔗 Verwandte Projekte

### Phase 1
- [Taschenrechner](../phase-1/t4_taschenrechner_optimiert.py) - 9 Operationen mit Match/Case
- [Assignment 1: Service Monitor](../phase-1/david_vaupel_assignment1.py) - Homelab Monitoring

### Phase 1.5
- [Assignment 2: Quiz-System](../phase-1.5/david_vaupel_assignment2.py) - OOP Grundlagen, Basis für Phase 2

### Roadmap
- [Learning Roadmap](../docs/LEARNING-ROADMAP.md) - Kompletter Lernplan (Phasen 1-3)

---

## 🎓 Linux Essentials Zertifizierung

Dieses Quiz basiert auf dem **Linux Essentials 010-160 v1.6** Prüfungsformat:

### Prüfungs-Details
- **Dauer:** 60 Minuten
- **Fragen:** 40 Multiple-Choice
- **Format:** 4 Antwortoptionen (A-D)
- **Topics:** 5 Hauptthemen
- **Bestehen:** ~60% (24 von 40 richtig)

### Themen-Abdeckung

| Topic | Gewichtung | Fragen |
|-------|------------|--------|
| 1. Linux Community & Open Source | 17.5% | 7 |
| 2. Finding Your Way | 22.5% | 9 |
| 3. The Power of the Command Line | 25% | 10 |
| 4. The Linux Operating System | 27.5% | 11 |
| 5. Security & File Permissions | 7.5% | 3 |

### Prüfungsvorbereitung
- ✅ Alle offiziellen Topics abgedeckt
- ✅ Realistische Fragenstellung
- ✅ Prüfungs-Timer simuliert Zeitdruck
- ✅ Prozentuale Auswertung wie in Prüfung

---

## 📊 Entwicklungs-Statistik

### Code-Evolution
- **V1:** 1885 Zeilen (mit embedded Fragen)
- **V2:** ~320 Zeilen (ohne Fragen-Daten)
- **Reduktion:** 83% schlanker durch JSON-Trennung!

### Entwicklungszeit
- **Phase 2:** ~1 Woche (November 2025)
- **Fragen:** Von 10 auf 276 erweitert
- **Features:** 3 Modi, Timer, Custom-Auswahl

### Datenbank
- **Fragen:** 276 total
- **Kategorien:** 19 verschiedene
- **Duplikate:** 0 (geprüft)

---

## 💡 Gelernte Lektionen

### Was gut funktioniert
- ✅ JSON-Trennung macht Code wartbar
- ✅ Random-Shuffle verhindert Auswendiglernen
- ✅ Custom-Modus gibt Flexibilität
- ✅ Timer motiviert und simuliert Prüfungsdruck

### Herausforderungen
- Antworten shufflen + Index anpassen (gelöst mit `enumerate`)
- Timer im Hintergrund ohne Threading (gelöst mit `time.time()`)
- 276 Fragen manuell formatieren (gelöst: HTML-Parser!)
- Relative Pfade für Portabilität (gelöst mit `os.path`)

### Nächste Schritte
- **Phase 3:** HTML-Parser für automatischen Import
- Kategorien-Filter implementieren
- Ergebnisse in JSON speichern (Historie)
- Highscore-System

---

## 🛠️ Tech Stack

### Python 3.13
**Standard Library:**
- `json` - Datenimport/-export
- `random` - Shuffling (shuffle, sample)
- `time` - Timer-Funktionalität
- `os` - Pfad-Handling (portabel)

**Keine externen Dependencies!** ✅

---

## 🚀 Installation & Setup

### Voraussetzungen
- Python 3.10+ (wegen match/case in V1)
- Windows / Linux / macOS

### Setup
```bash
# Repository klonen
git clone https://github.com/MCCMDave/python-learning.git
cd python-learning/phase-2

# Starten
python quiz_engine_v2.py
```

### Dateien
Stelle sicher, dass diese Dateien im selben Ordner sind:
- `quiz_engine_v2.py`
- `fragen.json`

---

## 📖 Code-Beispiele

### Frage-Klasse
```python
class Frage:
    def __init__(self, fragetext, optionen, richtige_antwort, kategorie):
        self.frage = fragetext
        self.optionen = optionen
        self.richtige_antwort = richtige_antwort
        self.kategorie = kategorie
    
    def shuffle_optionen(self):
        """Mischt Antworten und passt Index an."""
        # ...
```

### JSON Laden
```python
def lade_fragen():
    """Lädt Fragen aus JSON."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_pfad = os.path.join(script_dir, 'fragen.json')
    
    with open(json_pfad, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Erstelle Frage-Objekte
    fragen_liste = [Frage(...) for q in data['fragen']]
    random.shuffle(fragen_liste)
    return fragen_liste
```

---

## 📄 Lizenz

MIT License - Frei verwendbar für Lernen & Prüfungsvorbereitung

---

## 👨‍💻 Autor

**David Vaupel**  
Python-Lernender | Linux Essentials Certified (85%+)

- 📧 Kontakt via [GitHub Issues](https://github.com/MCCMDave/python-learning/issues)
- 💼 [LinkedIn](https://www.linkedin.com/in/david-vaupel)
- 🏠 [Homelab-Automation](https://github.com/MCCMDave/homelab-automation)
- 💻 [Windows-Automation](https://github.com/MCCMDave/windows-automation)

---

## 📝 Changelog

### v2.0 (November 2025)
- ✅ JSON-Datenbank mit 276 Fragen
- ✅ 3 Quiz-Modi (Lernen/Prüfung/Custom)
- ✅ Timer-System für Prüfungsmodus
- ✅ Antworten-Shuffling
- ✅ Bestanden/Nicht Bestanden Logik

### v1.0 (November 2025)
- ✅ Basis-Quiz mit 277 embedded Fragen
- ✅ OOP mit Frage-Klasse
- ✅ Erste Version aus Assignment 2

---

**Status:** ✅ Phase 2 abgeschlossen (v2.0)  
**Letztes Update:** November 2025

---

**[⬆ Zurück nach oben](#-phase-2-quiz-engine)**
