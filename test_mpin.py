from mpin_checker import strengthOf_pin

# Trying out different PIN patterns against known dates
def test_pin_strength():
    test_data = [
        #quick throw-in test (used in many ATMs)
        ("2580", "", "18071999", "", "WEAK", ["COMMONLY_USED"]),
        #generic pins
        ("1234", "", "", "", "WEAK", ["COMMONLY_USED"]),
        ("0000", "", "", "", "WEAK", ["COMMONLY_USED"]),
        ("2486", "", "", "", "STRONG", []),
        ("0201", "02011998", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("3948", "22111999", "", "", "STRONG", []),
        ("991505", "", "15051999", "", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("1122", "", "", "", "WEAK", ["COMMONLY_USED"]),
        ("654321", "", "", "", "WEAK", ["COMMONLY_USED"]),
        ("1505", "15051999", "", "15051999", "WEAK", ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_ANNIVERSARY"]),
        ("7777", "", "23072003", "", "WEAK", ["COMMONLY_USED"]),
        # Trying 3 full match cases together (bit redundant?)
        ("1505", "15051999", "15051999", "15051999", "WEAK", [
            "DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"
        ]),
        ("123123", "", "", "", "WEAK", ["COMMONLY_USED"]),
        ("9999", "", "", "", "WEAK", ["COMMONLY_USED"]),
        ("839201", "23082003", "", "", "STRONG", []),
        ("314159", "", "", "", "STRONG", []),
        # Below seems fuzzy... need to verify if 02011998 works in anniv field
        ("0201", "02011998", "", "02011998", "WEAK", ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_ANNIVERSARY"]),
        # Testing with potential real-world dob match
        ("150519", "15051999", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("1004", "", "", "", "WEAK", ["COMMONLY_USED"]),
        # Possibly ambiguous not flagged?
        ("3948", "", "", "", "STRONG", []),
    ]

    success = 0

    for i, case in enumerate(test_data, 1):
        pin, dob, spouse_dob, anniv, expected_strength, expected_reasons = case
        actual_strength, actual_reasons = strengthOf_pin(pin, dob, anniv, spouse_dob)

        # basic validation
        strength_ok = actual_strength == expected_strength
        reasons_ok = set(actual_reasons) == set(expected_reasons)

        if strength_ok and reasons_ok:
            print(f"[{i}] ✔ PASS")
            success += 1
        else:
            print(f"[{i}] ✘ FAIL")
            print(f"   PIN: {pin}")
            print(f"   DOB={dob}, Spouse={spouse_dob}, Anniv={anniv}")
            print(f"   Expected → {expected_strength}, {expected_reasons}")
            print(f"   Got      → {actual_strength}, {actual_reasons}")
            print("-" * 40)

    print(f"\n{success}/{len(test_data)} passed\n")

# Basic manual test
# print(strengthOf_pin("1234", "15051999", "", ""))

if __name__ == "__main__":
    test_pin_strength()
