from PIL import Image
from PIL.ExifTags import TAGS
import os

def scan_image(image_path):
    print(f"\n[ BHACKSH - Image Intel ] Scanning: {image_path}\n")
    
    # 1. Basic Info
    img = Image.open(image_path)
    print(f"Format: {img.format} | Size: {img.size} | Mode: {img.mode}")

    # 2. EXIF Data - Yahi pe CTF flag chhupa hota hai
    print("\n--- EXIF Data (GPS, Device, Author) ---")
    exif_data = img._getexif()
    if exif_data:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag}: {value}")
            # Flag check
            if "CYBERX" in str(value) or "CTF" in str(value) or "flag" in str(value).lower():
                print(f"\n🚩 FLAG MIL GAYA! -> {value}")
    else:
        print("No EXIF data found - Try strings method")

    # 3. Strings method - Image ko text ki tarah padhna (CTF trick)
    print("\n--- Hidden Text in Image ---")
    with open(image_path, 'rb') as f:
        data = f.read()
        # last 500 chars check karte hai, wahi flag hota hai
        text = data[-2000:].decode('utf-8', errors='ignore')
        if "CYBERX{" in text or "flag{" in text.lower():
            print(f"Hidden Flag Found: {text}")

if __name__ == "__main__":
    path = input("Image ka path daal (e.g. photo.jpg): ")
    scan_image(path)
