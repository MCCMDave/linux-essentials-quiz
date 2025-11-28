# 📝 Anleitung: Neue Fragen hinzufügen

## Übersicht

Diese Anleitung erklärt, wie du neue Fragen zum Linux Essentials Quiz hinzufügst.

## 🚀 Schnellzugriff (Python-Version)

In der Python-Version (`quiz_engine_v2.py`) gibt es einen direkten Menüpunkt:

1. Starte das Quiz: `python quiz_engine_v2.py`
2. Wähle **[4] Fragen bearbeiten**
3. Wähle:
   - **[1]** für `fragen.json` (Fragen bearbeiten)
   - **[2]** für diese Anleitung (FRAGEN-HINZUFUEGEN.md)

Die Dateien werden automatisch im Standard-Editor deines Systems geöffnet.

## Fragendatenbank-Struktur

### Datenformat (JavaScript)

Fragen sind im `index.html` als JavaScript-Array gespeichert:

```javascript
const questionDatabase = [
    {
        id: 1,
        topic: "1.1 Linux Evolution and Popular Operating Systems",
        question: "Welche der folgenden Linux-Distributionen basiert auf Debian?",
        type: "multiple", // oder "single"
        options: [
            "Ubuntu",
            "Fedora",
            "openSUSE",
            "Arch Linux"
        ],
        correct: [0, 2], // Indizes der richtigen Antworten (0-basiert)
        explanation: "Ubuntu basiert auf Debian. Fedora basiert auf Red Hat."
    },
    // ... weitere Fragen
];
```

### Felder-Erklärung

| Feld | Typ | Beschreibung | Beispiel |
|------|-----|--------------|----------|
| `id` | number | Eindeutige ID (fortlaufend) | `42` |
| `topic` | string | Themenbereich (Topic) | `"1.1 Linux Evolution..."` |
| `question` | string | Fragetext | `"Was ist Linux?"` |
| `type` | string | Fragetyp: `"single"` oder `"multiple"` | `"multiple"` |
| `options` | array | Antwortmöglichkeiten (3-5 Optionen) | `["A", "B", "C"]` |
| `correct` | array | Indizes der richtigen Antworten (0-basiert!) | `[0, 2]` (A und C richtig) |
| `explanation` | string | Erklärung der richtigen Antwort | `"Ubuntu basiert auf Debian..."` |

## Topics & Gewichtung

Die Prüfung basiert auf der offiziellen LPI-Gewichtung:

| Topic | Gewichtung | Anzahl Fragen (von 40) |
|-------|------------|------------------------|
| **1.** The Linux Community and a Career in Open Source | 17.5% | 7 Fragen |
| **2.** Finding Your Way on a Linux System | 22.5% | 9 Fragen |
| **3.** The Power of the Command Line | 22.5% | 9 Fragen |
| **4.** The Linux Operating System | 20% | 8 Fragen |
| **5.** Security and File Permissions | 17.5% | 7 Fragen |

### Topic-Struktur

```
1. The Linux Community and a Career in Open Source
   1.1 Linux Evolution and Popular Operating Systems
   1.2 Major Open Source Applications
   1.3 Open Source Software and Licensing
   1.4 ICT Skills and Working in Linux

2. Finding Your Way on a Linux System
   2.1 Command Line Basics
   2.2 Using the Command Line to Get Help
   2.3 Using Directories and Listing Files
   2.4 Creating, Moving and Deleting Files

3. The Power of the Command Line
   3.1 Archiving Files on the Command Line
   3.2 Searching and Extracting Data from Files
   3.3 Turning Commands into a Script

4. The Linux Operating System
   4.1 Choosing an Operating System
   4.2 Understanding Computer Hardware
   4.3 Where Data is Stored
   4.4 Your Computer on the Network

5. Security and File Permissions
   5.1 Basic Security and Identifying User Types
   5.2 Creating Users and Groups
   5.3 Managing File Permissions and Ownership
   5.4 Special Directories and Files
```

## Schritt-für-Schritt: Neue Frage hinzufügen

### 1. Öffne `index.html`

Suche nach dem `questionDatabase` Array (ca. Zeile 800-2300).

### 2. Wähle die richtige Topic

Finde den passenden Themenbereich für deine Frage.

**Beispiel:** Wenn die Frage über `chmod` ist → Topic 5.3

### 3. Finde die letzte ID

Scrolle zum Ende der Fragendatenbank und merke dir die letzte ID.

**Beispiel:** Letzte Frage hat `id: 156` → Neue Frage bekommt `id: 157`

### 4. Füge die neue Frage hinzu

Kopiere diese Vorlage und füge sie am Ende des Arrays ein (VOR dem schließenden `];`):

```javascript
    ,
    {
        id: 157,  // Nächste fortlaufende ID
        topic: "5.3 Managing File Permissions and Ownership",
        question: "Welcher Befehl ändert die Zugriffsrechte einer Datei?",
        type: "single",  // oder "multiple"
        options: [
            "chmod",
            "chown",
            "chgrp",
            "chattr"
        ],
        correct: [0],  // chmod ist bei Index 0
        explanation: "chmod (change mode) ändert die Dateiberechtigungen. chown ändert den Besitzer."
    }
```

### 5. Prüfe die Syntax

**WICHTIG:**
- ✅ Komma nach jeder Frage (außer der letzten!)
- ✅ Arrays mit eckigen Klammern `[]`
- ✅ Strings mit Anführungszeichen `""`
- ✅ Korrekte Indizierung (0-basiert!)

**Häufige Fehler:**
- ❌ Letztes Komma vergessen
- ❌ Falsche Indizes bei `correct` (1 statt 0)
- ❌ `type: "single"` aber `correct: [0, 1]` (nur bei multiple!)

### 6. Teste die Frage

1. Öffne `index.html` im Browser
2. Starte eine Prüfung
3. Prüfe, ob die Frage korrekt angezeigt wird
4. Teste beide Frage-Typen (single/multiple)

## Fragetypen

### Single Choice (nur EINE richtige Antwort)

```javascript
{
    type: "single",
    options: ["A", "B", "C", "D"],
    correct: [1]  // Nur B ist richtig
}
```

### Multiple Choice (MEHRERE richtige Antworten)

```javascript
{
    type: "multiple",
    options: ["A", "B", "C", "D"],
    correct: [0, 2]  // A und C sind richtig
}
```

## Best Practices

### Gute Fragen schreiben

✅ **DO:**
- Klar und präzise formulieren
- Realistische Szenarien verwenden
- Alle Optionen gleich lang machen
- Erklärung mit Mehrwert schreiben

❌ **DON'T:**
- Trick-Fragen stellen
- Zu offensichtliche Optionen ("Alle" / "Keine")
- Unnötig kompliziert formulieren
- Copy-Paste ohne Anpassung

### Beispiel: Gute Frage

```javascript
{
    question: "Sie möchten eine Datei für alle Benutzer lesbar machen. Welcher Befehl ist korrekt?",
    options: [
        "chmod 444 datei.txt",
        "chmod 644 datei.txt",
        "chmod 744 datei.txt",
        "chmod 777 datei.txt"
    ],
    correct: [1],
    explanation: "chmod 644 gibt dem Besitzer Lese- und Schreibrechte (6), der Gruppe und allen anderen nur Leserechte (4)."
}
```

### Beispiel: Schlechte Frage ❌

```javascript
{
    question: "Was macht chmod?",  // Zu vage!
    options: [
        "Ändert Rechte",  // Zu kurz!
        "Ändert den Besitzer der Datei",
        "Löscht die Datei",
        "Keine der Antworten ist richtig"  // Vermeiden!
    ],
    correct: [0],
    explanation: "Rechte."  // Zu kurz, kein Mehrwert!
}
```

## Erklärungen schreiben

### Gute Erklärung ✅

```javascript
explanation: "tar ist das Standard-Archivierungstool unter Linux. Der Parameter -c erstellt ein neues Archiv, -z komprimiert mit gzip, -f gibt den Dateinamen an, und -v zeigt Fortschritt (verbose)."
```

### Schlechte Erklärung ❌

```javascript
explanation: "tar ist richtig."  // Zu kurz!
```

## Qualitätssicherung

### Checkliste vor dem Commit

- [ ] ID ist fortlaufend und einzigartig
- [ ] Topic ist korrekt zugeordnet
- [ ] Fragetext ist klar formuliert
- [ ] 3-5 Antwortoptionen vorhanden
- [ ] `correct` Array hat korrekte Indizes (0-basiert!)
- [ ] `type` passt zu Anzahl richtiger Antworten
- [ ] Erklärung ist informativ
- [ ] Syntax ist korrekt (Kommas, Klammern)
- [ ] Im Browser getestet

## Beispiel: Vollständige Frage

```javascript
{
    id: 158,
    topic: "3.2 Searching and Extracting Data from Files",
    question: "Sie möchten alle Zeilen in einer Datei finden, die das Wort 'error' enthalten (Groß-/Kleinschreibung egal). Welcher Befehl ist korrekt?",
    type: "single",
    options: [
        "grep -i error logfile.txt",
        "grep error logfile.txt",
        "find error logfile.txt",
        "search -i error logfile.txt"
    ],
    correct: [0],
    explanation: "grep -i führt eine case-insensitive Suche durch. Der Parameter -i steht für 'ignore case'. Ohne -i würde nur 'error' gefunden, aber nicht 'Error' oder 'ERROR'."
}
```

## Häufige Fehler & Lösungen

| Fehler | Symptom | Lösung |
|--------|---------|--------|
| Letztes Komma fehlt | Syntax Error | Komma nach jeder Frage (außer letzter) |
| Falsche Indizes | Falsche Antworten als korrekt | Index startet bei 0, nicht 1! |
| `type` falsch | Single-Choice zeigt Checkboxen | Bei nur 1 richtiger Antwort: `"single"` |
| Doppelte ID | Frage wird nicht angezeigt | IDs müssen einzigartig sein |
| Klammern falsch | Parsing Error | Arrays: `[]`, Objects: `{}` |

## Gewichtung beachten

Achte darauf, dass die Topics ausgewogen bleiben:

**Ziel-Verteilung (bei 160 Fragen gesamt):**
- Topic 1: ~28 Fragen (17.5%)
- Topic 2: ~36 Fragen (22.5%)
- Topic 3: ~36 Fragen (22.5%)
- Topic 4: ~32 Fragen (20%)
- Topic 5: ~28 Fragen (17.5%)

**Aktuellen Stand prüfen:**
```javascript
// Im Browser-Console:
const topics = questionDatabase.reduce((acc, q) => {
    const t = q.topic.charAt(0);
    acc[t] = (acc[t] || 0) + 1;
    return acc;
}, {});
console.table(topics);
```

## Weitere Ressourcen

- [LPI Linux Essentials Objectives](https://www.lpi.org/our-certifications/exam-010-objectives)
- [Linux man pages](https://man7.org/linux/man-pages/)
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/)

---

**Bei Fragen:** Erstelle ein Issue im Repository oder kontaktiere dave@vaupel.de

**Viel Erfolg beim Fragen erstellen!** 🎓
