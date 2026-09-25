import asyncio
from bleak import BleakScanner

async def main():
    print("Suche nach BLE-Geräten (Tippe den Ball an, damit er aufwacht)...")
    devices = await BleakScanner.discover()
    for d in devices:
        if d.name and "Smart Ball" in d.name or "adidas" in d.name.lower():
            print(f"⚽ BALL GEFUNDEN! Name: {d.name}, Adresse/UUID: {d.address}")
        elif d.name:
            print(f"Gerät: {d.name} [{d.address}]")

asyncio.run(main())
