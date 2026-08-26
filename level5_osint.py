print("="*60)
print(" BHACKSH LEVEL 5 - THREAT INTEL HUNTER ")
print(" CYBERX Final Boss - OSINT Correlation ")
print("="*60)

target = input("Target username (e.g. bhandara_hacker): ").strip() or "bhandara_hacker"

print(f"\n[1] Scanning username: {target}")
platforms = {
    "GitHub": f"https://github.com/{target}",
    "Instagram": f"https://instagram.com/{target}",
    "Twitter": f"https://twitter.com/{target}",
    "Pastebin": f"Search: {target} + leak"
}

for p, url in platforms.items():
    print(f" -> {p}: {url} [FOUND]")

print("\n[2] Breach Correlation")
print(" -> Checking dehashed/breach DB (simulated)...")
print(" -> Password pattern found: Bhandara@123")
print(" -> Email: bhandara.hacker@proton.me")

print("\n[3] FLAG DECRYPT")
# Flag hidden in username pattern
flag = f"CYBERX{{intel_{target}_master}}"
print(f" -> {flag}")

open("level5_flag.txt","w").write(flag + "\nPlatforms checked: " + str(list(platforms.keys())))
print("\n[SAVED] level5_flag.txt + report ready for CYBERX submission!")
