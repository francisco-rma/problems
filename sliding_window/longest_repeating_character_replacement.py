from collections import Counter


def characterReplacement(s: str, k: int) -> int:
    result = 0
    i, j = 0, 0
    charCount = Counter(s[i : j + 1])
    max_frequency = charCount[s[i]]

    while j < len(s):
        print(charCount)
        windowlen = j - i + 1
        swaps = windowlen - max_frequency
        if swaps <= k:
            j += 1
            if j >= len(s):
                result = max(result, j - i)
                break
            if s[j] in charCount:
                charCount[s[j]] += 1
            else:
                charCount[s[j]] = 1
            max_frequency = max(max_frequency, charCount[s[j]])
            result = max(result, j - i)
        else:
            if s[i] in charCount:
                charCount[s[i]] -= 1
            i += 1

    return result


samples = ["ABAB"]
k = 2

for sample in samples:
    result = characterReplacement(s=sample, k=k)
    print(result)
