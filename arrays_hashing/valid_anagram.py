def valid_anagram(term: str, comparison: str) -> bool:
    return count_char(term) == count_char(comparison)


def count_char(s: str) -> dict[str, int]:
    char_count = {}
    for _, value in enumerate(s):
        if value in char_count:
            char_count[value] += 1
        else:
            char_count[value] = 1
    return char_count
