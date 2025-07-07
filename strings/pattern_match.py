def wordsPatternsMatch(words, patterns):
    def pattern_match(word, pattern):
        i, j = 0, 0

        for char in word:
            if j >= len(pattern):
                break
            check = char == pattern[j] or pattern[j] == "."

            if check:
                j += 1
            else:
                j = 0

            i += 1

        return j >= len(pattern) - 1

    result = []

    for word in words:
        has_pattern = False
        i = 0

        while i < len(patterns):
            has_pattern = pattern_match(word=word, pattern=patterns[i])

            if has_pattern:
                result.append(patterns[i])
                break
            else:
                i += 1

    return result


words = ["grape", "banana", "melon", "apple", "orange", "expensive"]
patterns = ["a..le", ".anana", "x..", "..ape", "m.lon", "ex.ensive"]


result = wordsPatternsMatch(words=words, patterns=patterns)

print(result)
