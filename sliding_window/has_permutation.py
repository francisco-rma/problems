from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False

    result = False
    msg = "No permutations found"
    left = 0
    right = len(s1)

    count1 = Counter(s1)

    while right <= len(s2):
        count2 = Counter(s2[left:right])
        if count1 == count2:
            result = True
            msg = f"Permutation found at ({left},{right-1})"
            break

        left += 1
        right += 1

    print(msg)
    return result


s1, s2 = "abc", "lecaabee"
s1, s2 = "abc", "lecabee"

result = checkInclusion(s1=s1, s2=s2)

print(result)
