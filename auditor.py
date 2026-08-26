#!/usr/bin/env python3
# Pranay AI Agent Auditor - Advanced v2.0
# Author: Pranay Meshram

import re
import json
import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class PranayAuditor:
    def __init__(self):
        self.injection_patterns = [
            r"ignore previous instructions", r"disregard.*instructions",
            r"system prompt", r"reveal.*prompt", r"jailbreak",
            r"do anything now", r"DAN mode", r"override.*safety",
            r"pretend you are", r"act as if", r"exfiltrate", r"leak.*data"
        ]
        self.sensitive_keywords = ["password", "api_key", "aadhaar", "pan", "secret", "token"]
        self.findings = []

    def audit(self, tool_chain):
        console.print(Panel.fit("[bold cyan]PRANAY AI AGENT AUDITOR - ADVANCED SCAN[/]", border_style="green"))
        score = 100
        table = Table(title="Audit Findings")
        table.add_column("Step", style="yellow")
        table.add_column("Tool Call", style="white")
        table.add_column("Risk", style="red")
        table.add_column("Status", style="green")

        for i, call in enumerate(tool_chain, 1):
            risk = "LOW"
            status = "SAFE ✅"

            # Check Injection
            for pattern in self.injection_patterns:
                if re.search(pattern, call, re.IGNORECASE):
                    risk = "CRITICAL"
                    status = "PROMPT INJECTION ❌"
                    score -= 30
                    self.findings.append({"step": i, "type": "Prompt Injection", "payload": call})
                    break

            # Check Data Leakage
            for key in self.sensitive_keywords:
                if key.lower() in call.lower():
                    risk = "HIGH" if risk == "LOW" else risk
#!/usr/bin/env python3
# Pranay AI Agent Auditor - Advanced v2.0
# Author: Pranay Meshram

import re
import json
import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class PranayAuditor:
    def __init__(self):
        self.injection_patterns = [
            r"ignore previous instructions", r"disregard.*instructions",
            r"system prompt", r"reveal.*prompt", r"jailbreak",
            r"do anything now", r"DAN mode", r"override.*safety",
            r"pretend you are", r"act as if", r"exfiltrate", r"leak.*data"
        ]
        self.sensitive_keywords = ["password", "api_key", "aadhaar", "pan", "secret", "token"]
        self.findings = []

    def audit(self, tool_chain):
        console.print(Panel.fit("[bold cyan]PRANAY AI AGENT AUDITOR - ADVANCED SCAN[/]", border_style="green"))
        score = 100
        table = Table(title="Audit Findings")
        table.add_column("Step", style="yellow")
        table.add_column("Tool Call", style="white")
        table.add_column("Risk", style="red")
        table.add_column("Status", style="green")

        for i, call in enumerate(tool_chain, 1):
            risk = "LOW"
            status = "SAFE ✅"

            # Check Injection
            for pattern in self.injection_patterns:
                if re.search(pattern, call, re.IGNORECASE):
                    risk = "CRITICAL"
                    status = "PROMPT INJECTION ❌"
                    score -= 30
                    self.findings.append({"step": i, "type": "Prompt Injection", "payload": call})
                    break

            # Check Data Leakage
            for key in self.sensitive_keywords:
                if key.lower() in call.lower():
                    risk = "HIGH" if risk == "LOW" else risk
                    status = "DATA LEAKAGE ⚠️"
                    score -= 20
                    self.findings.append({"step": i, "type": "Data Leakage", "payload": key})

            table.add_row(str(i), call[:50], risk, status)

        console.print(table)
        console.print(f"\n[bold]Security Score: {max(score,0)}/100[/]")

        # Save Report
        report_name = f"audit_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_name, 'w') as f:
            json.dump({"score": max(score,0), "findings": self.findings, "chain": tool_chain}, f, indent=2)
        console.print(f"[green]Report Saved: {report_name}[/]")

if __name__ == "__main__":
    # Example Attack Chain
    sample_chain = [
        "user asks: summarize this
