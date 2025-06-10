from arrays_hashing import valid_anagram


def group_anagrams(terms: list[str]) -> list[list[str]]:
    counts = {}
    grouped_list = []
    for i, value in enumerate(terms):
        count = valid_anagram.count_char(value)
        counts[value] = count

    completed_indices = set()

    for i, x in enumerate(terms):
        if i in completed_indices:
            continue
        group = [x]

        if i == len(terms) - 1:
            grouped_list.append(group)
            continue

        for j, y in enumerate(terms[i + 1 :]):
            if counts[y] == counts[x]:
                group.append(y)
                completed_indices.add(j + i + 1)

        grouped_list.append(group)
    return grouped_list


def group_anagramsV2(terms: list[str]) -> list[list[str]]:
    counts: dict[int, list[str]] = {}
    for _, value in enumerate(terms):
        count: tuple[str, int] = tuple(sorted(valid_anagram.count_char(value).items()))
        if count not in counts:
            counts[count] = []
        counts[count].append(value)

    return counts.values()


str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagramsV2(str_list))
