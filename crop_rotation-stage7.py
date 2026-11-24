# === Stage 7: Поиск по нескольким словам ===
# Project: CropRotation
"""
crop_rotation_search.py

Search utilities for the CropRotation project.
Provides a keyword search over garden beds (gрядок) with support for
negation via a leading dash ("-word").
"""

from typing import List, Iterable


def _tokenize(query: str) -> List[str]:
    """Split the query into tokens, keeping leading dashes attached.

    Examples:
        "tomato -onion"      -> ["tomato", "-onion"]
        "tomato -onion -carrot" -> ["tomato", "-onion", "-carrot"]
        ""                   -> []
    """
    tokens = []
    for token in query.replace(",", " ").split():
        if token:
            tokens.append(token)
    return tokens


def _matches(bed_name: str, tokens: List[str]) -> bool:
    """Return True if the bed name satisfies the token set.

    A token without a leading dash is a required keyword: the bed name
    must contain it (case-insensitive).
    A token with a leading dash is a forbidden keyword: the bed name
    must NOT contain it (case-insensitive).
    """
    required = []
    forbidden = []
    for token in tokens:
        if token.startswith("-"):
            forbidden.append(token[1:].lower())
        else:
            required.append(token.lower())

    for keyword in required:
        if keyword not in bed_name.lower():
            return False

    for keyword in forbidden:
        if keyword in bed_name.lower():
            return False

    return True


def find_beds(
    beds: Iterable[str],
    query: str,
) -> List[str]:
    """Return the names of beds matching the search query.

    Args:
        beds: An iterable of bed name strings.
        query: A space- or comma-separated list of keywords. Prefix a
               keyword with "-" to exclude beds containing it.

    Examples:
        find_beds(["tomato bed", "onion bed", "carrot bed"], "tomato")
            -> ["tomato bed"]
        find_beds(["tomato bed", "onion bed", "carrot bed"], "tomato -onion")
            -> ["tomato bed", "carrot bed"]
    """
    tokens = _tokenize(query)
    if not tokens:
        return []

    return [bed for bed in beds if _matches(bed, tokens)]


if __name__ == "__main__":
    sample_beds = [
        "tomato bed",
        "onion bed",
        "carrot bed",
        "pepper bed",
        "tomato-onion mixed bed",
    ]

    print("tomato:", find_beds(sample_beds, "tomato"))
    print("onion -onion:", find_beds(sample_beds, "onion -onion"))
    print("root -onion:", find_beds(sample_beds, "root -onion"))
