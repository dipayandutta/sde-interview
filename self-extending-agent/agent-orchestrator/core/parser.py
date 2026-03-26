import re

INTENT_MAP = {
    "add": ["add", "plus", "sum"],
    "subtract": ["subtract", "minus"],
    "multiply": ["multiply", "multiplication", "product"],
    "divide": ["divide", "division"],
}


def extract_numbers(text):
    return list(map(int, re.findall(r"\d+", text)))


def parse_intent(user_input):
    user_input = user_input.lower()
    numbers = extract_numbers(user_input)

    for operation, keywords in INTENT_MAP.items():
        if any(keyword in user_input for keyword in keywords):
            return operation, numbers

    return None, []