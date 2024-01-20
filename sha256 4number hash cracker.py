import csv
from hashlib import sha256

cracked_pins = []

with open('passwords.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        username = row[0]
        hash = row[1]

        # Brute force all 0000 - 9999 PINs
        for pin in range(0000, 10000):
            pin = str(pin).zfill(4)
            pin_hash = sha256(pin.encode('utf-8')).hexdigest()
            if pin_hash == hash:
                print(f"Cracked PIN for {username}: {pin}")
                cracked_pins.append(pin)
                break

# Analyze cracked PINs
print(f"Total cracked PINs: {len(cracked_pins)}")

# Check for weak PINs like repeated digits, patterns, etc
weak_pins = []
for pin in cracked_pins:
    if pin == pin[0]*len(pin):  # repeated digit check
        weak_pins.append(pin)

print(f"{len(weak_pins)} weak PINs found:")
print(weak_pins)
