from string import ascii_uppercase


def char_count(src: str):
    count = {char: 0 for char in ascii_uppercase}
    for _, value in enumerate(src):
        if value in count:
            count[value] += 1
        else:
            count[value] = 1
    return count


def characterReplacement(s: str, k: int) -> int:
    result = 0
    i, j = 0, 0

    while j < len(s):
        charCount = char_count(s[i : j + 1])
        max_char = max(ascii_uppercase, key=charCount.get)
        windowlen = j - i + 1
        swaps = windowlen - charCount[max_char]
        if swaps <= k:
            j += 1
            result = max(result, j - i)
        else:
            i += 1

    return result


samples = ["AAABABB"]
k = 1

for sample in samples:
    result = characterReplacement(s=sample, k=k)
    print(result)
