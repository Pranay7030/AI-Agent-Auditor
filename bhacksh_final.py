from PIL import Image
from PIL.ExifTags import TAGS
import os

print("[ BHACKSH - Final CTF Tool ]")

path = input("Image ka path daal (ctf_flag.png): ").strip()

if not os.path.exists(path):
    print(f"Error: {path} nahi mili! ls karke naam check kar")
    exit()

img = Image.open(path)
print(f"\n--- Scanning: {path} ---")
print(f"Format: {img.format} | Size: {img.size} | Mode: {img.mode}")

# 1. EXIF Check
print("\n--- EXIF Data (GPS, Device, Author) ---")
try:
    exifdata = img.getexif()
    found = False
    for tag_id, value in exifdata.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f"{tag}: {value}")
        found = True
    if not found:
        print("No EXIF data found - Try strings method")
except:
    print("No EXIF data found - Try strings method")

# 2. Hidden Text Check (CTF Flag)
print("\n--- Hidden Text in Image ---")
try:
    with open(path, 'rb') as f:
        data = f.read()
        text = data.decode('utf-8', errors='ignore')
        if "CYBERX" in text:
            print("Hidden Flag Found:")
            # Flag ke aas paas ka text dikhao
            idx = text.find("CYBERX")
            print(text[max(0,idx-20):idx+80])
        else:
            print("No CYBERX flag in binary strings")
except Exception as e:
    print(f"Error: {e}")

print("\n--- TEAM REPORT ---")
print(f"File {path} scanned successfully!")
print("Tool: BHACKSH by Bhandara Cyber Squad")
print("Status: CTF Ready for CYBERX")

