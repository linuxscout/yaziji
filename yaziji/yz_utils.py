
from yaziji_const import PRONOUNS_INDEX, DAMMA_WORD, FATHA_WORD, KASRA_WORD
from yaziji_const import GENDER_FEMALE, GENDER_MALE, NUMBER_SINGULAR, NUMBER_DUAL, NUMBER_PLURAL, NUMBER_IRRGULAR_PLURAL
from pyarabic import araby
from typing import Union


def get_pronoun(person: str, feminin: bool = False, number: Union[int, str] = 1) -> str:
    """
    Return pronoun based on given features.

    :param person: The grammatical person (e.g., "غائب").
    :param feminin: Boolean indicating if the pronoun should be feminine.
    :param number: The grammatical number (1 for singular, 2 for dual, 3 or more for plural).
    :return: The appropriate pronoun as a string.
    """
    # Convert number to its string representation if it's an integer
    if isinstance(number, int):
        if number == 1:
            number = NUMBER_SINGULAR
        elif number == 2:
            number = NUMBER_DUAL
        elif number >= 3:
            number = NUMBER_PLURAL
        else:
            number = NUMBER_SINGULAR  # Default to singular if the number is invalid

    # Ensure number is in the valid set of values
    if number == NUMBER_IRRGULAR_PLURAL:
        number = NUMBER_PLURAL
    elif number not in (NUMBER_SINGULAR, NUMBER_DUAL, NUMBER_PLURAL):
        number = NUMBER_SINGULAR

    # Determine gender
    gender = GENDER_FEMALE if feminin else GENDER_MALE

    # Ensure person is a valid key in PRONOUNS_INDEX
    if person not in PRONOUNS_INDEX:
        person = "غائب"  # Default to "غائب" if the person is invalid

    # Lookup the pronoun
    pronoun = PRONOUNS_INDEX.get(person, {}).get(gender, {}).get(number, '')

    return pronoun


# Example usage
pronoun = get_pronoun("غائب", feminin=True, number=3)
print(pronoun)  # Output: هن


def equal_future_type(f_one: str, f_two: str) -> bool:
    """
    Test if the first form is the same as the second.

    :param f_one: The first form to compare.
    :param f_two: The second form to compare.
    :return: True if the forms are considered equal, False otherwise.
    """

    # Define groups of equivalent diacritics
    diacritic_groups = [
        (araby.DAMMA, "ضمة"),
        (araby.FATHA, "فتحة"),
        (araby.KASRA, "كسرة")
    ]

    # Check direct equality
    if f_one == f_two:
        return True

    # Check if both forms belong to any of the diacritic groups
    for group in diacritic_groups:
        if f_one in group and f_two in group:
            return True

    return False