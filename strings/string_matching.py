from collections import defaultdict
import re
import random


def random_string(size: int, seed: int = None) -> str:
    """
    Generate a random string of given size. Optionally seedable for reproducibility.
    """
    import string

    rng = random.Random(seed)
    alphabet = string.ascii_lowercase + string.digits
    return "".join(rng.choices(alphabet, k=size))


def naive_string_match(text: str, pattern: str) -> list[int]:
    """
    Check if the source string matches the pattern exactly.
    """
    if len(pattern) == 0:
        return []
    n, m = len(text), len(pattern)
    result: list[int] = []
    s = 0
    while s <= (n - m):
        if text[s : s + m] == pattern:
            result.append(s)
            s += m
        else:
            s += 1
    return result


def horner_rule(text: str, idx: int) -> int:
    if idx < 0 or idx >= len(text):
        return 0
    ord_val = ord(text[idx])
    hr = horner_rule(text, idx - 1)
    exponent = len(text) - idx - 1
    return (10**exponent) * ord_val + hr


def extract_sample(
    path: str, split_pattern: str = r"[\s:;.,()\[\]{}\"'=<>!#@\\/\|\-\+\*\&%$^`~]+"
) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        avl_content = f.read()
    return [w for w in re.split(split_pattern, avl_content) if w]


def match_files(
    text_path: str = "search/matrix_search.py", pattern_path: str = "trees/avl_tree.py"
):
    """
    Match patterns from one file against words in another file.
    """

    words = extract_sample(text_path)
    patterns = extract_sample(pattern_path)

    result = defaultdict(set)
    for pattern in patterns:
        result[pattern]
        for word in words:
            results = naive_string_match(text=word, pattern=pattern)
            is_match = len(results) > 0
            if is_match:
                for offset in results:
                    assert word[offset : offset + len(pattern)] == pattern
                result[pattern].add(word)

    for pattern, matches in result.items():
        print(f"Pattern '{pattern}' matches: {', '.join(matches)}")

    sorted_patterns = sorted(result.keys(), key=lambda x: len(result[x]))
    for pattern in sorted_patterns:
        print(f"Pattern '{pattern}' - # of matches: {len(result[pattern])}")

    print(
        "Unmatched patterns: ",
        len(list(filter(lambda x: len(x) == 0, result.values()))),
    )
    print(
        "patterns with more than one match: ",
        len(list(filter(lambda x: len(x) > 0, result.values()))),
    )


def ex1():
    pattern = "0001"
    text = "000010001010001"
    result = naive_string_match(text, pattern)
    print(f"Pattern '{pattern}' found at positions: {result}")


source = random_string(10000)
pattern = random_string(2)

print(f"Source: {source}")
print(f"Pattern: {pattern}")

result = naive_string_match(source, pattern)
print(f"Pattern found at positions: {result}")
