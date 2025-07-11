# NOTE: This code covers all 4-digit and 6-digit MPIN rules from Parts A–D of the assignment

# Some of the most frequently used PINs (pulled from common usage patterns, many more can be added)
COMMON_MPINS = {
    "0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999",
    "1234", "4321", "1212", "1122", "2580", "1004", "123123", "112233",
    "123456", "654321", "789456", "147258", "369258", "159753", "852963",
    "741852", "963852", "159357", "753951", "159951", "258963", "369147",
    "789123", "456789", "258024", 
    "000000", "222222", "333333", "444444", "555555", "666666", "777777", "888888", "999999"
}

def is_common_pin(pin: str) -> bool:
    return pin in COMMON_MPINS

# here generating the likely variants from a given date (in DDMMYYYY format)
def generate_date_variants(date: str) -> set[str]:
    if not date or len(date) != 8:
        return set()

    day = date[:2]
    month = date[2:4]
    year = date[4:]
    yy = year[-2:]

    # mixing up common formats
    variants = {
        day + month, month + day,
        yy + month, month + yy,
        day + yy, yy + day,
        day + month + yy,  # DDMMYY
        yy + month + day,
        month + day + yy, month + yy + day,
    }

    return variants

def strengthOf_pin(pin: str, dob: str = "", anniversary: str = "", spouse_dob: str = "") -> tuple[str, list[str]]:
    issues = []

    if is_common_pin(pin):
        issues.append("COMMONLY_USED")
    if dob and pin in generate_date_variants(dob):
        issues.append("DEMOGRAPHIC_DOB_SELF")
    if spouse_dob and pin in generate_date_variants(spouse_dob):
        issues.append("DEMOGRAPHIC_DOB_SPOUSE")
    if anniversary and pin in generate_date_variants(anniversary):
        issues.append("DEMOGRAPHIC_ANNIVERSARY")
    return ("WEAK", issues) if issues else ("STRONG", [])
