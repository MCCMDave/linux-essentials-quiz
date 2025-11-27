"""
OOP Assignment: Quiz-Fragen-System für Linux Essentials
Ein Programm zum Erstellen u. Abfragen von Prüfungsfragen

Autor: Dave
Datum: 16.11.2025
Assignment: Python OOP Grundlagen
"""

# Konstanten f. d. Formatierung
BREITE = 95
INNENBREITE = 91
RAHMEN = "="         
EINRUECKUNG = 31
OPT_EINRUECKUNG = 38
# Funktionen f. d. Formatierung
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
    print(RAHMEN*2 + "".center(INNENBREITE) + RAHMEN*2)
def trennung():
    """Trennlinie"""
    print(RAHMEN*BREITE)
def tren_leer():
    """Trennlinie mit leerer Zeile."""
    leer()
    trennung()
    leer()
def zeige_zeile(text):
    """Zeigt eine zentrierte Zeile mit Rahmen."""
    print(RAHMEN*2 + text.center(INNENBREITE) + RAHMEN*2)
def zeige_option(text):
    """Zeigt eine linksbündige Option mit Rahmen."""
    print(RAHMEN*2 + " " * OPT_EINRUECKUNG + text.ljust(INNENBREITE - OPT_EINRUECKUNG) + RAHMEN*2)
def einr_input(prompt):
    """Nutzt Input mit Rahmen."""
    leer()
    input(RAHMEN*2 + " " * EINRUECKUNG + prompt)
def erstelle_fragen():
    """
    Erstellt u. gibt alle Quiz-Fragen zurück.
    
    Returns:
        list: Liste mit Frage-Objekten für das Quiz
    """
    fragen = [
        Frage(
            fragetext="Wer hat den Linux-Kernel ursprünglich entwickelt?",
            optionen=['Richard Stallman', 'Linus Torvalds', 'Dennis Ritchie', 'Ken Thompson'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Welcher Befehl zeigt die aktuelle Linux-Distribution und Version an?",
            optionen=['uname -a', 'cat /etc/os-release', 'linux --version', 'distribution --info'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Welche Distribution-Familie verwendet das .deb-Paketformat?",
            optionen=['Red Hat Familie', 'Debian Familie', 'SUSE Familie', 'Arch Familie'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Welcher Webserver ist am weitesten verbreitet in der Open-Source-Welt?",
            optionen=['IIS', 'Apache HTTP Server', 'WebLogic', 'WebSphere'],
            richtige_antwort=1,
            kategorie="1.2 Open Source Applications"
        ),
        Frage(
            fragetext="Was bedeutet GPL (General Public License)?",
            optionen=['Software darf nur kostenlos verteilt werden', 'Änderungen müssen unter derselben Lizenz veröffentlicht werden', 'Software darf nicht kommerziell genutzt werden', 'Quellcode muss geheim bleiben'],
            richtige_antwort=1,
            kategorie="1.3 Open Source Licensing"
        ),
        Frage(
            fragetext="Welche der folgenden Lizenzen ist permissiv (nicht Copyleft)?",
            optionen=['GPL', 'MIT', 'LGPL', 'AGPL'],
            richtige_antwort=1,
            kategorie="1.3 Open Source Licensing"
        ),
        Frage(
            fragetext="Welche Desktop-Umgebung wird standardmäßig bei Ubuntu verwendet?",
            optionen=['KDE Plasma', 'GNOME', 'Xfce', 'LXDE'],
            richtige_antwort=1,
            kategorie="1.4 ICT Skills"
        ),
        Frage(
            fragetext="Mit welcher Tastenkombination wechselt man zu einer virtuellen Konsole (tty)?",
            optionen=['Alt + F1-F6', 'Ctrl + Alt + F1-F6', 'Ctrl + F1-F6', 'Shift + F1-F6'],
            richtige_antwort=1,
            kategorie="1.4 ICT Skills"
        ),
        Frage(
            fragetext="Wie setzt man eine Umgebungsvariable für Kindprozesse?",
            optionen=['set VARIABLE=value', 'export VARIABLE=value', 'env VARIABLE=value', 'var VARIABLE=value'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was gibt der Befehl 'echo $PATH' aus?",
            optionen=['Das aktuelle Verzeichnis', 'Die Suchpfade für ausführbare Dateien', 'Den Pfad zur Home-Directory', 'Alle installierten Programme'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Welcher Befehl zeigt den Typ eines Befehls an (alias, builtin, file)?",
            optionen=['which', 'type', 'whereis', 'locate'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Mit welchem Befehl durchsucht man die Man-Pages nach einem Stichwort?",
            optionen=['man -s keyword', 'man -k keyword', 'man -f keyword', 'man -w keyword'],
            richtige_antwort=1,
            kategorie="2.2 Getting Help"
        ),
        Frage(
            fragetext="In welcher Man-Page Sektion findet man Systemaufrufe?",
            optionen=['Sektion 1', 'Sektion 2', 'Sektion 5', 'Sektion 8'],
            richtige_antwort=1,
            kategorie="2.2 Getting Help"
        ),
        Frage(
            fragetext="Was bewirkt der Befehl 'cd -'?",
            optionen=['Wechselt zum Root-Verzeichnis', 'Wechselt zum vorherigen Verzeichnis', 'Wechselt zum Home-Verzeichnis', 'Wechselt eine Ebene nach oben'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Welche Option von 'ls' zeigt versteckte Dateien an?",
            optionen=['ls -h', 'ls -a', 'ls -l', 'ls -r'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Welcher Befehl kopiert rekursiv ein ganzes Verzeichnis?",
            optionen=['cp directory newdir', 'cp -r directory newdir', 'copy -R directory newdir', 'cp -a directory newdir'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Was bewirkt das Wildcard-Muster '?.txt'?",
            optionen=['Alle Dateien die mit .txt enden', 'Dateien mit genau einem Zeichen vor .txt', 'Alle versteckten .txt Dateien', 'Keine Dateien'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Welcher Befehl erstellt ein komprimiertes tar-Archiv mit gzip?",
            optionen=['tar -cf archive.tar.gz files/', 'tar -czf archive.tar.gz files/', 'tar -xzf archive.tar.gz files/', 'gzip -c archive.tar files/'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Wie extrahiert man ein .tar.bz2 Archiv?",
            optionen=['tar -xzf archive.tar.bz2', 'tar -xjf archive.tar.bz2', 'bunzip2 archive.tar.bz2', 'tar -xf archive.tar.bz2'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen tar und gzip?",
            optionen=['Es gibt keinen Unterschied', 'tar archiviert, gzip komprimiert', 'gzip ist schneller', 'tar ist nur für Linux'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Was bewirkt der Redirect '2>&1'?",
            optionen=['Leitet STDOUT nach STDERR', 'Leitet STDERR nach STDOUT', 'Leitet beide nach /dev/null', 'Leitet STDIN nach STDOUT'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Welcher Befehl zeigt die ersten 20 Zeilen einer Datei?",
            optionen=['tail -n 20 file', 'head -n 20 file', 'cat -n 20 file', 'less -n 20 file'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was macht 'grep -v pattern file'?",
            optionen=['Zeigt Zeilen mit dem Muster', 'Zeigt Zeilen OHNE das Muster', 'Zählt die Treffer', 'Zeigt Zeilennummern'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Wie extrahiert man das erste Feld aus /etc/passwd (Benutzernamen)?",
            optionen=['cut -d: -f1 /etc/passwd', 'cut -f1 /etc/passwd', "awk -d: '{print $1}' /etc/passwd", 'grep -f1 /etc/passwd'],
            richtige_antwort=0,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was muss die erste Zeile eines Bash-Scripts sein?",
            optionen=['# Bash Script', '#!/bin/bash', '!#/bin/bash', '<bash>'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was ist in einem Script der Wert von $1?",
            optionen=['Der Script-Name', 'Das erste Argument', 'Die Anzahl der Argumente', 'Der Exit-Status'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was bedeutet LTS bei Ubuntu?",
            optionen=['Linux Terminal System', 'Long Term Support', 'Latest Technology Stack', 'Linux Test Suite'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Wie heißt die erste SATA-Festplatte in Linux?",
            optionen=['/dev/hda', '/dev/sda', '/dev/sda1', '/dev/disk1'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was ist /dev/null?",
            optionen=['Eine leere Datei', 'Ein Device das alle Daten verwirft', 'Eine Null-Partition', 'Ein Netzwerk-Device'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Wo befinden sich Systemkonfigurationsdateien?",
            optionen=['/var', '/etc', '/usr', '/opt'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wo werden System-Logdateien gespeichert?",
            optionen=['/tmp/log', '/var/log', '/etc/log', '/usr/log'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Welcher Befehl zeigt alle laufenden Prozesse an?",
            optionen=['ls -p', 'ps aux', 'proc -a', 'show processes'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Welcher moderne Befehl ersetzt 'ifconfig'?",
            optionen=['netconfig', 'ip addr', 'network -i', 'ipconfig'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Wo werden DNS-Server konfiguriert?",
            optionen=['/etc/hosts', '/etc/resolv.conf', '/etc/dns.conf', '/var/dns'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Welche UID hat der root-Benutzer?",
            optionen=['-1', '0', '1', '1000'],
            richtige_antwort=1,
            kategorie="5.1 Basic Security"
        ),
        Frage(
            fragetext="Wo werden verschlüsselte Passwörter gespeichert?",
            optionen=['/etc/passwd', '/etc/shadow', '/etc/password', '/var/passwd'],
            richtige_antwort=1,
            kategorie="5.1 Basic Security"
        ),
        Frage(
            fragetext="Welcher Befehl erstellt einen Benutzer mit Home-Verzeichnis?",
            optionen=['useradd username', 'useradd -m username', 'adduser username', 'user create username'],
            richtige_antwort=1,
            kategorie="5.2 Creating Users"
        ),
        Frage(
            fragetext="Was bedeutet 'chmod 755 file'?",
            optionen=['rwxrwxrwx', 'rwxr-xr-x', 'rw-r--r--', 'r-xr-xr-x'],
            richtige_antwort=1,
            kategorie="5.3 File Permissions"
        ),
        Frage(
            fragetext="Wie ändert man den Besitzer einer Datei?",
            optionen=['chmod user file', 'chown user file', 'owner user file', 'setowner user file'],
            richtige_antwort=1,
            kategorie="5.3 File Permissions"
        ),
        Frage(
            fragetext="Was bedeutet das Sticky Bit auf einem Verzeichnis?",
            optionen=['Niemand kann Dateien löschen', 'Nur der Owner kann eigene Dateien löschen', 'Das Verzeichnis ist schreibgeschützt', 'Alle Dateien werden ausführbar'],
            richtige_antwort=1,
            kategorie="5.4 Special Permissions"
        ),
        Frage(
            fragetext="Was ist SUID (Set User ID)?",
            optionen=['Datei läuft mit Root-Rechten', 'Datei läuft mit Rechten des Datei-Owners', 'Datei ist nur für einen User sichtbar', 'User ID wird in der Datei gespeichert'],
            richtige_antwort=1,
            kategorie="5.4 Special Permissions"
        ),
        Frage(
            fragetext="Wie wird eine Variable in der Shell OHNE Leerzeichen gesetzt?",
            optionen=['VARIABLE = value', 'VARIABLE=value', 'set VARIABLE = value', '$VARIABLE=value'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Wie macht man ein Script ausführbar?",
            optionen=['chmod +x script.sh', 'execute script.sh', 'run script.sh', 'bash script.sh'],
            richtige_antwort=0,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was gibt $? zurück?",
            optionen=['Prozess-ID', 'Exit-Status des letzten Befehls', 'Anzahl der Argumente', 'Aktueller Benutzer'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Welche Syntax ist korrekt für eine for-Schleife?",
            optionen=['for i in 1 2 3; do echo $i; done', 'for (i=1; i<3; i++) echo $i', 'for i = 1 to 3 do echo $i', 'foreach i in 1 2 3 echo $i'],
            richtige_antwort=0,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was ist /proc in Linux?",
            optionen=['Ein normales Verzeichnis', 'Ein virtuelles Dateisystem für Prozessinformationen', 'Ein Backup-Verzeichnis', 'Ein Log-Verzeichnis'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was macht 'tail -f /var/log/syslog'?",
            optionen=['Zeigt die ersten Zeilen', 'Zeigt die letzten Zeilen und folgt neuen Einträgen', 'Filtert die Datei', 'Löscht alte Einträge'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was zeigt 'ls -l' in der ersten Spalte?",
            optionen=['Dateigröße', 'Dateityp und Permissions', 'Erstellungsdatum', 'Besitzer'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Welches ist eine Open-Source Datenbank?",
            optionen=['Oracle Database', 'MariaDB', 'Microsoft SQL Server', 'DB2'],
            richtige_antwort=1,
            kategorie="1.2 Open Source Applications"
        ),
        Frage(
            fragetext="Was bedeutet 'chmod 644 file'?",
            optionen=['rwxrwxrwx', 'rw-r--r--', 'r--r--r--', 'rwxr-xr-x'],
            richtige_antwort=1,
            kategorie="5.3 File Permissions"
        ),
        Frage(
            fragetext="Mit welchem Befehl testet man die Erreichbarkeit eines Hosts?",
            optionen=['test host', 'ping host', 'connect host', 'reach host'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen 'rm' und 'rmdir'?",
            optionen=['Kein Unterschied', 'rmdir löscht nur leere Verzeichnisse', 'rm ist sicherer', 'rmdir braucht sudo'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Wie zählt man die Anzahl Zeilen in einer Datei?",
            optionen=['count file', 'wc -l file', 'lines file', 'cat -n file'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was macht der Pipe-Operator '|'?",
            optionen=['Verkettet Dateien', 'Leitet STDOUT des ersten Befehls zu STDIN des zweiten', 'Führt Befehle parallel aus', 'Kommentiert Code'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Welches Verzeichnis enthält die Vorlage für neue Home-Verzeichnisse?",
            optionen=['/etc/home', '/etc/skel', '/home/template', '/usr/template'],
            richtige_antwort=1,
            kategorie="5.2 Creating Users"
        ),
        Frage(
            fragetext="Welche Paketmanager verwenden Red Hat basierte Systeme?",
            optionen=['apt und dpkg', 'rpm und yum', 'pacman', 'emerge'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Wo befindet sich das Home-Verzeichnis des root-Benutzers?",
            optionen=['/home/root', '/root', '/', '/etc/root'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wie zeigt man den Inhalt eines tar-Archivs an OHNE zu extrahieren?",
            optionen=['tar -xf archive.tar', 'tar -tf archive.tar', 'tar -cf archive.tar', 'cat archive.tar'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Was macht 'whatis command'?",
            optionen=['Zeigt die Man-Page', 'Zeigt eine einzeilige Beschreibung', 'Zeigt den Speicherort', 'Zeigt alle Optionen'],
            richtige_antwort=1,
            kategorie="2.2 Getting Help"
        ),
        Frage(
            fragetext="Was macht 'sudo command'?",
            optionen=['Wechselt zu root', 'Führt einen Befehl als root aus', 'Ändert das Passwort', 'Zeigt Benutzerinfo'],
            richtige_antwort=1,
            kategorie="5.1 Basic Security"
        ),
        Frage(
            fragetext="Was ist der Kernel in einem Linux-System?",
            optionen=['Die grafische Oberfläche', 'Der Kern des Betriebssystems der Hardware verwaltet', 'Ein Texteditor', 'Die Shell'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Welches Open-Source Office-Paket ist weit verbreitet?",
            optionen=['Microsoft Office', 'LibreOffice', 'WordPerfect', 'Lotus Notes'],
            richtige_antwort=1,
            kategorie="1.2 Open Source Applications"
        ),
        Frage(
            fragetext="Was erlaubt die Apache License 2.0 im Gegensatz zur GPL?",
            optionen=['Keine kommerzielle Nutzung', 'Proprietäre Ableitungen ohne Quellcode-Veröffentlichung', 'Nur private Nutzung', 'Keine Modifikationen'],
            richtige_antwort=1,
            kategorie="1.3 Open Source Licensing"
        ),
        Frage(
            fragetext="Welcher Befehl startet den grafischen Anmeldebildschirm neu?",
            optionen=['restart gdm', 'systemctl restart gdm', 'gdm --restart', 'service gdm reload'],
            richtige_antwort=1,
            kategorie="1.4 ICT Skills"
        ),
        Frage(
            fragetext="Wie greift man auf das zweite Kommandozeilenargument in einem Script zu?",
            optionen=['$1', '$2', '$args[2]', '${2}'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was zeigt 'man -K keyword' im Gegensatz zu 'man -k keyword'?",
            optionen=['Nur Überschriften', 'Durchsucht den gesamten Inhalt aller Man-Pages', 'Zeigt nur Sektionen', 'Schnellere Suche'],
            richtige_antwort=1,
            kategorie="2.2 Getting Help"
        ),
        Frage(
            fragetext="Was macht 'ls -i'?",
            optionen=['Zeigt versteckte Dateien', 'Zeigt Inode-Nummern', 'Zeigt Dateitypen', 'Invertiert die Sortierung'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Was bewirkt 'mv datei1 datei2' wenn datei2 bereits existiert?",
            optionen=['Fehler wird ausgegeben', 'datei2 wird überschrieben', 'Beide Dateien werden zusammengeführt', 'datei1 wird gelöscht'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Wie listet man den Inhalt eines tar-Archivs mit Detailinformationen?",
            optionen=['tar -tf archiv.tar', 'tar -tvf archiv.tar', 'tar -xvf archiv.tar', 'tar -cf archiv.tar'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Was macht 'grep -r pattern directory'?",
            optionen=['Löscht das Muster', 'Durchsucht rekursiv alle Dateien im Verzeichnis', 'Ersetzt das Muster', 'Zählt Vorkommen'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Wie testet man in einem Script ob eine Datei existiert?",
            optionen=['if exists file', 'if [ -e file ]', 'if file.exists()', 'test -e file only'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was ist ein Rolling Release Modell?",
            optionen=['Feste Release-Zyklen', 'Kontinuierliche Updates ohne Versionssprünge', 'Jährliche Updates', 'Beta-Testing'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen /dev/sda und /dev/sda1?",
            optionen=['Kein Unterschied', 'sda ist die Festplatte, sda1 ist die erste Partition', 'sda1 ist schneller', 'sda ist virtuell'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was enthält /usr/local typischerweise?",
            optionen=['Systemdateien', 'Lokal installierte Software', 'Logdateien', 'Temporäre Dateien'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Welcher Port wird standardmäßig für SSH verwendet?",
            optionen=['21', '22', '23', '80'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was ist der Zweck von /etc/sudoers?",
            optionen=['Benutzerpasswörter', 'Konfiguration wer sudo nutzen darf', 'Systemlogs', 'Netzwerkeinstellungen'],
            richtige_antwort=1,
            kategorie="5.1 Basic Security"
        ),
        Frage(
            fragetext="Wie setzt man das Passwort für einen Benutzer?",
            optionen=['password username', 'passwd username', 'setpass username', 'usermod -p username'],
            richtige_antwort=1,
            kategorie="5.2 Creating Users"
        ),
        Frage(
            fragetext="Was bedeutet 'chmod 600 file'?",
            optionen=['rwxrwxrwx', 'rw-------', 'r--r--r--', 'rwxr-xr-x'],
            richtige_antwort=1,
            kategorie="5.3 File Permissions"
        ),
        Frage(
            fragetext="Wie setzt man das SGID-Bit auf ein Verzeichnis?",
            optionen=['chmod 1755 dir', 'chmod 2755 dir', 'chmod 4755 dir', 'chmod g+s dir'],
            richtige_antwort=1,
            kategorie="5.4 Special Permissions"
        ),
        Frage(
            fragetext="Was macht 'cd ~'?",
            optionen=['Wechselt zu /tmp', 'Wechselt zum Home-Verzeichnis des Users', 'Wechselt zu /root', 'Zeigt das aktuelle Verzeichnis'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Welcher Befehl zeigt die Route zu einem Host?",
            optionen=['route host', 'traceroute host', 'path host', 'netstat host'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was macht 'find / -name file.txt'?",
            optionen=['Sucht ab Root nach file.txt', 'Löscht file.txt', 'Kopiert file.txt', 'Zeigt Dateiinfo'],
            richtige_antwort=0,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Wie leitet man STDOUT in eine Datei um und hängt an (append)?",
            optionen=['command > file', 'command >> file', 'command >+ file', 'command < file'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was ist /tmp und welche Eigenschaft hat es?",
            optionen=['Permanenter Speicher', 'Temporäres Verzeichnis, wird bei Reboot gelöscht', 'Backup-Verzeichnis', 'Logverzeichnis'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Welches Verzeichnis enthält ausführbare Binärdateien für alle User?",
            optionen=['/etc', '/usr/bin', '/var', '/opt'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wie zeigt man alle Netzwerkverbindungen an?",
            optionen=['connections', 'netstat -a', 'network -show', 'ip connections'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was macht 'usermod -aG gruppe user'?",
            optionen=['Entfernt User aus Gruppe', 'Fügt User zu zusätzlicher Gruppe hinzu', 'Löscht die Gruppe', 'Erstellt neue Gruppe'],
            richtige_antwort=1,
            kategorie="5.2 Creating Users"
        ),
        Frage(
            fragetext="Wie entfernt man rekursiv alle Schreibrechte für group und others?",
            optionen=['chmod 755 -R dir', 'chmod -R go-w dir', 'chmod -w dir', 'chmod 644 -R dir'],
            richtige_antwort=1,
            kategorie="5.3 File Permissions"
        ),
        Frage(
            fragetext="Was ist der Zweck von /etc/group?",
            optionen=['Benutzerpasswörter', 'Gruppendefinitionen und Mitgliedschaften', 'Systemlogs', 'Netzwerkgruppen'],
            richtige_antwort=1,
            kategorie="5.2 Creating Users"
        ),
        Frage(
            fragetext="Wie sucht man nach allen Dateien mit SUID-Bit?",
            optionen=['find / -perm 644', 'find / -perm /4000', 'grep suid /', 'ls -suid /'],
            richtige_antwort=1,
            kategorie="5.4 Special Permissions"
        ),
        Frage(
            fragetext="Was ist GNU in GNU/Linux?",
            optionen=['Ein Kernel', 'Eine Sammlung von freien Unix-Tools und Utilities', 'Eine Distribution', 'Ein Dateisystem'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Welche Distribution verwendet pacman als Paketmanager?",
            optionen=['Debian', 'Arch Linux', 'Fedora', 'Ubuntu'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Was ist Samba?",
            optionen=['Ein Texteditor', 'Open-Source Implementierung von SMB/CIFS für Dateifreigaben', 'Eine Datenbank', 'Ein Webserver'],
            richtige_antwort=1,
            kategorie="1.2 Open Source Applications"
        ),
        Frage(
            fragetext="Was ist GIMP?",
            optionen=['Ein Compiler', 'Open-Source Bildbearbeitungsprogramm', 'Ein Paketmanager', 'Eine Shell'],
            richtige_antwort=1,
            kategorie="1.2 Open Source Applications"
        ),
        Frage(
            fragetext="Was bedeutet Copyleft?",
            optionen=['Software darf nicht kopiert werden', 'Abgeleitete Werke müssen unter gleicher Lizenz bleiben', 'Software ist gemeinfrei', 'Nur Linksklick erlaubt'],
            richtige_antwort=1,
            kategorie="1.3 Open Source Licensing"
        ),
        Frage(
            fragetext="Welche Lizenz nutzt der Linux-Kernel?",
            optionen=['MIT', 'GPL v2', 'BSD', 'Apache 2.0'],
            richtige_antwort=1,
            kategorie="1.3 Open Source Licensing"
        ),
        Frage(
            fragetext="Was ist X11/Xorg?",
            optionen=['Ein Dateisystem', 'Ein Display-Server für grafische Oberflächen', 'Ein Netzwerkprotokoll', 'Ein Editor'],
            richtige_antwort=1,
            kategorie="1.4 ICT Skills"
        ),
        Frage(
            fragetext="Was ist Wayland?",
            optionen=['Ein Browser', 'Moderner Display-Server-Protokoll', 'Eine Distribution', 'Ein Paketmanager'],
            richtige_antwort=1,
            kategorie="1.4 ICT Skills"
        ),
        Frage(
            fragetext="Wie zeigt man alle gesetzten Umgebungsvariablen an?",
            optionen=['show env', 'env oder printenv', 'vars', 'echo $ALL'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was macht die Tilde (~) in Pfadangaben?",
            optionen=['Nichts', 'Steht für das Home-Verzeichnis', 'Steht für Root', 'Steht für aktuelles Verzeichnis'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Wie zeigt man alle verfügbaren Man-Page Sektionen zu einem Thema?",
            optionen=['man -s topic', 'man -a topic', 'man --all topic', 'man -l topic'],
            richtige_antwort=1,
            kategorie="2.2 Getting Help"
        ),
        Frage(
            fragetext="Was ist info im Vergleich zu man?",
            optionen=['Gleiche Funktion', 'Alternatives Dokumentationssystem mit Hyperlinks', 'Schnellere Version', 'Nur für Kernel-Docs'],
            richtige_antwort=1,
            kategorie="2.2 Getting Help"
        ),
        Frage(
            fragetext="Was zeigt 'pwd'?",
            optionen=['Passwort', 'Print Working Directory - aktuelles Verzeichnis', 'Power Down', 'Process Watch Display'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Was macht 'ls -R'?",
            optionen=['Sortiert umgekehrt', 'Listet rekursiv alle Unterverzeichnisse', 'Zeigt nur Verzeichnisse', 'Zeigt Rechteinformationen'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Wie erstellt man mehrere verschachtelte Verzeichnisse auf einmal?",
            optionen=['mkdir dir1/dir2/dir3', 'mkdir -p dir1/dir2/dir3', 'mkdir -r dir1/dir2/dir3', 'mkdirs dir1/dir2/dir3'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Was macht 'touch datei'?",
            optionen=['Löscht die Datei', 'Erstellt leere Datei oder aktualisiert Zeitstempel', 'Öffnet die Datei', 'Zeigt Dateiinhalt'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Wie erstellt man ein bzip2-komprimiertes tar-Archiv?",
            optionen=['tar -czf archiv.tar.bz2 files/', 'tar -cjf archiv.tar.bz2 files/', 'tar -cxf archiv.tar.bz2 files/', 'bzip2 -c files/'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen gzip und bzip2?",
            optionen=['Kein Unterschied', 'bzip2 komprimiert besser, ist aber langsamer', 'gzip ist neuer', 'bzip2 funktioniert nur mit tar'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Was macht 'grep -i pattern file'?",
            optionen=['Ignoriert leere Zeilen', 'Sucht case-insensitive', 'Zeigt nur Dateinamen', 'Invertiert die Suche'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Wie zeigt man nur eindeutige Zeilen in einer Datei?",
            optionen=['unique file', 'sort file | uniq', 'uniq file', 'grep -u file'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was macht 'sed s/alt/neu/g file'?",
            optionen=['Löscht Zeilen', 'Ersetzt alle Vorkommen von alt durch neu', 'Sucht nach alt', 'Sortiert die Datei'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Wie kommentiert man in Bash-Scripts?",
            optionen=['// Kommentar', '# Kommentar', '/* Kommentar */', '-- Kommentar'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was ist $# in einem Script?",
            optionen=['Prozess-ID', 'Anzahl der übergebenen Argumente', 'Exit-Status', 'Aktueller User'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Wie testet man ob eine Variable leer ist?",
            optionen=['if [ $var ]', 'if [ -z $var ]', 'if empty($var)', 'if [ $var == empty ]'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen [ ] und [[ ]]?",
            optionen=['Kein Unterschied', '[[ ]] ist moderner und sicherer in Bash', '[ ] ist schneller', '[[ ]] funktioniert nur in sh'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was ist eine Live-Distribution?",
            optionen=['Immer online', 'Linux von CD/USB ohne Installation lauffähig', 'Nur für Streaming', 'Beta-Version'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was ist ein Hypervisor?",
            optionen=['Schneller Prozessor', 'Software zur Virtualisierung von Betriebssystemen', 'Netzwerkgerät', 'Grafikbeschleuniger'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was zeigt 'lsblk'?",
            optionen=['Netzwerkblöcke', 'Block-Devices und Partitionen in Baumstruktur', 'Prozesse', 'Benutzer'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was zeigt 'lscpu'?",
            optionen=['Festplatten', 'CPU-Informationen', 'Speicherauslastung', 'Netzwerkkarten'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was ist /dev/random?",
            optionen=['Zufallsgerät', 'Pseudo-Device für Zufallszahlen', 'Backup-Gerät', 'Log-Gerät'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was enthält /boot?",
            optionen=['Startskripte', 'Kernel und Boot-Loader Dateien', 'Systemlogs', 'Temporäre Dateien'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen /bin und /usr/bin?",
            optionen=['Kein Unterschied mehr in modernen Systemen', '/bin für essentielle, /usr/bin für zusätzliche Programme', '/bin ist schneller', '/usr/bin nur für root'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wie zeigt man die Routing-Tabelle an?",
            optionen=['show route', 'ip route show oder route -n', 'netstat -r only', 'routing --show'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was macht 'hostname'?",
            optionen=['Zeigt IP-Adresse', 'Zeigt oder setzt den Hostnamen', 'Startet Netzwerk neu', 'Zeigt DNS-Server'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was ist der Zweck von /etc/hosts?",
            optionen=['Zeigt alle Hosts im Netzwerk', 'Lokale DNS-Auflösung von Namen zu IPs', 'Liste erlaubter Hosts', 'Netzwerkkonfiguration'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was macht 'su - username'?",
            optionen=['Zeigt User-Info', 'Wechselt zu User mit dessen Umgebung', 'Löscht User', 'Sperrt User'],
            richtige_antwort=1,
            kategorie="5.1 Basic Security"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen 'su' und 'su -'?",
            optionen=['Kein Unterschied', 'su - lädt die komplette Login-Umgebung', 'su ist schneller', 'su - braucht kein Passwort'],
            richtige_antwort=1,
            kategorie="5.1 Basic Security"
        ),
        Frage(
            fragetext="Wie zeigt man alle Gruppen eines Users?",
            optionen=['showgroups user', 'groups user oder id user', 'usergroups user', 'cat /etc/group | grep user'],
            richtige_antwort=1,
            kategorie="5.2 Creating Users"
        ),
        Frage(
            fragetext="Was macht 'chgrp gruppe datei'?",
            optionen=['Ändert Permissions', 'Ändert die Gruppe der Datei', 'Löscht die Gruppe', 'Erstellt Gruppe'],
            richtige_antwort=1,
            kategorie="5.3 File Permissions"
        ),
        Frage(
            fragetext="Was bedeutet das 't' in 'drwxrwxrwt'?",
            optionen=['Temporär', 'Sticky Bit ist gesetzt', 'Textdatei', 'Ausführbar'],
            richtige_antwort=1,
            kategorie="5.4 Special Permissions"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen Hard Link und Symbolic Link?",
            optionen=['Kein Unterschied', 'Hard Link zeigt auf Inode, Symlink auf Pfad', 'Hard Link ist schneller', 'Symlink nur für Verzeichnisse'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Wie erstellt man einen symbolischen Link?",
            optionen=['link ziel link_name', 'ln -s ziel link_name', 'symlink ziel link_name', 'ln ziel link_name'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Was macht 'df -h'?",
            optionen=['Zeigt Dateien', 'Zeigt Festplattennutzung in lesbarem Format', 'Löscht Dateien', 'Defragmentiert'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was macht 'du -sh verzeichnis'?",
            optionen=['Löscht Verzeichnis', 'Zeigt Größe des Verzeichnisses zusammengefasst', 'Dupliziert Verzeichnis', 'Durchsucht Verzeichnis'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Wie mountet man ein Dateisystem?",
            optionen=['mount /dev/sdb1', 'mount /dev/sdb1 /mnt/punkt', 'attach /dev/sdb1', 'connect /dev/sdb1'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Wie unmountet man ein Dateisystem?",
            optionen=['unmount /mnt/punkt', 'umount /mnt/punkt', 'detach /mnt/punkt', 'disconnect /mnt/punkt'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was zeigt 'free -h'?",
            optionen=['Freier Speicherplatz auf Festplatte', 'RAM- und Swap-Nutzung in lesbarem Format', 'Freie Prozesse', 'Freie Ports'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was macht 'kill -9 PID'?",
            optionen=['Startet Prozess neu', 'Beendet Prozess sofort (SIGKILL)', 'Pausiert Prozess', 'Zeigt Prozessinfo'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was macht 'killall programm'?",
            optionen=['Löscht das Programm', 'Beendet alle Prozesse mit diesem Namen', 'Zeigt alle Prozesse', 'Startet das Programm'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was zeigt 'top'?",
            optionen=['Oberste Dateien', 'Laufende Prozesse in Echtzeit', 'Höchste Verzeichnisse', 'Top-User'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was macht 'nice -n 10 befehl'?",
            optionen=['Macht Befehl freundlicher', 'Startet Befehl mit niedriger Priorität', 'Beschleunigt Befehl', 'Verzögert Befehl um 10s'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wie startet man einen Prozess im Hintergrund?",
            optionen=['befehl background', 'befehl &', 'bg befehl', 'befehl -b'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was macht 'jobs'?",
            optionen=['Zeigt freie Stellen', 'Zeigt Hintergrund-Jobs der aktuellen Shell', 'Erstellt Jobs', 'Löscht Jobs'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was macht 'fg %1'?",
            optionen=['Löscht Job 1', 'Holt Job 1 in den Vordergrund', 'Startet Job 1', 'Zeigt Job 1 Info'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was macht 'nohup befehl &'?",
            optionen=['Verhindert Ausgabe', 'Befehl läuft weiter nach Terminal-Schließung', 'Befehl wird nicht ausgeführt', 'Befehl läuft mit höherer Priorität'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was ist systemd?",
            optionen=['Systemdatei', 'Init-System und Service-Manager', 'Systemfestplatte', 'Daemon für Devices'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Wie startet man einen Service mit systemd?",
            optionen=['service start name', 'systemctl start name', 'start name', 'daemon start name'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Wie aktiviert man einen Service beim Systemstart?",
            optionen=['systemctl boot name', 'systemctl enable name', 'systemctl autostart name', 'service enable name'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was zeigt 'systemctl status name'?",
            optionen=['Systemstatus', 'Status eines Services', 'Status aller Services', 'Benutzerstatus'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was zeigt 'journalctl'?",
            optionen=['Journal-Dateien', 'Systemd Journal-Logs', 'Benutzer-Journals', 'Cron-Logs'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wie lädt man eine Webseite mit der Kommandozeile herunter?",
            optionen=['download URL', 'wget URL oder curl -O URL', 'get URL', 'fetch URL'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Wie verbindet man sich per SSH zu einem Server?",
            optionen=['connect user@host', 'ssh user@host', 'remote user@host', 'login user@host'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Wie kopiert man eine Datei über SSH?",
            optionen=['cp user@host:file .', 'scp user@host:file .', 'ssh cp user@host:file .', 'copy user@host:file .'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was ist der Standard-Port für HTTP?",
            optionen=['21', '80', '443', '8080'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was ist der Standard-Port für HTTPS?",
            optionen=['80', '443', '8443', '22'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Wie öffnet man eine Datei in vi/vim?",
            optionen=['open datei', 'vi datei oder vim datei', 'edit datei', 'view datei'],
            richtige_antwort=1,
            kategorie="1.4 ICT Skills"
        ),
        Frage(
            fragetext="Wie speichert und beendet man vi/vim?",
            optionen=[':sq', ':wq oder ZZ', ':save', ':exit'],
            richtige_antwort=1,
            kategorie="1.4 ICT Skills"
        ),
        Frage(
            fragetext="Wie beendet man vi/vim ohne zu speichern?",
            optionen=[':q', ':q!', ':exit!', ':quit'],
            richtige_antwort=1,
            kategorie="1.4 ICT Skills"
        ),
        Frage(
            fragetext="Was ist nano?",
            optionen=['Kleines Programm', 'Einfacher Kommandozeilen-Texteditor', 'Dateisystem', 'Netzwerktool'],
            richtige_antwort=1,
            kategorie="1.4 ICT Skills"
        ),
        Frage(
            fragetext="Was zeigt 'cat datei'?",
            optionen=['Kategorisiert Datei', 'Zeigt Dateiinhalt an', 'Verbindet Dateien', 'Katalogisiert Datei'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen 'more' und 'less'?",
            optionen=['Kein Unterschied', 'less erlaubt Vor- und Rückwärtsnavigation', 'more ist neuer', 'less ist langsamer'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was macht 'tee datei'?",
            optionen=['Teilt Dateien', 'Schreibt STDIN zu STDOUT und in Datei', 'Zeigt drei Dateien', 'Testet Dateien'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was ist /etc/fstab?",
            optionen=['Schnelle Tabelle', 'Konfiguration für automatisches Mounten', 'Dateisystem-Test', 'Backup-Tabelle'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was macht 'alias ll=\"ls -la\"'?",
            optionen=['Benennt Datei um', 'Erstellt Kurzbefehls-Alias', 'Linked Befehle', 'Listet Aliase'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Wie zeigt man alle gesetzten Aliase?",
            optionen=['show alias', 'alias', 'list aliases', 'aliases -a'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was macht 'history'?",
            optionen=['Zeigt Systemgeschichte', 'Zeigt Befehlshistorie der Shell', 'Zeigt Login-Historie', 'Zeigt Datei-Historie'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Wie führt man den letzten Befehl erneut aus?",
            optionen=['repeat', '!!', 'again', 'last'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was macht 'uname -r'?",
            optionen=['Zeigt Benutzernamen', 'Zeigt Kernel-Version', 'Zeigt Releasenummer', 'Entfernt Name'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was zeigt 'uptime'?",
            optionen=['Update-Zeit', 'Laufzeit des Systems und Load Average', 'Zeitzone', 'Upload-Zeit'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was zeigt 'dmesg'?",
            optionen=['Disk-Meldungen', 'Kernel-Ring-Buffer Nachrichten', 'Daemon-Meldungen', 'Debug-Meldungen'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was macht 'apt update'?",
            optionen=['Updated alle Pakete', 'Aktualisiert Paketlisten', 'Updated System', 'Updated Kernel'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Was macht 'apt upgrade'?",
            optionen=['Upgraded Distribution', 'Installiert verfügbare Paket-Updates', 'Upgraded Kernel', 'Upgraded nur wichtige Pakete'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Wie installiert man ein Paket mit apt?",
            optionen=['apt get paket', 'apt install paket', 'apt add paket', 'apt setup paket'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Wie entfernt man ein Paket mit apt?",
            optionen=['apt delete paket', 'apt remove paket', 'apt uninstall paket', 'apt erase paket'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Was macht 'dpkg -l'?",
            optionen=['Löscht Pakete', 'Listet installierte Pakete', 'Lädt Pakete', 'Loggt Pakete'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Was ist ein Repository?",
            optionen=['Recycling-Ordner', 'Paketquelle für Software', 'Backup-Speicher', 'Report-System'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Wo werden apt-Repositorys konfiguriert?",
            optionen=['/etc/apt/repos', '/etc/apt/sources.list', '/var/apt/sources', '/usr/apt/config'],
            richtige_antwort=1,
            kategorie="1.1 Linux Evolution"
        ),
        Frage(
            fragetext="Was ist cron?",
            optionen=['Chronometer', 'Zeitbasierter Job-Scheduler', 'Crash-Logger', 'Config-Runner'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wie bearbeitet man die crontab eines Users?",
            optionen=['edit crontab', 'crontab -e', 'vi /etc/crontab', 'nano crontab'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was bedeutet '* * * * *' in crontab?",
            optionen=['Alle 5 Sekunden', 'Jede Minute', 'Einmal täglich', 'Jede Stunde'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was macht 'zip archiv.zip dateien'?",
            optionen=['Entpackt Archiv', 'Erstellt ZIP-Archiv', 'Testet Archiv', 'Zeigt Archiv'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Wie entpackt man ein ZIP-Archiv?",
            optionen=['zip -x archiv.zip', 'unzip archiv.zip', 'extract archiv.zip', 'zip -d archiv.zip'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Was ist umask?",
            optionen=['Unmount-Maske', 'Standard-Berechtigungen für neue Dateien', 'User-Maske', 'Unicode-Maske'],
            richtige_antwort=1,
            kategorie="5.3 File Permissions"
        ),
        Frage(
            fragetext="Was macht 'grep -n pattern file'?",
            optionen=['Zeigt Anzahl', 'Zeigt Zeilennummern mit Treffern', 'Sucht nach Zahlen', 'Negiert Suche'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was macht 'grep -c pattern file'?",
            optionen=['Zeigt Kontext', 'Zählt Anzahl der Treffer', 'Zeigt Zeichen', 'Erstellt Kopie'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was ist /etc/passwd?",
            optionen=['Password-Datei mit verschlüsselten Passwörtern', 'User-Account-Informationen', 'Password-Generator', 'Password-Policy'],
            richtige_antwort=1,
            kategorie="5.2 Creating Users"
        ),
        Frage(
            fragetext="Wie viele Felder hat jede Zeile in /etc/passwd?",
            optionen=['5', '7', '10', '3'],
            richtige_antwort=1,
            kategorie="5.2 Creating Users"
        ),
        Frage(
            fragetext="Was ist der Zweck von /etc/login.defs?",
            optionen=['Login-Logs', 'Standard-Konfiguration für User-Erstellung', 'Login-Definitionen', 'Default-Shell'],
            richtige_antwort=1,
            kategorie="5.2 Creating Users"
        ),
        Frage(
            fragetext="Was ist der Zweck von /opt?",
            optionen=['Optionale Dateien', 'Zusätzliche/optionale Software-Pakete', 'Optimierte Programme', 'Temporäre Optionen'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was macht 'chmod u+x datei'?",
            optionen=['Entfernt Execute-Recht', 'Fügt Execute-Recht für User hinzu', 'Fügt alle Rechte hinzu', 'Entfernt alle Rechte'],
            richtige_antwort=1,
            kategorie="5.3 File Permissions"
        ),
        Frage(
            fragetext="Was ist der Standard-Port für FTP?",
            optionen=['20', '21', '22', '23'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was macht 'ps -ef'?",
            optionen=['Zeigt Fehler', 'Zeigt alle Prozesse im Full-Format', 'Entfernt Prozesse', 'Editiert Prozesse'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wie beendet man einen Prozess mit SIGTERM?",
            optionen=['kill -9 PID', 'kill -15 PID oder kill PID', 'stop PID', 'end PID'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was ist /sys in Linux?",
            optionen=['System-Backup', 'Virtuelles Dateisystem für Kernel/Hardware-Info', 'System-Programme', 'Synchronisations-Ordner'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was macht 'awk '{print $1}' datei'?",
            optionen=['Druckt Datei', 'Gibt die erste Spalte jeder Zeile aus', 'Druckt erste Zeile', 'Gibt erstes Zeichen aus'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen .bashrc und .bash_profile?",
            optionen=['Kein Unterschied', '.bash_profile für Login-Shells, .bashrc für interaktive Shells', '.bashrc ist neuer', '.bash_profile nur für root'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was macht 'source datei' oder '. datei'?",
            optionen=['Zeigt Quellcode', 'Führt Script in aktueller Shell aus', 'Kopiert Datei', 'Sucht Datei'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Wie fügt man Text am Ende einer Datei hinzu ohne Editor?",
            optionen=['echo text > datei', 'echo text >> datei', 'echo text < datei', 'add text datei'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was ist die Funktion von 'xargs'?",
            optionen=['Zeigt Argumente', 'Baut Befehlszeilen aus STDIN und führt sie aus', 'Exportiert Variablen', 'Löscht Argumente'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was macht 'ln datei1 datei2' (ohne -s)?",
            optionen=['Kopiert Datei', 'Erstellt Hard Link', 'Erstellt Symlink', 'Linked Verzeichnisse'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Was ist der Unterschied zwischen /sbin und /bin?",
            optionen=['Kein Unterschied', '/sbin für System-Admin-Befehle, /bin für User-Befehle', '/sbin ist schneller', '/sbin nur temporär'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Was macht 'dd if=/dev/zero of=file bs=1M count=10'?",
            optionen=['Löscht 10MB', 'Erstellt 10MB Datei mit Nullen', 'Komprimiert Datei', 'Dupliziert Datei'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Was ist rsync?",
            optionen=['Zufalls-Sync', 'Effizienter Datei-Synchronisations-Befehl', 'Reboot-System', 'Registry-Sync'],
            richtige_antwort=1,
            kategorie="2.4 Creating/Moving Files"
        ),
        Frage(
            fragetext="Wie zeigt man die Größe aller Dateien in einem Verzeichnis sortiert?",
            optionen=['ls -S', 'du -h * | sort -h', 'size *', 'ls -size'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Was macht 'basename /pfad/zu/datei.txt'?",
            optionen=['Zeigt Basisrechte', 'Gibt nur den Dateinamen aus', 'Zeigt Pfad', 'Ändert Namen'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was macht 'dirname /pfad/zu/datei.txt'?",
            optionen=['Zeigt Verzeichnisgröße', 'Gibt nur den Pfad ohne Dateinamen aus', 'Löscht Verzeichnis', 'Erstellt Verzeichnis'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was ist der Exit-Status 0?",
            optionen=['Fehler', 'Erfolgreiche Ausführung', 'Warnung', 'Abbruch'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Wie testet man in einem Script ob ein Verzeichnis existiert?",
            optionen=['if [ -f dir ]', 'if [ -d dir ]', 'if exists dir', 'if dir.exists'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was ist $$ in einem Script?",
            optionen=['Exit-Status', 'Prozess-ID des Scripts', 'Anzahl Argumente', 'Letzter Befehl'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was macht 'sleep 5'?",
            optionen=['Suspendiert System', 'Pausiert für 5 Sekunden', 'Schließt Prozesse', 'Startet nach 5s neu'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Was ist /dev/tty?",
            optionen=['Test-Terminal', 'Aktuelles Terminal des Prozesses', 'Temporäres Device', 'Text-Terminal'],
            richtige_antwort=1,
            kategorie="4.2 Computer Hardware"
        ),
        Frage(
            fragetext="Wie zeigt man nur Verzeichnisse mit ls?",
            optionen=['ls -d', 'ls -d */', 'ls --dirs', 'ls -folders'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Was macht 'file datei'?",
            optionen=['Öffnet Datei', 'Bestimmt den Dateityp', 'Filtert Datei', 'Findet Dateien'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Was ist shebang (#!)?",
            optionen=['Shell-Bang', 'Zeile die Interpreter für Script angibt', 'Kommentar', 'Variablendeklaration'],
            richtige_antwort=1,
            kategorie="3.3 Shell Scripting"
        ),
        Frage(
            fragetext="Wie macht man einen Befehl zu einem Alias permanent?",
            optionen=['alias -p befehl', 'Eintrag in ~/.bashrc oder ~/.bash_aliases', 'save alias befehl', 'permanent alias befehl'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was zeigt 'who'?",
            optionen=['Wer bin ich', 'Eingeloggte Benutzer', 'Alle Benutzer', 'Benutzerrechte'],
            richtige_antwort=1,
            kategorie="5.1 Basic Security"
        ),
        Frage(
            fragetext="Was zeigt 'whoami'?",
            optionen=['Alle User', 'Aktueller Benutzername', 'User-ID', 'Benutzergruppen'],
            richtige_antwort=1,
            kategorie="5.1 Basic Security"
        ),
        Frage(
            fragetext="Was macht 'last'?",
            optionen=['Letzter Befehl', 'Zeigt Login-Historie', 'Letzte Datei', 'Letzter Prozess'],
            richtige_antwort=1,
            kategorie="5.1 Basic Security"
        ),
        Frage(
            fragetext="Was ist /var/spool?",
            optionen=['Variable Pools', 'Warteschlangen für Print/Mail etc.', 'Backup-Speicher', 'Temporäre Dateien'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wie findet man große Dateien (über 100MB)?",
            optionen=['ls -large', 'find / -size +100M', 'locate --big', 'search --size 100M'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was macht 'locate dateiname'?",
            optionen=['Zeigt Speicherort', 'Durchsucht Datenbank nach Dateinamen', 'Erstellt lokale Kopie', 'Sperrt Datei'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Wie aktualisiert man die locate-Datenbank?",
            optionen=['locate --update', 'updatedb', 'locate -refresh', 'dbupdate'],
            richtige_antwort=1,
            kategorie="3.2 Searching and Extracting"
        ),
        Frage(
            fragetext="Was ist /etc/profile?",
            optionen=['Benutzerprofile', 'System-weite Shell-Konfiguration für Login-Shells', 'Netzwerkprofile', 'Profiling-Daten'],
            richtige_antwort=1,
            kategorie="2.1 Command Line Basics"
        ),
        Frage(
            fragetext="Was macht 'reboot' oder 'shutdown -r now'?",
            optionen=['Beendet System', 'Startet System neu', 'Rebootet Dienst', 'Löscht Logs'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was macht 'shutdown -h now'?",
            optionen=['Hilfe anzeigen', 'Fährt System herunter (halt)', 'Startet neu', 'Hibernate'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was ist init?",
            optionen=['Initialisierung', 'Erster Prozess beim Systemstart (PID 1)', 'Internet-Init', 'Interface-Init'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was sind Runlevel?",
            optionen=['Lauf-Geschwindigkeiten', 'Betriebsmodi des Systems (0-6)', 'Prozess-Level', 'User-Level'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was ist Runlevel 0?",
            optionen=['Normal-Betrieb', 'System herunterfahren', 'Single-User-Mode', 'Reboot'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was ist Runlevel 6?",
            optionen=['Grafischer Modus', 'Reboot', 'Shutdown', 'Multi-User'],
            richtige_antwort=1,
            kategorie="4.1 Choosing an OS"
        ),
        Frage(
            fragetext="Was macht 'lsof'?",
            optionen=['Listet offene Dateien', 'Listet offene Dateien und Prozesse die sie nutzen', 'Listet Logs', 'Listet Optionen'],
            richtige_antwort=1,
            kategorie="4.3 Where Data is Stored"
        ),
        Frage(
            fragetext="Wie findet man welcher Prozess einen Port nutzt?",
            optionen=['port 80', 'lsof -i :80 oder netstat -tlnp | grep :80', 'find port 80', 'ps port 80'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was ist MAC-Adresse?",
            optionen=['MacOS Adresse', 'Media Access Control - Hardware-Adresse der Netzwerkkarte', 'Master Access Code', 'Multi-Access Channel'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was macht 'ifconfig eth0 down'?",
            optionen=['Lädt Interface', 'Deaktiviert Netzwerk-Interface eth0', 'Zeigt Download', 'Dokumentiert Interface'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was ist DHCP?",
            optionen=['Direct Host Control', 'Dynamic Host Configuration Protocol - automatische IP-Vergabe', 'Disk Hardware Config', 'Database Host Connection'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
            fragetext="Was macht 'tar --exclude=muster -czf archiv.tar.gz verzeichnis/'?",
            optionen=['Extrahiert ohne Muster', 'Erstellt Archiv und schließt Dateien mit Muster aus', 'Zeigt ausgeschlossene Dateien', 'Löscht Muster'],
            richtige_antwort=1,
            kategorie="3.1 Archiving Files"
        ),
        Frage(
            fragetext="Was macht 'stat datei'?",
            optionen=['Startet Datei', 'Zeigt detaillierte Datei-Statistiken und Metadaten', 'Status der Datei', 'Sortiert Statistiken'],
            richtige_antwort=1,
            kategorie="2.3 Directories and Listing"
        ),
        Frage(
            fragetext="Was ist /etc/hostname?",
            optionen=['Host-Historie', 'Datei mit dem Systemhostnamen', 'Netzwerk-Hosts', 'Hostname-Backup'],
            richtige_antwort=1,
            kategorie="4.4 Computer on Network"
        ),
        Frage(
        fragetext="Was ist Raspbian (jetzt Raspberry Pi OS)?",
        optionen=['Ein Webserver', 'Linux-Distribution für Raspberry Pi', 'Ein Paketmanager', 'Ein Dateisystem'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Welches Betriebssystem nutzt Android als Basis?",
        optionen=['Windows Kernel', 'Linux-Kernel', 'BSD-Kernel', 'Eigener Kernel'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Was ist ein typisches Embedded System mit Linux?",
        optionen=['Desktop-PC', 'Raspberry Pi oder Router', 'Mainframe', 'Supercomputer'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Welche Distribution ist speziell für Anfänger und basiert auf Ubuntu?",
        optionen=['Arch Linux', 'Linux Mint', 'Gentoo', 'Slackware'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Was ist Scientific Linux?",
        optionen=['Linux für Schulen', 'RHEL-Rebuild für wissenschaftliche Institute', 'Mathematik-Software', 'Testing-Distribution'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    
    # === MAJOR OPEN SOURCE APPLICATIONS (1.2) ===
    Frage(
        fragetext="Was ist Nextcloud?",
        optionen=['Texteditor', 'Open-Source Cloud-Speicher und Collaboration-Plattform', 'Webserver', 'Datenbank'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Was ist ownCloud?",
        optionen=['Cloud-Provider', 'Open-Source File-Sync und Share-Lösung', 'Backup-Tool', 'Virtualisierung'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Welcher Webserver ist neben Apache sehr beliebt?",
        optionen=['IIS', 'NGINX', 'WebLogic', 'Tomcat'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Was ist NFS?",
        optionen=['New File System', 'Network File System - für Netzwerk-Dateifreigaben', 'Not For Sale', 'Network Firewall System'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Welcher Open-Source Browser wird von Mozilla entwickelt?",
        optionen=['Chrome', 'Firefox', 'Safari', 'Edge'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Was ist Thunderbird?",
        optionen=['Datenbank', 'Open-Source E-Mail-Client', 'Webserver', 'Dateisystem'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Was ist MySQL?",
        optionen=['Texteditor', 'Open-Source Relationale Datenbank', 'Webserver', 'Programmiersprache'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Welche Programmiersprache ist interpretiert und für Web-Backend beliebt?",
        optionen=['C', 'PHP', 'Assembly', 'Pascal'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Welche Programmiersprache wird oft für System-Administration und Scripting verwendet?",
        optionen=['Java', 'Python', 'C++', 'COBOL'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Was ist Perl?",
        optionen=['Dateisystem', 'Programmiersprache für Text-Verarbeitung', 'Datenbank', 'Webserver'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    Frage(
        fragetext="Welche Sprache läuft im Browser (Client-Side)?",
        optionen=['PHP', 'JavaScript', 'C', 'Bash'],
        richtige_antwort=1,
        kategorie="1.2 Open Source Applications"
    ),
    
    # === PACKAGE MANAGEMENT ERWEITERT (1.2) ===
    Frage(
        fragetext="Welcher Paketmanager ersetzt yum in modernen Fedora/RHEL 8+?",
        optionen=['apt', 'dnf', 'pacman', 'zypper'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Was sind Dependencies in der Paketverwaltung?",
        optionen=['Duplikate', 'Abhängige Pakete die benötigt werden', 'Alte Versionen', 'Backups'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Welcher Paketmanager wird bei SUSE/openSUSE verwendet?",
        optionen=['apt', 'zypper', 'dnf', 'pacman'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Was ist YaST?",
        optionen=['Yet another Shell Tool', 'SUSE Konfigurations- und Administrations-Tool', 'Paketformat', 'Dateisystem'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Was macht 'apt search paketname'?",
        optionen=['Löscht Paket', 'Sucht nach Paketen in Repositories', 'Installiert Paket', 'Updated Paket'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Was ist der Unterschied zwischen apt-get und apt?",
        optionen=['Kein Unterschied', 'apt ist neuere benutzerfreundlichere Version', 'apt-get ist schneller', 'apt nur für Ubuntu'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    
    # === DISTRIBUTIONEN DETAILS (1.1) ===
    Frage(
        fragetext="Was ist Fedora?",
        optionen=['Debian-basiert', 'Community-Distribution gesponsert von Red Hat', 'Ubuntu-Fork', 'BSD-System'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Was ist der Unterschied zwischen CentOS und RHEL?",
        optionen=['Kein Unterschied', 'CentOS ist freier RHEL-Rebuild ohne Support', 'RHEL ist langsamer', 'CentOS nur für Desktop'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    Frage(
        fragetext="Welche Distribution ist bekannt für Rolling Releases und pacman?",
        optionen=['Ubuntu', 'Arch Linux', 'Debian', 'CentOS'],
        richtige_antwort=1,
        kategorie="1.1 Linux Evolution"
    ),
    
    # === COMMAND LINE ERWEITERT (2.1) ===
    Frage(
        fragetext="Was macht Command Substitution mit $(command)?",
        optionen=['Kommentiert Command', 'Führt Command aus und setzt Ausgabe ein', 'Löscht Command', 'Wiederholt Command'],
        richtige_antwort=1,
        kategorie="2.1 Command Line Basics"
    ),
    Frage(
        fragetext="Was ist Brace Expansion: echo {A,B,C}?",
        optionen=['Zeigt ABC', 'Erweitert zu A B C', 'Fehler', 'Zeigt {A,B,C}'],
        richtige_antwort=1,
        kategorie="2.1 Command Line Basics"
    ),
    Frage(
        fragetext="Was macht 'Ctrl+R' in der Bash?",
        optionen=['Reboot', 'Rückwärts-Suche in History', 'Reset Terminal', 'Remove Line'],
        richtige_antwort=1,
        kategorie="2.1 Command Line Basics"
    ),
    Frage(
        fragetext="Wo wird die Bash-History standardmäßig gespeichert?",
        optionen=['/etc/history', '~/.bash_history', '/var/log/bash', '/tmp/history'],
        richtige_antwort=1,
        kategorie="2.1 Command Line Basics"
    ),
    Frage(
        fragetext="Was ist die HISTSIZE Variable?",
        optionen=['History löschen', 'Anzahl Befehle die im Speicher gehalten werden', 'Größe der Dateien', 'Terminal-Größe'],
        richtige_antwort=1,
        kategorie="2.1 Command Line Basics"
    ),
    
    # === NETZWERK ERWEITERT (4.4) ===
    Frage(
        fragetext="Was ist 127.0.0.1?",
        optionen=['Router-Adresse', 'Localhost/Loopback-Adresse', 'Broadcast', 'Gateway'],
        richtige_antwort=1,
        kategorie="4.4 Computer on Network"
    ),
    Frage(
        fragetext="Was ist ein Gateway im Netzwerk?",
        optionen=['Firewall', 'Router/Ausgang zu anderen Netzwerken', 'Switch', 'Modem'],
        richtige_antwort=1,
        kategorie="4.4 Computer on Network"
    ),
    Frage(
        fragetext="Was bedeutet die Subnetzmaske 255.255.255.0?",
        optionen=['/8 Netzwerk', '/24 Netzwerk (Class C)', '/16 Netzwerk', '/32 Host'],
        richtige_antwort=1,
        kategorie="4.4 Computer on Network"
    ),
    Frage(
        fragetext="Was ist CIDR-Notation /24?",
        optionen=['24 Hosts', '24 Bit für Netzwerkanteil (255.255.255.0)', '24 Router', '24 Ports'],
        richtige_antwort=1,
        kategorie="4.4 Computer on Network"
    ),
    Frage(
        fragetext="Welcher Port ist standard für DNS?",
        optionen=['25', '53', '80', '443'],
        richtige_antwort=1,
        kategorie="4.4 Computer on Network"
    ),
    Frage(
        fragetext="Was macht 'netstat -tulnp'?",
        optionen=['Testet Netzwerk', 'Zeigt listening Ports mit Prozessen', 'Startet Netzwerk', 'Konfiguriert Ports'],
        richtige_antwort=1,
        kategorie="4.4 Computer on Network"
    ),
    
    # === DATEISYSTEM ERWEITERT (4.2, 4.3) ===
    Frage(
        fragetext="Was ist ein Inode?",
        optionen=['Internet Node', 'Index Node - Datenstruktur für Datei-Metadaten', 'Input Node', 'Internal Node'],
        richtige_antwort=1,
        kategorie="4.2 Computer Hardware"
    ),
    Frage(
        fragetext="Welches Dateisystem ist Standard bei modernen Linux-Distributionen?",
        optionen=['FAT32', 'ext4', 'NTFS', 'HFS+'],
        richtige_antwort=1,
        kategorie="4.2 Computer Hardware"
    ),
    Frage(
        fragetext="Was ist XFS?",
        optionen=['X File System - altes DOS System', 'High-Performance Journaling Dateisystem', 'Windows Dateisystem', 'Backup-System'],
        richtige_antwort=1,
        kategorie="4.2 Computer Hardware"
    ),
    Frage(
        fragetext="Was ist Btrfs?",
        optionen=['Backup-Tool', 'Modernes Copy-on-Write Dateisystem mit Snapshots', 'Bit Transfer', 'Browser Tool'],
        richtige_antwort=1,
        kategorie="4.2 Computer Hardware"
    ),
]
    return fragen
def hole_antwort(prompt):
    """Holt Nutzer-Input mit Validierung u. Rahmen."""
    while True:
        leer()
        nutzer_input = input(RAHMEN*2 + " " * EINRUECKUNG + prompt).upper()
        
        if nutzer_input in ["A", "B", "C", "D"]:
            return nutzer_input
        else:
            leer()
            zeige_zeile(" FEHLER: Bitte nur A, B, C oder D! ")

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
    # Klassenattribut - zählt alle erstellten Fragen
    anzahl_fragen = 0

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
    
        # Fragen-Anzahl steigern
        Frage.anzahl_fragen += 1 

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

# Hauptprogramm
def main():
    """
    Hauptfunktion - Testet die Frage-Klasse mit Beispiel-Fragen.
    
    Erstellt Test-Fragen, zeigt sie an, fragt den User nach Antworten
    u. gibt Feedback ob die Antwort richtig oder falsch war.
    """
    header()

    fragen_liste = erstelle_fragen()
    richtige_antworten = 0
    zeige_zeile(f" Insgesamt {Frage.anzahl_fragen} Fragen geladen ")
    leer()

    # Quiz durchlaufen
    for i, frage in enumerate(fragen_liste, 1):
        
        zeige_zeile(f" Frage {i} von {len(fragen_liste)} ")
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

    # Endergebnis
    zeige_zeile(f" ENDERGEBNIS: {richtige_antworten}/{len(fragen_liste)} richtig ")
    zeige_zeile(f" Das sind {richtige_antworten/len(fragen_liste)*100:.0f}% ")
    leer()
    trennung()
    leer()

    input(" " * EINRUECKUNG + "ENTER zum Beenden... ")

    footer()

if __name__ == "__main__":
    main()