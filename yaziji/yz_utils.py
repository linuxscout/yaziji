
from yaziji_const import PRONOUNS_INDEX
def get_pronoun(person, feminin=False, number=1):
    """
    return pronoun based on given features
    :param word:
    :param feminin:
    :param number:
    :return:
    """
    if number not in {"مفرد", "مثنى", "جمع"}:
        number = "مفرد"
    gender = "مؤنث" if feminin else "مذكر"
    pronoun = PRONOUNS_INDEX["غائب"].get(gender, {}).get(number, '')