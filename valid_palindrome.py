ignore = set(["", " ", ".", ",", ":", ";", "()", ")", "-"])


def isPalindrome(s: str) -> bool:
    size = len(s)
    half = len(s) // 2
    right = 0
    left = len(s) // 2

    i = 0

    while i <= half:
        a = s[right]
        b = s[len(s) - 1 - i]
        c = s[left]
        d = s[half + 1 + i]
        if s[right] != s[len(s) - 1 - i]:
            return False
        if s[left] != s[half + 1 + i]:
            return False

        i += 1
        right += 1
        left -= 1

    return True


def clean(s: str) -> str:
    returnString = ""
    for index, char in enumerate(s):
        if char not in ignore:
            returnString += char.lower()

    return returnString


s = "A man, a plan, a canal: Panama"

print(isPalindrome(clean(s)))
