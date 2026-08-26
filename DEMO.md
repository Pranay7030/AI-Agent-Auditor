# Demo Video Script - Kali Linux Testing
Title: Pranay AI Agent Auditor - Cross Platform Test

Intro: Hello, I am Pranay Meshram. Built on Termux, now testing on Kali Linux.

Step 1: Check OS
uname -a

Step 2: Clone & List
git clone https://github.com/Pranay7030/AI-Agent-Auditor.git
cd AI-Agent-Auditor
ls -lh

Step 3: Run
pip3 install -r requirements.txt
python3 auditor.py

Step 4: Forensic Report
cat audit_report_*.json | head -20

Outro: Proves tool works on Termux + Kali Linux both.
