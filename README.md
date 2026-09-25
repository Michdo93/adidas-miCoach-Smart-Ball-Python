# adidas-miCoach-Smart-Ball-Python

Der **adidas miCoach Smart Ball** ist hardwaretechnisch ein extrem faszinierendes Stück Technik. Da adidas die miCoach-Plattform eingestellt hat, sind die Bälle für normale App-Nutzer "nutzlos" geworden – für Bastler mit Python und Bluetooth Smart (BLE) aber ein absoluter Schatz.

---

## Welche Werte können erfasst werden?

Im Inneren des Balls hängt an Federaufhängungen ein Paket aus **3-Achsen-Beschleunigungssensoren und Gyroskopen**. Über das Bluetooth Low Energy (BLE) Protokoll überträgt der Ball folgende Sensorwerte:

1. **Schuss-Geschwindigkeit (Ball Speed):** Gemessen in km/h oder mph (berechnet aus der Impuls-Beschleunigung beim Treffpunkt).
2. **Rotation / Spin (Umdrehungen pro Minute):** Wie stark dreht sich der Ball (z. B. bei einem Schnittball / Schnitt-Freistoß im "Bananenflanken"-Stil).
3. **Treffpunkt am Ball (Impact Point):** Wo genau hat der Schuh den Ball getroffen (mittig, unten für Unterschnitt, seitlich für Drall).
4. **Flugbahn-Vektor (Trajectory / Impact Direction):** Die Richtung des Kraftimpulses in $X$-, $Y$- und $Z$-Achse.
5. **Akkustand & Ladezustand:** Die Spannung des internen Akkus sowie der Status der Induktionsladestation.

---

## Wie funktioniert das Auslesen per Python?

Der Ball sendet Daten über Standard-BLE-GATT-Services. Wenn der Ball ruht, befindet er sich im Standby. Ein Stoß oder Tritt "weckt" die Sensoren auf, woraufhin der Ball die Messdaten sammelt und über eine Bluetooth-GATT-Characteristic pusht.

Unter Python nutzt man am besten das moderne und plattformübergreifende Framework **`bleak`**.

### 1. Python-Bibliothek installieren

```bash
pip install bleak asyncio
```

### 2. Schritt 1: Den Ball per BLE suchen (Bluetooth Scan)

Zuerst musst du den Ball aufwecken (einmal leicht auf den Boden tippen/kicken) und seine MAC-Adresse bzw. UUID ermitteln.

```
python3 smartball_scan.py
```

### 3. Schritt 2: Sensordaten & Schüsse auslesen (`smartball_reader.py`)

Wenn du die Adresse (z. B. `XX:XX:XX:XX:XX:XX` unter Linux/Raspberry Pi oder eine UUID unter macOS/Windows) hast, kannst du die Benachrichtigungen (Notifications) der Sensor-Characteristic abonnieren.

```
python3 smartball_reader.py
```

---

## Was kann man damit Cooles bauen?

Da du die Rohdaten in Python hast, kannst du das Projekt perfekt in dein Smart Home oder Labor integrieren:

* **Speed-Messanlage für den Garten / Garage:** Verbinde den Raspberry Pi mit einem Display oder LED-Strip. Nach jedem Torschuss leuchtet der Strip rot/grün auf und zeigt die km/h an.
* **Audio-Ausgabe (Text-to-Speech):** Der Raspberry Pi liest die Schussgeschwindigkeit über einen Lautsprecher vor ("Schussgeschwindigkeit: 84 Kilometer pro Stunde!").
* **MQTT & openHAB Integration:** Schicke jeden Schuss direkt in deine openHAB-Datenbank, um eine Highscore-Tabelle oder Grafana-Diagramme für die besten Torschüsse deiner Familie/Freunde anzulegen.
