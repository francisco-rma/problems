from collections import defaultdict


def naive_string_match(source: str, pattern: str) -> bool:
    """
    Check if the source string matches the pattern exactly.
    """
    i, j = 0, 0

    for char in source:
        if j >= len(pattern):
            break

        check = char == pattern[j]

        if check:
            j += 1
        else:
            i += 1
            j = 0

    return j >= len(pattern)


words = ["grape", "banana", "melon", "apple", "orange", "expensive"]
patterns = ["ple", "nana", "x", "ap", "lon", "nsive", "p"]


result = defaultdict(list)
for pattern in patterns:
    for word in words:
        if naive_string_match(source=word, pattern=pattern):
            result[pattern].append(word)

for pattern, matches in result.items():
    print(f"Pattern '{pattern}' matches: {', '.join(matches)}")
