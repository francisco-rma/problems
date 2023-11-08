from typing import List
import valid_anagram


def group_anagrams(terms: List[str]) -> List[List[str]]:
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


str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(str_list))
