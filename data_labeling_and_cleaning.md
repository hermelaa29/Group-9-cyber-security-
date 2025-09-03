## 1. INSTALL DOCCANO
``
sudo apt update
``

``
sudo apt install pipx
``

``
pipx ensurepath
``
## CLOSE AND REOPEN YOUR TERMINAL NOW!
``pipx install doccano``


``pipx inject doccano marshmallow==3.20.1``

``pipx inject doccano numpy==1.24.4``

# 2. FIRST-TIME SETUP (RUN ONCE)
``doccano init``

``doccano createuser --username admin --password <newpass>``

# 3. RUN DOCCANO (EVERY TIME)
# OPEN TWO TERMINAL WINDOWS/TABS:

# TERMINAL 1 - WEB SERVER:
``doccano webserver --port 8000``

# TERMINAL 2 - BACKGROUND WORKER:
``doccano task``

# THEN OPEN: http://localhost:8000

# 4. EXTRACT MESSAGES FROM TELEGRAM JSON
# Save this as extract_messages.py first (get the code separately)
``python index.py result.json all_messages.txt``


LABELING SHORTCUTS:

0 = PHISHING

1 = LEGITIMATE

→ = NEXT MESSAGE

↑ = PREVIOUS MESSAGE

s = SKIP


