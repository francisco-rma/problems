from collections import defaultdict
from typing import Optional
import re


def naive_string_match(source: str, pattern: str) -> tuple[bool, Optional[int]]:
    """
    Check if the source string matches the pattern exactly.
    """
    i, j = 0, 0

    for idx, char in enumerate(source):
        if j >= len(pattern):
            break

        check = char == pattern[j]

        if check:
            j += 1
        else:
            i = idx + 1
            j = 0

    result = j >= len(pattern)

    return result, i


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
        is_match, offset = naive_string_match(source=word, pattern=pattern)

        if is_match:
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
