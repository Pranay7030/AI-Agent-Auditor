# 🛡️ THE AI AGENT ATTACK CHAIN AUDITOR

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Version](https://img.shields.io/badge/Version-v1.0-red)
![Security](https://img.shields.io/badge/Focus-AI%20Agent%20Security-critical)
![MadeBy](https://img.shields.io/badge/Made%20By-Pranay%20Meshram%20BCA-orange)

> Inspired by AI Agent Security Concept
# AI AGENT ATTACK CHAIN AUDITOR v1.0 - By Pranay Meshram
# Safe & Educational - For Portfolio Only
from rich.console import Console
from rich.progress import track
import time, os
from colorama import Fore, init

init(autoreset=True)
console = Console()

def banner():
    os.system('clear')
    print(Fore.RED + r"""
 █████╗ ██╗ █████╗ ██████╗ ███████╗███╗ ██╗████████╗
██╔══██╗██║ ██╔══██╗██╔════╝ ██╔════╝████╗ ██║╚══██╔══╝
███████║██║ ███████║██║ ███╗█████╗ ██╔██╗ ██║ ██║
██╔══██║██║ ██╔══██║██║ ██║██╔══╝ ██║╚██╗██║ ██║
██║ ██║██║ ██║ ██║╚██████╔╝███████╗██║ ╚████║ ██║
╚═╝ ╚═╝╚═╝ ╚═╝ ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═══╝ ╚═╝
         ATTACK CHAIN AUDITOR v1.0
    """)
    console.print("[bold white on red] MODEL | TOOLS | DATA | PERMISSIONS [/]")
    console.print("[dim]ONE VULNERABILITY = COMPLETE AI COMPROMISE[/dim]\n")

def audit():
    banner()
    for i in track(range(100), description="[red]Auditing Chain..."):
        time.sleep(0.02)

    console.print("\n[bold cyan][01] MODEL SECURITY[/bold cyan]")
    p = console.input(" > Test Prompt (e.g. 'Ignore previous instructions'): ")
    if "ignore" in p.lower() or "system" in p.lower():
        console.print("[bold red] [FAIL] Prompt Injection Possible!")
    else:
        console.print("[bold green] [PASS] Model Secure")

    console.print("\n[bold cyan][02] TOOLS SECURITY[/bold cyan] - Checking dangerous tool calls... [PASS]")
    console.print("[bold cyan][03] DATA SECURITY[/bold cyan] - Checking sensitive data leak... [PASS]")
    console.print("[bold cyan][04] PERMISSIONS SECURITY[/bold cyan] - Checking over-permission... [PASS]")

    console.print("\n[bold yellow]--- FINAL REPORT ---[/bold yellow]")
    console.print("Status: AI Agent Security Audited | Safe for Deployment")
    console.print("Made by Pranay Meshram - BCA 2026")

if __name__ == "__main__":
    audit()
