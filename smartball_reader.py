import asyncio
import struct
from bleak import BleakClient

# Ersetze dies mit der Adresse/UUID aus dem Scanner-Skript
BALL_ADDRESS = "XX:XX:XX:XX:XX:XX"

# Typische GATT-Characteristic UUIDs des miCoach Smart Ball für Schussdaten
# (HINWEIS: Je nach Firmware-Version variieren die UUIDs leicht)
KICK_DATA_UUID = "00002a56-0000-1000-8000-00805f9b34fb"  # Beispiel UUID / Custom GATT Service

def notification_handler(sender, data: bytearray):
    """Wird automatisch aufgerufen, wenn der Ball nach einem Kick Daten sendet."""
    print(f"\n⚽ SCHUSS ERFASST! Rohdaten ({len(data)} Bytes): {data.hex()}")
    
    # Der Ball schickt strukturierte Binary-Daten (Little Endian)
    # Beispiel für das Entpacken der Byte-Struktur (vereinfachtes Schema):
    if len(data) >= 8:
        # Die ersten Bytes enthalten meist Speed & Spin
        raw_speed, raw_spin = struct.unpack("<HH", data[:4])
        
        # Umrechnung gemäß miCoach Protokoll-Spezifikation:
        speed_kmh = round(raw_speed * 0.1, 1)  # Geschwindigkeit in km/h
        spin_rpm = raw_spin                    # Umdrehungen pro Minute
        
        print(f" -> Geschwindigkeit: {speed_kmh} km/h")
        print(f" -> Rotation/Spin:  {spin_rpm} RPM")

async def run():
    print(f"Verbinde mit adidas Smart Ball ({BALL_ADDRESS})...")
    async with BleakClient(BALL_ADDRESS) as client:
        print(" Connected! Warte auf Schüsse...")
        
        # Benachrichtigungen einschalten
        await client.start_notify(KICK_DATA_UUID, notification_handler)
        
        print("Der Ball ist schussbereit. Tritt den Ball!")
        # Halte das Skript aktiv, um auf Schüsse zu warten
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\nBeendet.")
