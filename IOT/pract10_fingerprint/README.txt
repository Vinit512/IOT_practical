| Fingerprint Pin | Wire   | Connect to USB-TTL |
| --------------- | ------ | ------------------ |
| 1. VCC          | Red    | **5V / VCC**       |
| 2. GND          | Black  | **GND**            |
| 3. TX           | Yellow | **RX**             |
| 4. RX           | White  | **TX**             |


commands:
sudo apt update
sudo apt install -y python3-pip python3-serial
pip3 install pyfingerprint --break-system-packages