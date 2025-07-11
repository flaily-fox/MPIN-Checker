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
- `mpin_checker.py` – final combined version with all parts (A to D) for both 4,6 digit MPINS
- `test_mpin.py` – includes 20+ test cases to verify the logic  
- `UI_format_mpin_cheker.html` – simple web-based interface to try out the checker

📌 Created as part of a data science assignment for OneBanc.

---

Want to try it?

Run test cases:
```bash
python test_mpin.py
