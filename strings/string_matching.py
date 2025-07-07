from collections import defaultdict
import re


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
            continue
        s += 1
    return result


def extract_sample(
    path: str, split_pattern: str = r"[\s:;.,()\[\]{}\"'=<>!#@\\/\|\-\+\*\&%$^`~]+"
) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        avl_content = f.read()
    return [w for w in re.split(split_pattern, avl_content) if w]


words = extract_sample("search/matrix_search.py")
patterns = extract_sample("trees/avl_tree.py")


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
