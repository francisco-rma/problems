def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    char_set = set()
    max_size = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        max_size = max(max_size, r - l + 1)

    return max_size


s = "dvdf"

result = lengthOfLongestSubstring(s)

print(result)
