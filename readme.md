# MPIN Strength Checker

A simple Python + HTML-based tool to evaluate the strength of a mobile banking MPIN (4 or 6 digits) based on two major criteria:

- Commonly used or predictable PINs
- Demographic patterns (e.g. DOB, anniversary, spouse DOB)

🧩 Features:
- Supports both 4-digit and 6-digit MPINs
- Flags weak PINs and provides clear reasons
- Includes 25+ automated test cases
- Simple HTML UI for quick testing

📁 Files included:
- part_A.py → Checks if MPIN is common
- part_B.py → Adds DOB/anniversary matching
- part_C.py → Returns reasons for weakness
- mpin_checker.py → Final combined logic (Parts A to D)
- test_mpin.py → Validates with multiple test cases
- UI_format_mpin_cheker.html → Interactive form for browser
- README.md → You're reading it 🙂

📌 Created as part of a data science assignment for OneBanc.

---

Want to try it?

Run test cases:
```bash
python test_mpin.py
