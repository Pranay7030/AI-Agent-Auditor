from PIL import Image
from PIL.ExifTags import TAGS
import datetime, os

print("[ BHACKSH OSINT PRO - Offline ]")
path = input("Image path: ").strip()

img = Image.open(path)
print(f"Scanning: {path} | {img.size}")

flag = ""
with open(path, 'rb') as f:
    d = f.read().decode(errors='ignore')
    if "CYBERX" in d:
        i = d.find("CYBERX")
        flag = d[i:i+50].split()[0]
        print(f"\nFLAG FOUND: {flag}")

report = f"""BHACKSH Report - {datetime.datetime.now()}
File: {path}
Size: {img.size}
Flag: {flag}
Team: Bhandara Cyber Squad
Status: CYBERX Ready
"""
print("\n" + report)
open("team_report.txt","w").write(report)
print("team_report.txt saved!")
